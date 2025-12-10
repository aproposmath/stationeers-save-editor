import dataclasses
from typing import Any
import zipfile
from pathlib import Path
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.parsers import XmlParser
import re
import orjson
from html import escape
import base64


from .schema import *

class SaveData:
    children: dict[int, ReferencableSaveData] = {}
    by_id: dict[int, ReferencableSaveData] = {}
    humans: list[HumanSaveData] = []
    ic_chips: list[ProgrammableChipSaveData] = []
    filename: str

    def __init__(self, filename: str):
        self.children = {}
        self.by_id = {}
        self.filename = filename
        self.humans = []
        if filename.endswith(".save"):
            import zipfile

            with zipfile.ZipFile(filename, "r") as z:
                with z.open("world.xml") as f:
                    data = f.read()
            parser = XmlParser()
            self.data = parser.from_string(data.decode("utf-8"), WorldData)
        elif filename.endswith(".xml"):
            parser = XmlParser()
            self.data = parser.parse(filename, WorldData)
        else:
            raise ValueError("Unsupported file type: " + filename)

        self.traverse(self.data)

    def traverse(self, obj: Any, depth=0):
        if dataclasses.is_dataclass(obj):
            if isinstance(obj, HumanSaveData):
                # print("Found human:", obj)
                self.humans.append(obj)
            if isinstance(obj, ProgrammableChipSaveData):
                self.ic_chips.append(obj)
            if hasattr(obj, "reference_id"):
                self.by_id[obj.reference_id] = obj
            if hasattr(obj, "parent_reference_id"):
                pref = obj.parent_reference_id
                if pref not in self.children:
                    self.children[pref] = []
                self.children[pref].append(obj)
            for field in dataclasses.fields(obj):
                value = getattr(obj, field.name)
                if dataclasses.is_dataclass(value):
                    self.traverse(value, depth + 2)
                elif isinstance(value, list):
                    for item in value:
                        self.traverse(item, depth + 3)
        elif isinstance(obj, list):
            for item in obj:
                self.traverse(item, depth)

    def apply_recursively(self, obj, func):
        func(obj)
        if hasattr(obj, "reference_id"):
            obj_id = obj.reference_id
            if obj_id in self.children:
                for child in self.children[obj_id]:
                    self.apply_recursively(child, func)

    def save(self, filename: str):
        config = SerializerConfig(pretty_print=True, xml_declaration=False)
        serializer = XmlSerializer(config=config)
        out = serializer.render(self.data)
        out = re.sub(r"(\S)/>", r"\1 />", out)
        out = re.sub(r"(\d+)\.0(?!\d)", r"\1", out)
        out = out.replace(' xsi:nil="true"', "")

        out = out.replace(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"', "")

        out = '<?xml version="1.0"?>\n' + out
        out = out.replace(
            "<WorldData Id=",
            '<WorldData xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" Id=',
        )
        out = out.replace("\r\n", "\n").replace("\n", "\r\n")
        out = out.strip()

        n = 0
        m = 0
        for c in out:
            if c == "\n":
                n += 1
            if c == "\r":
                m += 1

        if filename.endswith(".xml"):
            Path(filename).write_text(out, encoding="utf-8")
            return

        if not filename.endswith(".save"):
            raise ValueError("Can only save to .save or .xml files")

        if not self.filename.endswith(".save"):
            raise ValueError("Can only save to .save files if loaded from .save")

        ori_data = {}
        with zipfile.ZipFile(self.filename, "r") as zin:
            for item in zin.infolist():
                if item.filename != "world.xml":
                    ori_data[item.filename] = zin.read(item.filename)

        with zipfile.ZipFile(filename, "w", zipfile.ZIP_DEFLATED) as z:
            z.writestr("world.xml", out)
            for k, v in ori_data.items():
                z.writestr(k, v)

    def print_info(self):
        print("Save file:", self.filename)
        print("Total objects with IDs:", len(self.by_id))

        for id_, obj in self.by_id.items():
            if isinstance(obj, SimpleFabricatorSaveData):
                name = obj.prefab_name
                if name.startswith("Structure"):
                    name = name[len("Structure") :]
                print(f"{name:20} ID={id_:5} at {obj.world_position}")

        for human in self.humans:
            print(f"Human ID={human.reference_id}")
            print(f"\tPosition:     {human.world_position}")
            print(f"\tOxygen:       {human.oxygenation:5.3f}")
            print(f"\tNutrition:    {human.nutrition:5.3f}")
            print(f"\tHydration:    {human.hydration:5.3f}")
            print(f"\tMood:         {human.mood:5.3f}")
            print(f"\tHygiene:      {human.hygiene:5.3f}")
            print(f"\tFood quality: {human.food_quality:5.3f}")
            print(f"\tDays alive:   {human.days_lived}")
            print(f"\tDamage:       {human.damage_state}")

    def get_info_json(self):
        data = {}
        data["info_html"] = self.print_info_html() + self.get_ic10_codes()
        icons = []

        data['humans'] = [dataclasses.asdict(h) for h in self.humans]
        data['data'] = dataclasses.asdict(self.data)


        for human in self.humans:
            p = human.world_position
            icons.append(
                {
                    "type": "player",
                    "position": [p.x, p.y, p.z],
                }
            )

        for obj in self.by_id.values():
            if isinstance(obj, SimpleFabricatorSaveData):
                name = obj.prefab_name.strip()
                if name.startswith("Structure"):
                    name = name[len("Structure") :]
                if name == 'Autolathe':
                    p = obj.world_position
                    icons.append(
                        {
                            "type": "autolathe",
                            "position": [p.x, p.y, p.z],
                        }
                    )
        data['icons'] = icons
        data['planet'] = self.data.world_setting.id.replace("2", "").lower()
        return orjson.dumps(data)


    def print_info_html(self):
        structures_rows = ""
        for id_, obj in self.by_id.items():
            if isinstance(obj, SimpleFabricatorSaveData):
                name = obj.prefab_name
                if name.startswith("Structure"):
                    name = name[len("Structure"):]
                pos = obj.world_position
                pos_str = f"({pos.x:5.1f}, {pos.y:5.1f}, {pos.z:5.1f})"
                structures_rows += f"""
                    <tr>
                        <td>{escape(name)}</td>
                        <td>{escape(str(id_))}</td>
                        <td>{escape(pos_str)}</td>
                    </tr>
                """

        human_sections = ""
        for human in self.humans:
            human_sections += f"""
                <details>
                    <summary>Human ID={human.reference_id}</summary>
                    <ul>
                        <li><strong>Position:</strong> {escape(str(human.world_position))}</li>
                        <li><strong>Oxygen:</strong> {human.oxygenation:5.3f}</li>
                        <li><strong>Nutrition:</strong> {human.nutrition:5.3f}</li>
                        <li><strong>Hydration:</strong> {human.hydration:5.3f}</li>
                        <li><strong>Mood:</strong> {human.mood:5.3f}</li>
                        <li><strong>Hygiene:</strong> {human.hygiene:5.3f}</li>
                        <li><strong>Food quality:</strong> {human.food_quality:5.3f}</li>
                        <li><strong>Days alive:</strong> {human.days_lived}</li>
                        <li><strong>Damage state:</strong> {escape(str(human.damage_state))}</li>
                    </ul>
                </details>
            """

        return f"""
        <h1>Save File Info</h1>
        <p><strong>File:</strong> {escape(str(self.filename))}</p>
        <p><strong>Total objects with IDs:</strong> {len(self.by_id)}</p>

        <h2>Structures</h2>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>ID</th>
                    <th>World Position</th>
                </tr>
            </thead>
            <tbody>
                {structures_rows}
            </tbody>
        </table>

        <h2>Humans</h2>
        {human_sections}
    """

    def move_player(self, x, y, z):
        if not self.humans:
            raise ValueError("No humans found in save data")
        human = self.humans[0]

        p = human.world_position
        dx = x-p.x
        dy = y-p.y
        dz = z-p.z

        def move_obj(obj):
            if hasattr(obj, "world_position"):
                obj.world_position.x += dx
                obj.world_position.y += dy
                obj.world_position.z += dz

        self.apply_recursively(human, move_obj)

    def heal_players(self):
        for human in self.humans:
            state : DamageUpdate = human.damage_state
            state.brute = 0
            state.burn = 0
            state.oxygen = 0
            state.hydration = 0
            state.starvation = 0
            state.toxic = 0
            state.radiation = 0
            state.stun = 0
            state.decay = 0



    def get_ic10_codes(self):
        codes = {chip.reference_id: chip.source_code for chip in self.ic_chips}

        html = '<h1>IC-10 Chip Codes</h1>\n'


        for chip_id, code in codes.items():
            code_b64 = base64.b64encode(code.encode('utf-8')).decode('utf-8')
            html += f'''
            <details class="chip-block">
                <summary>Chip ID: {chip_id}</summary>
                <div class="code-wrapper">
                    <button class="copy-btn" onclick="navigator.clipboard.writeText(window.atob('{code_b64}'))">Copy</button>
                    <pre><code>{escape(code)}</code></pre>
                </div>
            </details>
            '''
        return html
