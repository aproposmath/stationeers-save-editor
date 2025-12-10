from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


@dataclass
class AchievementData:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    send_to_all: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SendToAll",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ActionData:
    pass


class ArmState(Enum):
    UNDEFINED = "Undefined"
    UP = "Up"
    DOWN = "Down"
    ANIMATING_DOWN = "AnimatingDown"
    ANIMATING_UP = "AnimatingUp"


@dataclass
class ArrayOfInt:
    build_state: list[int] = field(
        default_factory=list,
        metadata={
            "name": "BuildState",
            "type": "Element",
        },
    )


@dataclass
class ArrayOfInt1:
    int_value: list[int] = field(
        default_factory=list,
        metadata={
            "name": "int",
            "type": "Element",
        },
    )


@dataclass
class ArrayOfLong:
    long: list[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ArrayOfLong1:
    network_id: list[int] = field(
        default_factory=list,
        metadata={
            "name": "NetworkId",
            "type": "Element",
        },
    )


@dataclass
class ArrayOfString:
    tag: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Tag",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfString1:
    prefab_name: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PrefabName",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfString2:
    requirement: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Requirement",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfString3:
    string: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfString4:
    path: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Path",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfString5:
    setting_name: list[str] = field(
        default_factory=list,
        metadata={
            "name": "SettingName",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfString6:
    string: list[str] = field(
        default_factory=list,
        metadata={
            "name": "String",
            "type": "Element",
            "nillable": True,
        },
    )


class AudioSpeakerMode(Enum):
    MONO = "Mono"
    STEREO = "Stereo"
    QUAD = "Quad"
    SURROUND = "Surround"
    MODE5POINT1 = "Mode5point1"
    MODE7POINT1 = "Mode7point1"
    PROLOGIC = "Prologic"


class BatteryCellState(Enum):
    EMPTY = "Empty"
    CRITICAL = "Critical"
    LOW = "Low"
    VERY_LOW = "VeryLow"
    MEDIUM = "Medium"
    HIGH = "High"
    FULL = "Full"


@dataclass
class BoolReference:
    value: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class BulkMultiplier:
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CelestialSaveData:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass
class ChanceData:
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )


class Class(Enum):
    NONE = "None"
    HELMET = "Helmet"
    SUIT = "Suit"
    BACK = "Back"
    GAS_FILTER = "GasFilter"
    GAS_CANISTER = "GasCanister"
    MOTHERBOARD = "Motherboard"
    CIRCUITBOARD = "Circuitboard"
    DATA_DISK = "DataDisk"
    ORGAN = "Organ"
    ORE = "Ore"
    PLANT = "Plant"
    UNIFORM = "Uniform"
    ENTITY = "Entity"
    BATTERY = "Battery"
    EGG = "Egg"
    BELT = "Belt"
    TOOL = "Tool"
    APPLIANCE = "Appliance"
    INGOT = "Ingot"
    TORPEDO = "Torpedo"
    CARTRIDGE = "Cartridge"
    ACCESS_CARD = "AccessCard"
    MAGAZINE = "Magazine"
    CIRCUIT = "Circuit"
    BOTTLE = "Bottle"
    PROGRAMMABLE_CHIP = "ProgrammableChip"
    GLASSES = "Glasses"
    CREDIT_CARD = "CreditCard"
    DIRT_CANISTER = "DirtCanister"
    SENSOR_PROCESSING_UNIT = "SensorProcessingUnit"
    LIQUID_CANISTER = "LiquidCanister"
    LIQUID_BOTTLE = "LiquidBottle"
    WRECKAGE = "Wreckage"
    SOUND_CARTRIDGE = "SoundCartridge"
    DRILL_HEAD = "DrillHead"
    SCANNING_HEAD = "ScanningHead"
    FLARE = "Flare"
    BLOCKED = "Blocked"
    SUIT_MOD = "SuitMod"
    CRATE = "Crate"
    PORTABLES = "Portables"
    ROCKET_PAYLOAD = "RocketPayload"


@dataclass
class CloudShadowReference:
    opacity: Optional[float] = field(
        default=None,
        metadata={
            "name": "Opacity",
            "type": "Attribute",
            "required": True,
        },
    )
    parallax: Optional[float] = field(
        default=None,
        metadata={
            "name": "Parallax",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ColorRgb:
    class Meta:
        name = "ColorRGB"

    r: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    g: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    b: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ColorReference:
    pass


@dataclass
class ColorSwatchReference:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass
class Color1:
    class Meta:
        name = "Color"

    r: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    g: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    b: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    a: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


class CompareOperator(Enum):
    UNASSIGNED = "Unassigned"
    LESS = "Less"
    EQUAL_OR_LESS = "EqualOrLess"
    EQUAL = "Equal"
    EQUAL_OR_GREATER = "EqualOrGreater"
    GREATER = "Greater"


@dataclass
class ConditionData:
    conditions: list[ConditionDataCollection] = field(
        default_factory=list,
        metadata={
            "name": "Conditions",
            "type": "Element",
        },
    )
    room: list[RoomCondition] = field(
        default_factory=list,
        metadata={
            "name": "Room",
            "type": "Element",
        },
    )
    network: list[NetworkCondition] = field(
        default_factory=list,
        metadata={
            "name": "Network",
            "type": "Element",
        },
    )
    survival_property: list[SurvivalPropertyCondition] = field(
        default_factory=list,
        metadata={
            "name": "SurvivalProperty",
            "type": "Element",
        },
    )
    custom_name: list[CustomNameCondition] = field(
        default_factory=list,
        metadata={
            "name": "CustomName",
            "type": "Element",
        },
    )
    prefab: list[ThingPrefabCondition] = field(
        default_factory=list,
        metadata={
            "name": "Prefab",
            "type": "Element",
        },
    )
    contact: list[TraderContactCondition] = field(
        default_factory=list,
        metadata={
            "name": "Contact",
            "type": "Element",
        },
    )
    size: list[SizeCondition] = field(
        default_factory=list,
        metadata={
            "name": "Size",
            "type": "Element",
        },
    )
    temperature: list[TemperatureComparableCondition] = field(
        default_factory=list,
        metadata={
            "name": "Temperature",
            "type": "Element",
        },
    )
    growth_state: list[GrowthStateCondition] = field(
        default_factory=list,
        metadata={
            "name": "GrowthState",
            "type": "Element",
        },
    )
    plant_status: list[PlantStatusCondition] = field(
        default_factory=list,
        metadata={
            "name": "PlantStatus",
            "type": "Element",
        },
    )
    plant_record: list[PlantRecordCondition] = field(
        default_factory=list,
        metadata={
            "name": "PlantRecord",
            "type": "Element",
        },
    )
    logic_type: list[LogicCondition] = field(
        default_factory=list,
        metadata={
            "name": "LogicType",
            "type": "Element",
        },
    )
    reagents: list[ReagentCondition] = field(
        default_factory=list,
        metadata={
            "name": "Reagents",
            "type": "Element",
        },
    )
    build_state: list[BuildStateCondition] = field(
        default_factory=list,
        metadata={
            "name": "BuildState",
            "type": "Element",
        },
    )
    interactable: list[InteractableCondition] = field(
        default_factory=list,
        metadata={
            "name": "Interactable",
            "type": "Element",
        },
    )
    quantity: list[Quantity] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
        },
    )
    decay: list[Decay] = field(
        default_factory=list,
        metadata={
            "name": "Decay",
            "type": "Element",
        },
    )
    gas: list[GasCondition] = field(
        default_factory=list,
        metadata={
            "name": "Gas",
            "type": "Element",
        },
    )
    pressure: list[PressureCondition] = field(
        default_factory=list,
        metadata={
            "name": "Pressure",
            "type": "Element",
        },
    )
    temperature_range: list[TemperatureRangeCondition] = field(
        default_factory=list,
        metadata={
            "name": "TemperatureRange",
            "type": "Element",
        },
    )
    percent: list[Percent] = field(
        default_factory=list,
        metadata={
            "name": "Percent",
            "type": "Element",
        },
    )
    item: list[Item] = field(
        default_factory=list,
        metadata={
            "name": "Item",
            "type": "Element",
        },
    )
    moles: list[Moles] = field(
        default_factory=list,
        metadata={
            "name": "Moles",
            "type": "Element",
        },
    )
    charge: list[Energy] = field(
        default_factory=list,
        metadata={
            "name": "Charge",
            "type": "Element",
        },
    )
    difficulty: list[Difficulty] = field(
        default_factory=list,
        metadata={
            "name": "Difficulty",
            "type": "Element",
        },
    )
    species: list[Species] = field(
        default_factory=list,
        metadata={
            "name": "Species",
            "type": "Element",
        },
    )
    pre_spawned: list[PreSpawnedCondition] = field(
        default_factory=list,
        metadata={
            "name": "PreSpawned",
            "type": "Element",
        },
    )
    in_cell: list[InCellCondition] = field(
        default_factory=list,
        metadata={
            "name": "InCell",
            "type": "Element",
        },
    )
    region: list[RegionCondition] = field(
        default_factory=list,
        metadata={
            "name": "Region",
            "type": "Element",
        },
    )
    surface: list[SurfaceCondition] = field(
        default_factory=list,
        metadata={
            "name": "Surface",
            "type": "Element",
        },
    )
    depth: list[DepthCondition] = field(
        default_factory=list,
        metadata={
            "name": "Depth",
            "type": "Element",
        },
    )
    hidden: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Hidden",
            "type": "Attribute",
            "required": True,
        },
    )


class ConditionOperation(Enum):
    EQUALS = "Equals"
    GREATER = "Greater"
    LESS = "Less"
    NOT_EQUALS = "NotEquals"


@dataclass
class ContactSlotSaveData:
    id_hash: Optional[int] = field(
        default=None,
        metadata={
            "name": "IdHash",
            "type": "Element",
            "required": True,
        },
    )
    current_contact_reference_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "CurrentContactReferenceId",
            "type": "Element",
            "required": True,
        },
    )
    current_down_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "CurrentDownTime",
            "type": "Element",
            "required": True,
        },
    )
    down_time_remaining: Optional[float] = field(
        default=None,
        metadata={
            "name": "DownTimeRemaining",
            "type": "Element",
            "required": True,
        },
    )


class Controller(Enum):
    NONE = "None"
    JOYSTICK1 = "Joystick1"
    JOYSTICK2 = "Joystick2"
    JOYSTICK3 = "Joystick3"
    JOYSTICK4 = "Joystick4"
    JOYSTICK5 = "Joystick5"
    JOYSTICK6 = "Joystick6"


class ControllerAxis(Enum):
    NONE = "None"
    AXIS1 = "Axis1"
    AXIS2 = "Axis2"
    AXIS3 = "Axis3"
    AXIS4 = "Axis4"
    AXIS5 = "Axis5"
    AXIS6 = "Axis6"


@dataclass
class DamageUpdate:
    brute: Optional[float] = field(
        default=None,
        metadata={
            "name": "Brute",
            "type": "Element",
            "required": True,
        },
    )
    burn: Optional[float] = field(
        default=None,
        metadata={
            "name": "Burn",
            "type": "Element",
            "required": True,
        },
    )
    oxygen: Optional[float] = field(
        default=None,
        metadata={
            "name": "Oxygen",
            "type": "Element",
            "required": True,
        },
    )
    hydration: Optional[float] = field(
        default=None,
        metadata={
            "name": "Hydration",
            "type": "Element",
            "required": True,
        },
    )
    starvation: Optional[float] = field(
        default=None,
        metadata={
            "name": "Starvation",
            "type": "Element",
            "required": True,
        },
    )
    toxic: Optional[float] = field(
        default=None,
        metadata={
            "name": "Toxic",
            "type": "Element",
            "required": True,
        },
    )
    radiation: Optional[float] = field(
        default=None,
        metadata={
            "name": "Radiation",
            "type": "Element",
            "required": True,
        },
    )
    stun: Optional[float] = field(
        default=None,
        metadata={
            "name": "Stun",
            "type": "Element",
            "required": True,
        },
    )
    decay: Optional[float] = field(
        default=None,
        metadata={
            "name": "Decay",
            "type": "Element",
            "required": True,
        },
    )


class DeleteSkeletonOnDecay(Enum):
    FALSE = "false"
    TRUE = "true"


class DeployType(Enum):
    NONE = "None"
    NUCLEAR_BOMB = "NuclearBomb"


@dataclass
class DepositMaterialGasData:
    weight: Optional[float] = field(
        default=None,
        metadata={
            "name": "Weight",
            "type": "Attribute",
            "required": True,
        },
    )
    temperature_c: Optional[float] = field(
        default=None,
        metadata={
            "name": "TemperatureC",
            "type": "Attribute",
            "required": True,
        },
    )
    temperature_k: Optional[float] = field(
        default=None,
        metadata={
            "name": "TemperatureK",
            "type": "Attribute",
            "required": True,
        },
    )
    oxygen: Optional[float] = field(
        default=None,
        metadata={
            "name": "Oxygen",
            "type": "Attribute",
            "required": True,
        },
    )
    nitrogen: Optional[float] = field(
        default=None,
        metadata={
            "name": "Nitrogen",
            "type": "Attribute",
            "required": True,
        },
    )
    carbon_dioxide: Optional[float] = field(
        default=None,
        metadata={
            "name": "CarbonDioxide",
            "type": "Attribute",
            "required": True,
        },
    )
    volatiles: Optional[float] = field(
        default=None,
        metadata={
            "name": "Volatiles",
            "type": "Attribute",
            "required": True,
        },
    )
    pollutant: Optional[float] = field(
        default=None,
        metadata={
            "name": "Pollutant",
            "type": "Attribute",
            "required": True,
        },
    )
    water: Optional[float] = field(
        default=None,
        metadata={
            "name": "Water",
            "type": "Attribute",
            "required": True,
        },
    )
    polluted_water: Optional[float] = field(
        default=None,
        metadata={
            "name": "PollutedWater",
            "type": "Attribute",
            "required": True,
        },
    )
    nitrous_oxide: Optional[float] = field(
        default=None,
        metadata={
            "name": "NitrousOxide",
            "type": "Attribute",
            "required": True,
        },
    )
    liquid_nitrogen: Optional[float] = field(
        default=None,
        metadata={
            "name": "LiquidNitrogen",
            "type": "Attribute",
            "required": True,
        },
    )
    liquid_oxygen: Optional[float] = field(
        default=None,
        metadata={
            "name": "LiquidOxygen",
            "type": "Attribute",
            "required": True,
        },
    )
    liquid_volatiles: Optional[float] = field(
        default=None,
        metadata={
            "name": "LiquidVolatiles",
            "type": "Attribute",
            "required": True,
        },
    )
    steam: Optional[float] = field(
        default=None,
        metadata={
            "name": "Steam",
            "type": "Attribute",
            "required": True,
        },
    )
    liquid_carbon_dioxide: Optional[float] = field(
        default=None,
        metadata={
            "name": "LiquidCarbonDioxide",
            "type": "Attribute",
            "required": True,
        },
    )
    liquid_pollutant: Optional[float] = field(
        default=None,
        metadata={
            "name": "LiquidPollutant",
            "type": "Attribute",
            "required": True,
        },
    )
    liquid_nitrous_oxide: Optional[float] = field(
        default=None,
        metadata={
            "name": "LiquidNitrousOxide",
            "type": "Attribute",
            "required": True,
        },
    )
    hydrogen: Optional[float] = field(
        default=None,
        metadata={
            "name": "Hydrogen",
            "type": "Attribute",
            "required": True,
        },
    )
    liquid_hydrogen: Optional[float] = field(
        default=None,
        metadata={
            "name": "LiquidHydrogen",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class DepositMaterialOreData:
    weight: Optional[float] = field(
        default=None,
        metadata={
            "name": "Weight",
            "type": "Attribute",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass
class DoubleReference:
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class DynamicPanelData:
    orientation: Optional[int] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Attribute",
            "required": True,
        },
    )
    offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Attribute",
            "required": True,
        },
    )
    extra_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "ExtraSize",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class DynamicThingData:
    custom_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomName",
            "type": "Element",
        },
    )
    prefab_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrefabName",
            "type": "Element",
        },
    )
    use_master_color: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseMasterColor",
            "type": "Element",
            "required": True,
        },
    )
    custom_color: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomColor",
            "type": "Element",
        },
    )
    contents: Optional[ArrayOfInventoryData] = field(
        default=None,
        metadata={
            "name": "Contents",
            "type": "Element",
        },
    )


@dataclass
class EdgeData:
    x1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    y1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    z1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    x2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    y2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    z2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


class EntityState(Enum):
    ALIVE = "Alive"
    DEAD = "Dead"
    UNCONSCIOUS = "Unconscious"
    DECAY = "Decay"


class EntitySurvivalProperty(Enum):
    NONE = "None"
    OXYGEN_QUALITY = "OxygenQuality"
    NUTRITION = "Nutrition"
    HYDRATION = "Hydration"
    MOOD = "Mood"
    HYGIENE = "Hygiene"
    FOOD_QUALITY = "FoodQuality"
    HEALTH = "Health"


@dataclass
class FabricatorJob:
    prefab_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrefabName",
            "type": "Attribute",
        },
    )
    quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Float3:
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    y: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    z: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class FloatRangeData:
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )
    min: Optional[float] = field(
        default=None,
        metadata={
            "name": "Min",
            "type": "Attribute",
            "required": True,
        },
    )
    max: Optional[float] = field(
        default=None,
        metadata={
            "name": "Max",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class FloatReference:
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class GasTradeData:
    gas_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "GasName",
            "type": "Element",
        },
    )
    trade_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "TradeValue",
            "type": "Element",
            "required": True,
        },
    )


class GasTypeValue(Enum):
    UNDEFINED = "Undefined"
    OXYGEN = "Oxygen"
    NITROGEN = "Nitrogen"
    CARBON_DIOXIDE = "CarbonDioxide"
    VOLATILES = "Volatiles"
    POLLUTANT = "Pollutant"
    WATER = "Water"
    NITROUS_OXIDE = "NitrousOxide"
    LIQUID_NITROGEN = "LiquidNitrogen"
    LIQUID_OXYGEN = "LiquidOxygen"
    LIQUID_VOLATILES = "LiquidVolatiles"
    STEAM = "Steam"
    LIQUID_CARBON_DIOXIDE = "LiquidCarbonDioxide"
    LIQUID_POLLUTANT = "LiquidPollutant"
    LIQUID_NITROUS_OXIDE = "LiquidNitrousOxide"
    HYDROGEN = "Hydrogen"
    LIQUID_HYDROGEN = "LiquidHydrogen"
    POLLUTED_WATER = "PollutedWater"
    AIR = "Air"
    FUEL = "Fuel"


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"


@dataclass
class GeneWrapper:
    gene: Optional[Gene] = field(
        default=None,
        metadata={
            "name": "Gene",
            "type": "Element",
            "nillable": True,
        },
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    stability: Optional[float] = field(
        default=None,
        metadata={
            "name": "Stability",
            "type": "Element",
            "required": True,
        },
    )


class Gene1(Enum):
    NONE = "None"
    GROWTH_TIME_MULTIPLIER = "GrowthTimeMultiplier"
    DARK_PER_DAY = "DarkPerDay"
    LIGHT_PER_DAY = "LightPerDay"
    DROUGHT_TOLERANCE = "DroughtTolerance"
    WATER_USAGE = "WaterUsage"
    LOW_PRESSURE_RESISTANCE = "LowPressureResistance"
    LOW_TEMPERATURE_RESISTANCE = "LowTemperatureResistance"
    UNDESIRED_GAS_TOLERANCE = "UndesiredGasTolerance"
    GAS_PRODUCTION = "GasProduction"
    HIGH_PRESSURE_RESISTANCE = "HighPressureResistance"
    HIGH_TEMPERATURE_RESISTANCE = "HighTemperatureResistance"
    SUFFOCATION_TOLERANCE = "SuffocationTolerance"
    LOW_PRESSURE_TOLERANCE = "LowPressureTolerance"
    LOW_TEMPERATURE_TOLERANCE = "LowTemperatureTolerance"
    HIGH_PRESSURE_TOLERANCE = "HighPressureTolerance"
    HIGH_TEMPERATURE_TOLERANCE = "HighTemperatureTolerance"
    UNDESIRED_GAS_RESISTANCE = "UndesiredGasResistance"
    LIGHT_TOLERANCE = "LightTolerance"
    DARKNESS_TOLERANCE = "DarknessTolerance"


@dataclass
class GlobalTemperatureOffsetData:
    pass


@dataclass
class GradientAlphaKey:
    alpha: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    time: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


class GradientMode(Enum):
    BLEND = "Blend"
    FIXED = "Fixed"
    PERCEPTUAL_BLEND = "PerceptualBlend"


@dataclass
class Grid3:
    x: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    y: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    z: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


class HideFlagsValue(Enum):
    NONE = "None"
    HIDE_IN_HIERARCHY = "HideInHierarchy"
    HIDE_IN_INSPECTOR = "HideInInspector"
    DONT_SAVE_IN_EDITOR = "DontSaveInEditor"
    NOT_EDITABLE = "NotEditable"
    DONT_SAVE_IN_BUILD = "DontSaveInBuild"
    DONT_UNLOAD_UNUSED_ASSET = "DontUnloadUnusedAsset"
    DONT_SAVE = "DontSave"
    HIDE_AND_DONT_SAVE = "HideAndDontSave"


@dataclass
class InstructionData:
    date_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "DateTime",
            "type": "Element",
            "required": True,
        },
    )
    game_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "GameVersion",
            "type": "Element",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
        },
    )
    author: Optional[str] = field(
        default=None,
        metadata={
            "name": "Author",
            "type": "Element",
        },
    )
    workshop_file_handle: Optional[int] = field(
        default=None,
        metadata={
            "name": "WorkshopFileHandle",
            "type": "Element",
            "required": True,
        },
    )
    instructions: Optional[str] = field(
        default=None,
        metadata={
            "name": "Instructions",
            "type": "Element",
        },
    )


@dataclass
class IntRangeData:
    value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )
    min: Optional[int] = field(
        default=None,
        metadata={
            "name": "Min",
            "type": "Attribute",
            "required": True,
        },
    )
    max: Optional[int] = field(
        default=None,
        metadata={
            "name": "Max",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class IntReference:
    value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class InteractableState:
    state_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "StateName",
            "type": "Element",
        },
    )
    state: Optional[int] = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Element",
            "required": True,
        },
    )


class InteractableType(Enum):
    OPEN = "Open"
    SLOT1 = "Slot1"
    SLOT2 = "Slot2"
    SLOT3 = "Slot3"
    SLOT4 = "Slot4"
    SLOT5 = "Slot5"
    SLOT6 = "Slot6"
    SLOT7 = "Slot7"
    SLOT8 = "Slot8"
    SLOT9 = "Slot9"
    SLOT10 = "Slot10"
    SLOT11 = "Slot11"
    SLOT12 = "Slot12"
    SLOT13 = "Slot13"
    SLOT14 = "Slot14"
    SLOT15 = "Slot15"
    SLOT16 = "Slot16"
    SLOT17 = "Slot17"
    SLOT18 = "Slot18"
    SLOT19 = "Slot19"
    SLOT20 = "Slot20"
    SLOT21 = "Slot21"
    SLOT22 = "Slot22"
    SLOT23 = "Slot23"
    SLOT24 = "Slot24"
    SLOT25 = "Slot25"
    SLOT26 = "Slot26"
    SLOT27 = "Slot27"
    SLOT28 = "Slot28"
    SLOT29 = "Slot29"
    SLOT30 = "Slot30"
    BUTTON1 = "Button1"
    BUTTON2 = "Button2"
    BUTTON3 = "Button3"
    BUTTON4 = "Button4"
    BUTTON5 = "Button5"
    ON_OFF = "OnOff"
    MODE = "Mode"
    LOCK = "Lock"
    IMPORT = "Import"
    EXPORT = "Export"
    ACTIVATE = "Activate"
    POWERED = "Powered"
    ERROR = "Error"
    EXPORT2 = "Export2"
    COLOR = "Color"
    ACCESS = "Access"
    SLOT31 = "Slot31"
    SLOT32 = "Slot32"
    SLOT33 = "Slot33"
    SLOT34 = "Slot34"
    SLOT35 = "Slot35"
    SLOT36 = "Slot36"
    SLOT37 = "Slot37"
    SLOT38 = "Slot38"
    SLOT39 = "Slot39"
    SLOT40 = "Slot40"
    SLOT41 = "Slot41"
    SLOT42 = "Slot42"
    SLOT43 = "Slot43"
    SLOT44 = "Slot44"
    SLOT45 = "Slot45"
    SLOT46 = "Slot46"
    SLOT47 = "Slot47"
    SLOT48 = "Slot48"
    SLOT49 = "Slot49"
    SLOT50 = "Slot50"
    SLOT51 = "Slot51"
    SLOT52 = "Slot52"
    SLOT53 = "Slot53"
    SLOT54 = "Slot54"
    SLOT55 = "Slot55"
    SLOT56 = "Slot56"
    SLOT57 = "Slot57"
    SLOT58 = "Slot58"
    SLOT59 = "Slot59"
    SLOT60 = "Slot60"
    SLOT61 = "Slot61"
    SLOT62 = "Slot62"
    SLOT63 = "Slot63"
    SLOT64 = "Slot64"
    SLOT65 = "Slot65"
    SLOT66 = "Slot66"
    SLOT67 = "Slot67"
    SLOT68 = "Slot68"
    SLOT69 = "Slot69"
    SLOT70 = "Slot70"
    SLOT71 = "Slot71"
    SLOT72 = "Slot72"
    SLOT73 = "Slot73"
    SLOT74 = "Slot74"
    SLOT75 = "Slot75"
    SLOT76 = "Slot76"
    SLOT77 = "Slot77"
    SLOT78 = "Slot78"
    SLOT79 = "Slot79"
    SLOT80 = "Slot80"
    SLOT81 = "Slot81"
    SLOT82 = "Slot82"
    SLOT83 = "Slot83"
    SLOT84 = "Slot84"
    SLOT85 = "Slot85"
    SLOT86 = "Slot86"
    SLOT87 = "Slot87"
    SLOT88 = "Slot88"
    SLOT89 = "Slot89"
    SLOT90 = "Slot90"
    SLOT91 = "Slot91"
    SLOT92 = "Slot92"
    SLOT93 = "Slot93"
    SLOT94 = "Slot94"
    SLOT95 = "Slot95"
    SLOT96 = "Slot96"
    SLOT97 = "Slot97"
    SLOT98 = "Slot98"
    SLOT99 = "Slot99"
    SLOT100 = "Slot100"
    SLOT101 = "Slot101"
    SLOT102 = "Slot102"
    SLOT103 = "Slot103"
    SLOT104 = "Slot104"
    SLOT105 = "Slot105"
    SLOT106 = "Slot106"
    SLOT107 = "Slot107"
    SLOT108 = "Slot108"
    SLOT109 = "Slot109"
    BUTTON6 = "Button6"
    BUTTON7 = "Button7"
    BUTTON8 = "Button8"
    BUTTON9 = "Button9"
    BUTTON10 = "Button10"
    BUTTON11 = "Button11"
    BUTTON12 = "Button12"
    BUTTON13 = "Button13"
    BUTTON14 = "Button14"
    BUTTON15 = "Button15"
    BUTTON16 = "Button16"
    BUTTON17 = "Button17"
    IMPORT2 = "Import2"


class KeyCode(Enum):
    NONE = "None"
    BACKSPACE = "Backspace"
    DELETE = "Delete"
    TAB = "Tab"
    CLEAR = "Clear"
    RETURN = "Return"
    PAUSE = "Pause"
    ESCAPE = "Escape"
    SPACE = "Space"
    KEYPAD0 = "Keypad0"
    KEYPAD1 = "Keypad1"
    KEYPAD2 = "Keypad2"
    KEYPAD3 = "Keypad3"
    KEYPAD4 = "Keypad4"
    KEYPAD5 = "Keypad5"
    KEYPAD6 = "Keypad6"
    KEYPAD7 = "Keypad7"
    KEYPAD8 = "Keypad8"
    KEYPAD9 = "Keypad9"
    KEYPAD_PERIOD = "KeypadPeriod"
    KEYPAD_DIVIDE = "KeypadDivide"
    KEYPAD_MULTIPLY = "KeypadMultiply"
    KEYPAD_MINUS = "KeypadMinus"
    KEYPAD_PLUS = "KeypadPlus"
    KEYPAD_ENTER = "KeypadEnter"
    KEYPAD_EQUALS = "KeypadEquals"
    UP_ARROW = "UpArrow"
    DOWN_ARROW = "DownArrow"
    RIGHT_ARROW = "RightArrow"
    LEFT_ARROW = "LeftArrow"
    INSERT = "Insert"
    HOME = "Home"
    END = "End"
    PAGE_UP = "PageUp"
    PAGE_DOWN = "PageDown"
    F1 = "F1"
    F2 = "F2"
    F3 = "F3"
    F4 = "F4"
    F5 = "F5"
    F6 = "F6"
    F7 = "F7"
    F8 = "F8"
    F9 = "F9"
    F10 = "F10"
    F11 = "F11"
    F12 = "F12"
    F13 = "F13"
    F14 = "F14"
    F15 = "F15"
    ALPHA0 = "Alpha0"
    ALPHA1 = "Alpha1"
    ALPHA2 = "Alpha2"
    ALPHA3 = "Alpha3"
    ALPHA4 = "Alpha4"
    ALPHA5 = "Alpha5"
    ALPHA6 = "Alpha6"
    ALPHA7 = "Alpha7"
    ALPHA8 = "Alpha8"
    ALPHA9 = "Alpha9"
    EXCLAIM = "Exclaim"
    DOUBLE_QUOTE = "DoubleQuote"
    HASH = "Hash"
    DOLLAR = "Dollar"
    PERCENT = "Percent"
    AMPERSAND = "Ampersand"
    QUOTE = "Quote"
    LEFT_PAREN = "LeftParen"
    RIGHT_PAREN = "RightParen"
    ASTERISK = "Asterisk"
    PLUS = "Plus"
    COMMA = "Comma"
    MINUS = "Minus"
    PERIOD = "Period"
    SLASH = "Slash"
    COLON = "Colon"
    SEMICOLON = "Semicolon"
    LESS = "Less"
    EQUALS = "Equals"
    GREATER = "Greater"
    QUESTION = "Question"
    AT = "At"
    LEFT_BRACKET = "LeftBracket"
    BACKSLASH = "Backslash"
    RIGHT_BRACKET = "RightBracket"
    CARET = "Caret"
    UNDERSCORE = "Underscore"
    BACK_QUOTE = "BackQuote"
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    H = "H"
    I = "I"
    J = "J"
    K = "K"
    L = "L"
    M = "M"
    N = "N"
    O = "O"
    P = "P"
    Q = "Q"
    R = "R"
    S = "S"
    T = "T"
    U = "U"
    V = "V"
    W = "W"
    X = "X"
    Y = "Y"
    Z = "Z"
    LEFT_CURLY_BRACKET = "LeftCurlyBracket"
    PIPE = "Pipe"
    RIGHT_CURLY_BRACKET = "RightCurlyBracket"
    TILDE = "Tilde"
    NUMLOCK = "Numlock"
    CAPS_LOCK = "CapsLock"
    SCROLL_LOCK = "ScrollLock"
    RIGHT_SHIFT = "RightShift"
    LEFT_SHIFT = "LeftShift"
    RIGHT_CONTROL = "RightControl"
    LEFT_CONTROL = "LeftControl"
    RIGHT_ALT = "RightAlt"
    LEFT_ALT = "LeftAlt"
    LEFT_META = "LeftMeta"
    LEFT_COMMAND = "LeftCommand"
    LEFT_APPLE = "LeftApple"
    LEFT_WINDOWS = "LeftWindows"
    RIGHT_META = "RightMeta"
    RIGHT_COMMAND = "RightCommand"
    RIGHT_APPLE = "RightApple"
    RIGHT_WINDOWS = "RightWindows"
    ALT_GR = "AltGr"
    HELP = "Help"
    PRINT = "Print"
    SYS_REQ = "SysReq"
    BREAK = "Break"
    MENU = "Menu"
    MOUSE0 = "Mouse0"
    MOUSE1 = "Mouse1"
    MOUSE2 = "Mouse2"
    MOUSE3 = "Mouse3"
    MOUSE4 = "Mouse4"
    MOUSE5 = "Mouse5"
    MOUSE6 = "Mouse6"
    JOYSTICK_BUTTON0 = "JoystickButton0"
    JOYSTICK_BUTTON1 = "JoystickButton1"
    JOYSTICK_BUTTON2 = "JoystickButton2"
    JOYSTICK_BUTTON3 = "JoystickButton3"
    JOYSTICK_BUTTON4 = "JoystickButton4"
    JOYSTICK_BUTTON5 = "JoystickButton5"
    JOYSTICK_BUTTON6 = "JoystickButton6"
    JOYSTICK_BUTTON7 = "JoystickButton7"
    JOYSTICK_BUTTON8 = "JoystickButton8"
    JOYSTICK_BUTTON9 = "JoystickButton9"
    JOYSTICK_BUTTON10 = "JoystickButton10"
    JOYSTICK_BUTTON11 = "JoystickButton11"
    JOYSTICK_BUTTON12 = "JoystickButton12"
    JOYSTICK_BUTTON13 = "JoystickButton13"
    JOYSTICK_BUTTON14 = "JoystickButton14"
    JOYSTICK_BUTTON15 = "JoystickButton15"
    JOYSTICK_BUTTON16 = "JoystickButton16"
    JOYSTICK_BUTTON17 = "JoystickButton17"
    JOYSTICK_BUTTON18 = "JoystickButton18"
    JOYSTICK_BUTTON19 = "JoystickButton19"
    JOYSTICK1_BUTTON0 = "Joystick1Button0"
    JOYSTICK1_BUTTON1 = "Joystick1Button1"
    JOYSTICK1_BUTTON2 = "Joystick1Button2"
    JOYSTICK1_BUTTON3 = "Joystick1Button3"
    JOYSTICK1_BUTTON4 = "Joystick1Button4"
    JOYSTICK1_BUTTON5 = "Joystick1Button5"
    JOYSTICK1_BUTTON6 = "Joystick1Button6"
    JOYSTICK1_BUTTON7 = "Joystick1Button7"
    JOYSTICK1_BUTTON8 = "Joystick1Button8"
    JOYSTICK1_BUTTON9 = "Joystick1Button9"
    JOYSTICK1_BUTTON10 = "Joystick1Button10"
    JOYSTICK1_BUTTON11 = "Joystick1Button11"
    JOYSTICK1_BUTTON12 = "Joystick1Button12"
    JOYSTICK1_BUTTON13 = "Joystick1Button13"
    JOYSTICK1_BUTTON14 = "Joystick1Button14"
    JOYSTICK1_BUTTON15 = "Joystick1Button15"
    JOYSTICK1_BUTTON16 = "Joystick1Button16"
    JOYSTICK1_BUTTON17 = "Joystick1Button17"
    JOYSTICK1_BUTTON18 = "Joystick1Button18"
    JOYSTICK1_BUTTON19 = "Joystick1Button19"
    JOYSTICK2_BUTTON0 = "Joystick2Button0"
    JOYSTICK2_BUTTON1 = "Joystick2Button1"
    JOYSTICK2_BUTTON2 = "Joystick2Button2"
    JOYSTICK2_BUTTON3 = "Joystick2Button3"
    JOYSTICK2_BUTTON4 = "Joystick2Button4"
    JOYSTICK2_BUTTON5 = "Joystick2Button5"
    JOYSTICK2_BUTTON6 = "Joystick2Button6"
    JOYSTICK2_BUTTON7 = "Joystick2Button7"
    JOYSTICK2_BUTTON8 = "Joystick2Button8"
    JOYSTICK2_BUTTON9 = "Joystick2Button9"
    JOYSTICK2_BUTTON10 = "Joystick2Button10"
    JOYSTICK2_BUTTON11 = "Joystick2Button11"
    JOYSTICK2_BUTTON12 = "Joystick2Button12"
    JOYSTICK2_BUTTON13 = "Joystick2Button13"
    JOYSTICK2_BUTTON14 = "Joystick2Button14"
    JOYSTICK2_BUTTON15 = "Joystick2Button15"
    JOYSTICK2_BUTTON16 = "Joystick2Button16"
    JOYSTICK2_BUTTON17 = "Joystick2Button17"
    JOYSTICK2_BUTTON18 = "Joystick2Button18"
    JOYSTICK2_BUTTON19 = "Joystick2Button19"
    JOYSTICK3_BUTTON0 = "Joystick3Button0"
    JOYSTICK3_BUTTON1 = "Joystick3Button1"
    JOYSTICK3_BUTTON2 = "Joystick3Button2"
    JOYSTICK3_BUTTON3 = "Joystick3Button3"
    JOYSTICK3_BUTTON4 = "Joystick3Button4"
    JOYSTICK3_BUTTON5 = "Joystick3Button5"
    JOYSTICK3_BUTTON6 = "Joystick3Button6"
    JOYSTICK3_BUTTON7 = "Joystick3Button7"
    JOYSTICK3_BUTTON8 = "Joystick3Button8"
    JOYSTICK3_BUTTON9 = "Joystick3Button9"
    JOYSTICK3_BUTTON10 = "Joystick3Button10"
    JOYSTICK3_BUTTON11 = "Joystick3Button11"
    JOYSTICK3_BUTTON12 = "Joystick3Button12"
    JOYSTICK3_BUTTON13 = "Joystick3Button13"
    JOYSTICK3_BUTTON14 = "Joystick3Button14"
    JOYSTICK3_BUTTON15 = "Joystick3Button15"
    JOYSTICK3_BUTTON16 = "Joystick3Button16"
    JOYSTICK3_BUTTON17 = "Joystick3Button17"
    JOYSTICK3_BUTTON18 = "Joystick3Button18"
    JOYSTICK3_BUTTON19 = "Joystick3Button19"
    JOYSTICK4_BUTTON0 = "Joystick4Button0"
    JOYSTICK4_BUTTON1 = "Joystick4Button1"
    JOYSTICK4_BUTTON2 = "Joystick4Button2"
    JOYSTICK4_BUTTON3 = "Joystick4Button3"
    JOYSTICK4_BUTTON4 = "Joystick4Button4"
    JOYSTICK4_BUTTON5 = "Joystick4Button5"
    JOYSTICK4_BUTTON6 = "Joystick4Button6"
    JOYSTICK4_BUTTON7 = "Joystick4Button7"
    JOYSTICK4_BUTTON8 = "Joystick4Button8"
    JOYSTICK4_BUTTON9 = "Joystick4Button9"
    JOYSTICK4_BUTTON10 = "Joystick4Button10"
    JOYSTICK4_BUTTON11 = "Joystick4Button11"
    JOYSTICK4_BUTTON12 = "Joystick4Button12"
    JOYSTICK4_BUTTON13 = "Joystick4Button13"
    JOYSTICK4_BUTTON14 = "Joystick4Button14"
    JOYSTICK4_BUTTON15 = "Joystick4Button15"
    JOYSTICK4_BUTTON16 = "Joystick4Button16"
    JOYSTICK4_BUTTON17 = "Joystick4Button17"
    JOYSTICK4_BUTTON18 = "Joystick4Button18"
    JOYSTICK4_BUTTON19 = "Joystick4Button19"
    JOYSTICK5_BUTTON0 = "Joystick5Button0"
    JOYSTICK5_BUTTON1 = "Joystick5Button1"
    JOYSTICK5_BUTTON2 = "Joystick5Button2"
    JOYSTICK5_BUTTON3 = "Joystick5Button3"
    JOYSTICK5_BUTTON4 = "Joystick5Button4"
    JOYSTICK5_BUTTON5 = "Joystick5Button5"
    JOYSTICK5_BUTTON6 = "Joystick5Button6"
    JOYSTICK5_BUTTON7 = "Joystick5Button7"
    JOYSTICK5_BUTTON8 = "Joystick5Button8"
    JOYSTICK5_BUTTON9 = "Joystick5Button9"
    JOYSTICK5_BUTTON10 = "Joystick5Button10"
    JOYSTICK5_BUTTON11 = "Joystick5Button11"
    JOYSTICK5_BUTTON12 = "Joystick5Button12"
    JOYSTICK5_BUTTON13 = "Joystick5Button13"
    JOYSTICK5_BUTTON14 = "Joystick5Button14"
    JOYSTICK5_BUTTON15 = "Joystick5Button15"
    JOYSTICK5_BUTTON16 = "Joystick5Button16"
    JOYSTICK5_BUTTON17 = "Joystick5Button17"
    JOYSTICK5_BUTTON18 = "Joystick5Button18"
    JOYSTICK5_BUTTON19 = "Joystick5Button19"
    JOYSTICK6_BUTTON0 = "Joystick6Button0"
    JOYSTICK6_BUTTON1 = "Joystick6Button1"
    JOYSTICK6_BUTTON2 = "Joystick6Button2"
    JOYSTICK6_BUTTON3 = "Joystick6Button3"
    JOYSTICK6_BUTTON4 = "Joystick6Button4"
    JOYSTICK6_BUTTON5 = "Joystick6Button5"
    JOYSTICK6_BUTTON6 = "Joystick6Button6"
    JOYSTICK6_BUTTON7 = "Joystick6Button7"
    JOYSTICK6_BUTTON8 = "Joystick6Button8"
    JOYSTICK6_BUTTON9 = "Joystick6Button9"
    JOYSTICK6_BUTTON10 = "Joystick6Button10"
    JOYSTICK6_BUTTON11 = "Joystick6Button11"
    JOYSTICK6_BUTTON12 = "Joystick6Button12"
    JOYSTICK6_BUTTON13 = "Joystick6Button13"
    JOYSTICK6_BUTTON14 = "Joystick6Button14"
    JOYSTICK6_BUTTON15 = "Joystick6Button15"
    JOYSTICK6_BUTTON16 = "Joystick6Button16"
    JOYSTICK6_BUTTON17 = "Joystick6Button17"
    JOYSTICK6_BUTTON18 = "Joystick6Button18"
    JOYSTICK6_BUTTON19 = "Joystick6Button19"
    JOYSTICK7_BUTTON0 = "Joystick7Button0"
    JOYSTICK7_BUTTON1 = "Joystick7Button1"
    JOYSTICK7_BUTTON2 = "Joystick7Button2"
    JOYSTICK7_BUTTON3 = "Joystick7Button3"
    JOYSTICK7_BUTTON4 = "Joystick7Button4"
    JOYSTICK7_BUTTON5 = "Joystick7Button5"
    JOYSTICK7_BUTTON6 = "Joystick7Button6"
    JOYSTICK7_BUTTON7 = "Joystick7Button7"
    JOYSTICK7_BUTTON8 = "Joystick7Button8"
    JOYSTICK7_BUTTON9 = "Joystick7Button9"
    JOYSTICK7_BUTTON10 = "Joystick7Button10"
    JOYSTICK7_BUTTON11 = "Joystick7Button11"
    JOYSTICK7_BUTTON12 = "Joystick7Button12"
    JOYSTICK7_BUTTON13 = "Joystick7Button13"
    JOYSTICK7_BUTTON14 = "Joystick7Button14"
    JOYSTICK7_BUTTON15 = "Joystick7Button15"
    JOYSTICK7_BUTTON16 = "Joystick7Button16"
    JOYSTICK7_BUTTON17 = "Joystick7Button17"
    JOYSTICK7_BUTTON18 = "Joystick7Button18"
    JOYSTICK7_BUTTON19 = "Joystick7Button19"
    JOYSTICK8_BUTTON0 = "Joystick8Button0"
    JOYSTICK8_BUTTON1 = "Joystick8Button1"
    JOYSTICK8_BUTTON2 = "Joystick8Button2"
    JOYSTICK8_BUTTON3 = "Joystick8Button3"
    JOYSTICK8_BUTTON4 = "Joystick8Button4"
    JOYSTICK8_BUTTON5 = "Joystick8Button5"
    JOYSTICK8_BUTTON6 = "Joystick8Button6"
    JOYSTICK8_BUTTON7 = "Joystick8Button7"
    JOYSTICK8_BUTTON8 = "Joystick8Button8"
    JOYSTICK8_BUTTON9 = "Joystick8Button9"
    JOYSTICK8_BUTTON10 = "Joystick8Button10"
    JOYSTICK8_BUTTON11 = "Joystick8Button11"
    JOYSTICK8_BUTTON12 = "Joystick8Button12"
    JOYSTICK8_BUTTON13 = "Joystick8Button13"
    JOYSTICK8_BUTTON14 = "Joystick8Button14"
    JOYSTICK8_BUTTON15 = "Joystick8Button15"
    JOYSTICK8_BUTTON16 = "Joystick8Button16"
    JOYSTICK8_BUTTON17 = "Joystick8Button17"
    JOYSTICK8_BUTTON18 = "Joystick8Button18"
    JOYSTICK8_BUTTON19 = "Joystick8Button19"


class LanguageCode(Enum):
    N = "N"
    AA = "AA"
    AB = "AB"
    AF = "AF"
    AM = "AM"
    AR = "AR"
    AR_SA = "AR_SA"
    AR_EG = "AR_EG"
    AR_DZ = "AR_DZ"
    AR_YE = "AR_YE"
    AR_JO = "AR_JO"
    AR_KW = "AR_KW"
    AR_BH = "AR_BH"
    AR_IQ = "AR_IQ"
    AR_MA = "AR_MA"
    AR_LY = "AR_LY"
    AR_OM = "AR_OM"
    AR_SY = "AR_SY"
    AR_LB = "AR_LB"
    AR_AE = "AR_AE"
    AR_QA = "AR_QA"
    AS = "AS"
    AY = "AY"
    AZ = "AZ"
    BA = "BA"
    BE = "BE"
    BG = "BG"
    BH = "BH"
    BI = "BI"
    BN = "BN"
    BO = "BO"
    BR = "BR"
    CN = "CN"
    CA = "CA"
    CO = "CO"
    CS = "CS"
    CY = "CY"
    DA = "DA"
    DE = "DE"
    DE_AT = "DE_AT"
    DE_LI = "DE_LI"
    DE_CH = "DE_CH"
    DE_LU = "DE_LU"
    DZ = "DZ"
    EL = "EL"
    EN = "EN"
    EN_US = "EN_US"
    EN_AU = "EN_AU"
    EN_NZ = "EN_NZ"
    EN_ZA = "EN_ZA"
    EN_CB = "EN_CB"
    EN_TT = "EN_TT"
    EN_GB = "EN_GB"
    EN_CA = "EN_CA"
    EN_IE = "EN_IE"
    EN_JM = "EN_JM"
    EN_BZ = "EN_BZ"
    EO = "EO"
    ES = "ES"
    ES_MX = "ES_MX"
    ES_CR = "ES_CR"
    ES_DO = "ES_DO"
    ES_CO = "ES_CO"
    ES_AR = "ES_AR"
    ES_CL = "ES_CL"
    ES_PY = "ES_PY"
    ES_SV = "ES_SV"
    ES_NI = "ES_NI"
    ES_GT = "ES_GT"
    ES_PA = "ES_PA"
    ES_VE = "ES_VE"
    ES_PE = "ES_PE"
    ES_EC = "ES_EC"
    ES_UY = "ES_UY"
    ES_BO = "ES_BO"
    ES_HN = "ES_HN"
    ES_PR = "ES_PR"
    ET = "ET"
    EU = "EU"
    FA = "FA"
    FI = "FI"
    FJ = "FJ"
    FO = "FO"
    FR = "FR"
    FR_BE = "FR_BE"
    FR_CH = "FR_CH"
    FR_CA = "FR_CA"
    FR_LU = "FR_LU"
    FY = "FY"
    GA = "GA"
    GD = "GD"
    GL = "GL"
    GN = "GN"
    GU = "GU"
    HA = "HA"
    HI = "HI"
    HE = "HE"
    HR = "HR"
    HU = "HU"
    HY = "HY"
    IA = "IA"
    ID = "ID"
    IE = "IE"
    IK = "IK"
    IN = "IN"
    IS = "IS"
    IT = "IT"
    IT_CH = "IT_CH"
    IU = "IU"
    IW = "IW"
    JA = "JA"
    JI = "JI"
    JW = "JW"
    KA = "KA"
    KK = "KK"
    KL = "KL"
    KM = "KM"
    KN = "KN"
    KO = "KO"
    KS = "KS"
    KU = "KU"
    KY = "KY"
    LA = "LA"
    LN = "LN"
    LO = "LO"
    LT = "LT"
    LV = "LV"
    MG = "MG"
    MI = "MI"
    MK = "MK"
    ML = "ML"
    MN = "MN"
    MO = "MO"
    MR = "MR"
    MS = "MS"
    MT = "MT"
    MY = "MY"
    NA = "NA"
    NE = "NE"
    NL = "NL"
    NL_BE = "NL_BE"
    NO = "NO"
    OC = "OC"
    OM = "OM"
    OR = "OR"
    PA = "PA"
    PL = "PL"
    PS = "PS"
    PT = "PT"
    PT_BR = "PT_BR"
    QU = "QU"
    RM = "RM"
    RN = "RN"
    RO = "RO"
    RO_MO = "RO_MO"
    RU = "RU"
    RU_MO = "RU_MO"
    RW = "RW"
    SA = "SA"
    SD = "SD"
    SG = "SG"
    SH = "SH"
    SI = "SI"
    SK = "SK"
    SL = "SL"
    SM = "SM"
    SN = "SN"
    SO = "SO"
    SQ = "SQ"
    SR = "SR"
    SS = "SS"
    ST = "ST"
    SU = "SU"
    SV = "SV"
    SV_FI = "SV_FI"
    SW = "SW"
    TA = "TA"
    TE = "TE"
    TG = "TG"
    TH = "TH"
    TI = "TI"
    TK = "TK"
    TL = "TL"
    TN = "TN"
    TO = "TO"
    TR = "TR"
    TS = "TS"
    TT = "TT"
    TW = "TW"
    UG = "UG"
    UK = "UK"
    UR = "UR"
    UZ = "UZ"
    VI = "VI"
    VO = "VO"
    WO = "WO"
    XH = "XH"
    YI = "YI"
    YO = "YO"
    ZA = "ZA"
    ZH = "ZH"
    ZH_TW = "ZH_TW"
    ZH_HK = "ZH_HK"
    ZH_CN = "ZH_CN"
    ZH_SG = "ZH_SG"
    ZU = "ZU"
    PB = "PB"


class LogicBatchMethod(Enum):
    AVERAGE = "Average"
    SUM = "Sum"
    MINIMUM = "Minimum"
    MAXIMUM = "Maximum"


class LogicOperator(Enum):
    ALL = "All"
    ANY = "Any"
    NONE = "None"


class LogicType(Enum):
    NONE = "None"
    POWER = "Power"
    OPEN = "Open"
    MODE = "Mode"
    ERROR = "Error"
    PRESSURE = "Pressure"
    TEMPERATURE = "Temperature"
    PRESSURE_EXTERNAL = "PressureExternal"
    PRESSURE_INTERNAL = "PressureInternal"
    ACTIVATE = "Activate"
    LOCK = "Lock"
    CHARGE = "Charge"
    SETTING = "Setting"
    REAGENTS = "Reagents"
    RATIO_OXYGEN = "RatioOxygen"
    RATIO_CARBON_DIOXIDE = "RatioCarbonDioxide"
    RATIO_NITROGEN = "RatioNitrogen"
    RATIO_POLLUTANT = "RatioPollutant"
    RATIO_VOLATILES = "RatioVolatiles"
    RATIO_WATER = "RatioWater"
    HORIZONTAL = "Horizontal"
    VERTICAL = "Vertical"
    SOLAR_ANGLE = "SolarAngle"
    MAXIMUM = "Maximum"
    RATIO = "Ratio"
    POWER_POTENTIAL = "PowerPotential"
    POWER_ACTUAL = "PowerActual"
    QUANTITY = "Quantity"
    ON = "On"
    IMPORT_QUANTITY = "ImportQuantity"
    IMPORT_SLOT_OCCUPANT = "ImportSlotOccupant"
    EXPORT_QUANTITY = "ExportQuantity"
    EXPORT_SLOT_OCCUPANT = "ExportSlotOccupant"
    REQUIRED_POWER = "RequiredPower"
    HORIZONTAL_RATIO = "HorizontalRatio"
    VERTICAL_RATIO = "VerticalRatio"
    POWER_REQUIRED = "PowerRequired"
    IDLE = "Idle"
    COLOR = "Color"
    ELEVATOR_SPEED = "ElevatorSpeed"
    ELEVATOR_LEVEL = "ElevatorLevel"
    RECIPE_HASH = "RecipeHash"
    EXPORT_SLOT_HASH = "ExportSlotHash"
    IMPORT_SLOT_HASH = "ImportSlotHash"
    PLANT_HEALTH1 = "PlantHealth1"
    PLANT_HEALTH2 = "PlantHealth2"
    PLANT_HEALTH3 = "PlantHealth3"
    PLANT_HEALTH4 = "PlantHealth4"
    PLANT_GROWTH1 = "PlantGrowth1"
    PLANT_GROWTH2 = "PlantGrowth2"
    PLANT_GROWTH3 = "PlantGrowth3"
    PLANT_GROWTH4 = "PlantGrowth4"
    PLANT_EFFICIENCY1 = "PlantEfficiency1"
    PLANT_EFFICIENCY2 = "PlantEfficiency2"
    PLANT_EFFICIENCY3 = "PlantEfficiency3"
    PLANT_EFFICIENCY4 = "PlantEfficiency4"
    PLANT_HASH1 = "PlantHash1"
    PLANT_HASH2 = "PlantHash2"
    PLANT_HASH3 = "PlantHash3"
    PLANT_HASH4 = "PlantHash4"
    REQUEST_HASH = "RequestHash"
    COMPLETION_RATIO = "CompletionRatio"
    CLEAR_MEMORY = "ClearMemory"
    EXPORT_COUNT = "ExportCount"
    IMPORT_COUNT = "ImportCount"
    POWER_GENERATION = "PowerGeneration"
    TOTAL_MOLES = "TotalMoles"
    VOLUME = "Volume"
    PLANT = "Plant"
    HARVEST = "Harvest"
    OUTPUT = "Output"
    PRESSURE_SETTING = "PressureSetting"
    TEMPERATURE_SETTING = "TemperatureSetting"
    TEMPERATURE_EXTERNAL = "TemperatureExternal"
    FILTRATION = "Filtration"
    AIR_RELEASE = "AirRelease"
    POSITION_X = "PositionX"
    POSITION_Y = "PositionY"
    POSITION_Z = "PositionZ"
    VELOCITY_MAGNITUDE = "VelocityMagnitude"
    VELOCITY_RELATIVE_X = "VelocityRelativeX"
    VELOCITY_RELATIVE_Y = "VelocityRelativeY"
    VELOCITY_RELATIVE_Z = "VelocityRelativeZ"
    RATIO_NITROUS_OXIDE = "RatioNitrousOxide"
    PREFAB_HASH = "PrefabHash"
    FORCE_WRITE = "ForceWrite"
    SIGNAL_STRENGTH = "SignalStrength"
    SIGNAL_ID = "SignalID"
    TARGET_X = "TargetX"
    TARGET_Y = "TargetY"
    TARGET_Z = "TargetZ"
    SETTING_INPUT = "SettingInput"
    SETTING_OUTPUT = "SettingOutput"
    CURRENT_RESEARCH_POD_TYPE = "CurrentResearchPodType"
    MANUAL_RESEARCH_REQUIRED_POD = "ManualResearchRequiredPod"
    MINEABLES_IN_VICINITY = "MineablesInVicinity"
    MINEABLES_IN_QUEUE = "MineablesInQueue"
    NEXT_WEATHER_EVENT_TIME = "NextWeatherEventTime"
    COMBUSTION = "Combustion"
    FUEL = "Fuel"
    RETURN_FUEL_COST = "ReturnFuelCost"
    COLLECTABLE_GOODS = "CollectableGoods"
    TIME = "Time"
    BPM = "Bpm"
    ENVIRONMENT_EFFICIENCY = "EnvironmentEfficiency"
    WORKING_GAS_EFFICIENCY = "WorkingGasEfficiency"
    PRESSURE_INPUT = "PressureInput"
    TEMPERATURE_INPUT = "TemperatureInput"
    RATIO_OXYGEN_INPUT = "RatioOxygenInput"
    RATIO_CARBON_DIOXIDE_INPUT = "RatioCarbonDioxideInput"
    RATIO_NITROGEN_INPUT = "RatioNitrogenInput"
    RATIO_POLLUTANT_INPUT = "RatioPollutantInput"
    RATIO_VOLATILES_INPUT = "RatioVolatilesInput"
    RATIO_WATER_INPUT = "RatioWaterInput"
    RATIO_NITROUS_OXIDE_INPUT = "RatioNitrousOxideInput"
    TOTAL_MOLES_INPUT = "TotalMolesInput"
    PRESSURE_INPUT2 = "PressureInput2"
    TEMPERATURE_INPUT2 = "TemperatureInput2"
    RATIO_OXYGEN_INPUT2 = "RatioOxygenInput2"
    RATIO_CARBON_DIOXIDE_INPUT2 = "RatioCarbonDioxideInput2"
    RATIO_NITROGEN_INPUT2 = "RatioNitrogenInput2"
    RATIO_POLLUTANT_INPUT2 = "RatioPollutantInput2"
    RATIO_VOLATILES_INPUT2 = "RatioVolatilesInput2"
    RATIO_WATER_INPUT2 = "RatioWaterInput2"
    RATIO_NITROUS_OXIDE_INPUT2 = "RatioNitrousOxideInput2"
    TOTAL_MOLES_INPUT2 = "TotalMolesInput2"
    PRESSURE_OUTPUT = "PressureOutput"
    TEMPERATURE_OUTPUT = "TemperatureOutput"
    RATIO_OXYGEN_OUTPUT = "RatioOxygenOutput"
    RATIO_CARBON_DIOXIDE_OUTPUT = "RatioCarbonDioxideOutput"
    RATIO_NITROGEN_OUTPUT = "RatioNitrogenOutput"
    RATIO_POLLUTANT_OUTPUT = "RatioPollutantOutput"
    RATIO_VOLATILES_OUTPUT = "RatioVolatilesOutput"
    RATIO_WATER_OUTPUT = "RatioWaterOutput"
    RATIO_NITROUS_OXIDE_OUTPUT = "RatioNitrousOxideOutput"
    TOTAL_MOLES_OUTPUT = "TotalMolesOutput"
    PRESSURE_OUTPUT2 = "PressureOutput2"
    TEMPERATURE_OUTPUT2 = "TemperatureOutput2"
    RATIO_OXYGEN_OUTPUT2 = "RatioOxygenOutput2"
    RATIO_CARBON_DIOXIDE_OUTPUT2 = "RatioCarbonDioxideOutput2"
    RATIO_NITROGEN_OUTPUT2 = "RatioNitrogenOutput2"
    RATIO_POLLUTANT_OUTPUT2 = "RatioPollutantOutput2"
    RATIO_VOLATILES_OUTPUT2 = "RatioVolatilesOutput2"
    RATIO_WATER_OUTPUT2 = "RatioWaterOutput2"
    RATIO_NITROUS_OXIDE_OUTPUT2 = "RatioNitrousOxideOutput2"
    TOTAL_MOLES_OUTPUT2 = "TotalMolesOutput2"
    COMBUSTION_INPUT = "CombustionInput"
    COMBUSTION_INPUT2 = "CombustionInput2"
    COMBUSTION_OUTPUT = "CombustionOutput"
    COMBUSTION_OUTPUT2 = "CombustionOutput2"
    OPERATIONAL_TEMPERATURE_EFFICIENCY = "OperationalTemperatureEfficiency"
    TEMPERATURE_DIFFERENTIAL_EFFICIENCY = "TemperatureDifferentialEfficiency"
    PRESSURE_EFFICIENCY = "PressureEfficiency"
    COMBUSTION_LIMITER = "CombustionLimiter"
    THROTTLE = "Throttle"
    RPM = "Rpm"
    STRESS = "Stress"
    INTERROGATION_PROGRESS = "InterrogationProgress"
    TARGET_PAD_INDEX = "TargetPadIndex"
    SIZE_X = "SizeX"
    SIZE_Y = "SizeY"
    SIZE_Z = "SizeZ"
    MINIMUM_WATTS_TO_CONTACT = "MinimumWattsToContact"
    WATTS_REACHING_CONTACT = "WattsReachingContact"
    CHANNEL0 = "Channel0"
    CHANNEL1 = "Channel1"
    CHANNEL2 = "Channel2"
    CHANNEL3 = "Channel3"
    CHANNEL4 = "Channel4"
    CHANNEL5 = "Channel5"
    CHANNEL6 = "Channel6"
    CHANNEL7 = "Channel7"
    LINE_NUMBER = "LineNumber"
    FLUSH = "Flush"
    SOUND_ALERT = "SoundAlert"
    SOLAR_IRRADIANCE = "SolarIrradiance"
    RATIO_LIQUID_NITROGEN = "RatioLiquidNitrogen"
    RATIO_LIQUID_NITROGEN_INPUT = "RatioLiquidNitrogenInput"
    RATIO_LIQUID_NITROGEN_INPUT2 = "RatioLiquidNitrogenInput2"
    RATIO_LIQUID_NITROGEN_OUTPUT = "RatioLiquidNitrogenOutput"
    RATIO_LIQUID_NITROGEN_OUTPUT2 = "RatioLiquidNitrogenOutput2"
    VOLUME_OF_LIQUID = "VolumeOfLiquid"
    RATIO_LIQUID_OXYGEN = "RatioLiquidOxygen"
    RATIO_LIQUID_OXYGEN_INPUT = "RatioLiquidOxygenInput"
    RATIO_LIQUID_OXYGEN_INPUT2 = "RatioLiquidOxygenInput2"
    RATIO_LIQUID_OXYGEN_OUTPUT = "RatioLiquidOxygenOutput"
    RATIO_LIQUID_OXYGEN_OUTPUT2 = "RatioLiquidOxygenOutput2"
    RATIO_LIQUID_VOLATILES = "RatioLiquidVolatiles"
    RATIO_LIQUID_VOLATILES_INPUT = "RatioLiquidVolatilesInput"
    RATIO_LIQUID_VOLATILES_INPUT2 = "RatioLiquidVolatilesInput2"
    RATIO_LIQUID_VOLATILES_OUTPUT = "RatioLiquidVolatilesOutput"
    RATIO_LIQUID_VOLATILES_OUTPUT2 = "RatioLiquidVolatilesOutput2"
    RATIO_STEAM = "RatioSteam"
    RATIO_STEAM_INPUT = "RatioSteamInput"
    RATIO_STEAM_INPUT2 = "RatioSteamInput2"
    RATIO_STEAM_OUTPUT = "RatioSteamOutput"
    RATIO_STEAM_OUTPUT2 = "RatioSteamOutput2"
    CONTACT_TYPE_ID = "ContactTypeId"
    RATIO_LIQUID_CARBON_DIOXIDE = "RatioLiquidCarbonDioxide"
    RATIO_LIQUID_CARBON_DIOXIDE_INPUT = "RatioLiquidCarbonDioxideInput"
    RATIO_LIQUID_CARBON_DIOXIDE_INPUT2 = "RatioLiquidCarbonDioxideInput2"
    RATIO_LIQUID_CARBON_DIOXIDE_OUTPUT = "RatioLiquidCarbonDioxideOutput"
    RATIO_LIQUID_CARBON_DIOXIDE_OUTPUT2 = "RatioLiquidCarbonDioxideOutput2"
    RATIO_LIQUID_POLLUTANT = "RatioLiquidPollutant"
    RATIO_LIQUID_POLLUTANT_INPUT = "RatioLiquidPollutantInput"
    RATIO_LIQUID_POLLUTANT_INPUT2 = "RatioLiquidPollutantInput2"
    RATIO_LIQUID_POLLUTANT_OUTPUT = "RatioLiquidPollutantOutput"
    RATIO_LIQUID_POLLUTANT_OUTPUT2 = "RatioLiquidPollutantOutput2"
    RATIO_LIQUID_NITROUS_OXIDE = "RatioLiquidNitrousOxide"
    RATIO_LIQUID_NITROUS_OXIDE_INPUT = "RatioLiquidNitrousOxideInput"
    RATIO_LIQUID_NITROUS_OXIDE_INPUT2 = "RatioLiquidNitrousOxideInput2"
    RATIO_LIQUID_NITROUS_OXIDE_OUTPUT = "RatioLiquidNitrousOxideOutput"
    RATIO_LIQUID_NITROUS_OXIDE_OUTPUT2 = "RatioLiquidNitrousOxideOutput2"
    PROGRESS = "Progress"
    DESTINATION_CODE = "DestinationCode"
    ACCELERATION = "Acceleration"
    REFERENCE_ID = "ReferenceId"
    AUTO_SHUT_OFF = "AutoShutOff"
    MASS = "Mass"
    DRY_MASS = "DryMass"
    THRUST = "Thrust"
    WEIGHT = "Weight"
    THRUST_TO_WEIGHT = "ThrustToWeight"
    TIME_TO_DESTINATION = "TimeToDestination"
    BURN_TIME_REMAINING = "BurnTimeRemaining"
    AUTO_LAND = "AutoLand"
    FORWARD_X = "ForwardX"
    FORWARD_Y = "ForwardY"
    FORWARD_Z = "ForwardZ"
    ORIENTATION = "Orientation"
    VELOCITY_X = "VelocityX"
    VELOCITY_Y = "VelocityY"
    VELOCITY_Z = "VelocityZ"
    PASSED_MOLES = "PassedMoles"
    EXHAUST_VELOCITY = "ExhaustVelocity"
    FLIGHT_CONTROL_RULE = "FlightControlRule"
    RE_ENTRY_ALTITUDE = "ReEntryAltitude"
    APEX = "Apex"
    ENTITY_STATE = "EntityState"
    DRILL_CONDITION = "DrillCondition"
    INDEX = "Index"
    CELESTIAL_HASH = "CelestialHash"
    ALIGNMENT_ERROR = "AlignmentError"
    DISTANCE_AU = "DistanceAu"
    ORBIT_PERIOD = "OrbitPeriod"
    INCLINATION = "Inclination"
    ECCENTRICITY = "Eccentricity"
    SEMI_MAJOR_AXIS = "SemiMajorAxis"
    DISTANCE_KM = "DistanceKm"
    CELESTIAL_PARENT_HASH = "CelestialParentHash"
    TRUE_ANOMALY = "TrueAnomaly"
    RATIO_HYDROGEN = "RatioHydrogen"
    RATIO_LIQUID_HYDROGEN = "RatioLiquidHydrogen"
    RATIO_POLLUTED_WATER = "RatioPollutedWater"
    DISCOVER = "Discover"
    CHART = "Chart"
    SURVEY = "Survey"
    NAV_POINTS = "NavPoints"
    CHARTED_NAV_POINTS = "ChartedNavPoints"
    SITES = "Sites"
    CURRENT_CODE = "CurrentCode"
    DENSITY = "Density"
    RICHNESS = "Richness"
    SIZE = "Size"
    TOTAL_QUANTITY = "TotalQuantity"
    MINED_QUANTITY = "MinedQuantity"
    BEST_CONTACT_FILTER = "BestContactFilter"
    NAME_HASH = "NameHash"
    ALTITUDE = "Altitude"
    TARGET_SLOT_INDEX = "TargetSlotIndex"
    TARGET_PREFAB_HASH = "TargetPrefabHash"
    EXTENDED = "Extended"
    NETWORK_FAULT = "NetworkFault"
    PROPORTIONAL_GAIN = "ProportionalGain"
    INTEGRAL_GAIN = "IntegralGain"
    DERIVATIVE_GAIN = "DerivativeGain"
    MINIMUM = "Minimum"
    SETPOINT = "Setpoint"
    RESET = "Reset"
    STACK_SIZE = "StackSize"
    NEXT_WEATHER_HASH = "NextWeatherHash"


class MachineTier(Enum):
    UNDEFINED = "Undefined"
    TIER_ONE = "TierOne"
    TIER_TWO = "TierTwo"
    TIER_THREE = "TierThree"
    MAX = "Max"


@dataclass
class MaterialReference:
    smoothness: Optional[float] = field(
        default=None,
        metadata={
            "name": "Smoothness",
            "type": "Attribute",
            "required": True,
        },
    )
    metallic: Optional[float] = field(
        default=None,
        metadata={
            "name": "Metallic",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class MeshReference:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    path: Optional[str] = field(
        default=None,
        metadata={
            "name": "Path",
            "type": "Attribute",
        },
    )
    scale: Optional[float] = field(
        default=None,
        metadata={
            "name": "Scale",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class MessageBaseOfKitMetaData:
    pass


@dataclass
class MessageBaseOfSpawnGas:
    pass


class MinableType(Enum):
    NONE = "None"
    STONE = "Stone"
    IRON = "Iron"
    ICE = "Ice"
    GOLD = "Gold"
    COAL = "Coal"
    COPPER = "Copper"
    URANIUM = "Uranium"
    NICKEL = "Nickel"
    LEAD = "Lead"
    SILVER = "Silver"
    SILICON = "Silicon"
    OXITE = "Oxite"
    VOLATILES = "Volatiles"
    GEYSER_HYDROGEN = "GeyserHydrogen"
    COBALT = "Cobalt"
    NITRICE = "Nitrice"
    LAST_MINABLE = "LastMinable"
    CRATER = "Crater"
    BEDROCK = "Bedrock"


@dataclass
class MineableDepositSaveData:
    density: Optional[float] = field(
        default=None,
        metadata={
            "name": "Density",
            "type": "Element",
            "required": True,
        },
    )
    richness: Optional[float] = field(
        default=None,
        metadata={
            "name": "Richness",
            "type": "Element",
            "required": True,
        },
    )
    size: Optional[float] = field(
        default=None,
        metadata={
            "name": "Size",
            "type": "Element",
            "required": True,
        },
    )
    mined_quantity_total: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinedQuantityTotal",
            "type": "Element",
            "required": True,
        },
    )
    total_ore_at_location: Optional[int] = field(
        default=None,
        metadata={
            "name": "TotalOreAtLocation",
            "type": "Element",
            "required": True,
        },
    )


class MixRule(Enum):
    NONE = "None"
    PURE = "Pure"


@dataclass
class MoleEnergy:
    pass


@dataclass
class MoleQuantity:
    pass


@dataclass
class MultiPlantStatData:
    mid_point: Optional[float] = field(
        default=None,
        metadata={
            "name": "MidPoint",
            "type": "Attribute",
            "required": True,
        },
    )
    center_size: Optional[float] = field(
        default=None,
        metadata={
            "name": "CenterSize",
            "type": "Attribute",
            "required": True,
        },
    )
    low_size: Optional[float] = field(
        default=None,
        metadata={
            "name": "LowSize",
            "type": "Attribute",
            "required": True,
        },
    )
    high_size: Optional[float] = field(
        default=None,
        metadata={
            "name": "HighSize",
            "type": "Attribute",
            "required": True,
        },
    )
    clamp: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Clamp",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class NodeConnectionData:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    distance_multiplier: Optional[float] = field(
        default=None,
        metadata={
            "name": "DistanceMultiplier",
            "type": "Attribute",
            "required": True,
        },
    )
    difficulty: Optional[int] = field(
        default=None,
        metadata={
            "name": "Difficulty",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class NodeIcon:
    path: Optional[str] = field(
        default=None,
        metadata={
            "name": "Path",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    size: Optional[float] = field(
        default=None,
        metadata={
            "name": "Size",
            "type": "Attribute",
            "required": True,
        },
    )
    tint: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tint",
            "type": "Attribute",
        },
    )
    selection_size: Optional[float] = field(
        default=None,
        metadata={
            "name": "SelectionSize",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class NoiseLayerData:
    emissive: Optional[float] = field(
        default=None,
        metadata={
            "name": "Emissive",
            "type": "Attribute",
            "required": True,
        },
    )
    threshold: Optional[float] = field(
        default=None,
        metadata={
            "name": "Threshold",
            "type": "Attribute",
            "required": True,
        },
    )
    power: Optional[float] = field(
        default=None,
        metadata={
            "name": "Power",
            "type": "Attribute",
            "required": True,
        },
    )
    multiplier: Optional[float] = field(
        default=None,
        metadata={
            "name": "Multiplier",
            "type": "Attribute",
            "required": True,
        },
    )
    mask_multiplier: Optional[float] = field(
        default=None,
        metadata={
            "name": "MaskMultiplier",
            "type": "Attribute",
            "required": True,
        },
    )


class OcclusionDownscale(Enum):
    X1 = "x1"
    X2 = "x2"
    X4 = "x4"


class OcclusionSamples(Enum):
    X64 = "x64"
    X164 = "x164"
    X244 = "x244"


class OcclusionType(Enum):
    LOS = "LOS"
    ROOM = "Room"
    NONE = "None"


@dataclass
class OrbitData:
    period: Optional[float] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Attribute",
            "required": True,
        },
    )
    inclination: Optional[float] = field(
        default=None,
        metadata={
            "name": "Inclination",
            "type": "Attribute",
            "required": True,
        },
    )
    eccentricity: Optional[float] = field(
        default=None,
        metadata={
            "name": "Eccentricity",
            "type": "Attribute",
            "required": True,
        },
    )
    semi_major_axis_km: Optional[float] = field(
        default=None,
        metadata={
            "name": "SemiMajorAxisKm",
            "type": "Attribute",
            "required": True,
        },
    )
    semi_major_axis_au: Optional[float] = field(
        default=None,
        metadata={
            "name": "SemiMajorAxisAu",
            "type": "Attribute",
            "required": True,
        },
    )
    argument_of_periapsis: Optional[float] = field(
        default=None,
        metadata={
            "name": "ArgumentOfPeriapsis",
            "type": "Attribute",
            "required": True,
        },
    )
    longitude_of_ascending_node: Optional[float] = field(
        default=None,
        metadata={
            "name": "LongitudeOfAscendingNode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class PerennialData:
    revert_to_stage: Optional[int] = field(
        default=None,
        metadata={
            "name": "RevertToStage",
            "type": "Attribute",
            "required": True,
        },
    )


class PipeBurstValue(Enum):
    NONE = "None"
    FALSE = "false"
    PRESSURE = "Pressure"
    TRUE = "true"
    LIQUID = "Liquid"
    SOLID = "Solid"


@dataclass
class PlantRecord:
    plant_reference: Optional[int] = field(
        default=None,
        metadata={
            "name": "PlantReference",
            "type": "Element",
            "required": True,
        },
    )
    age: Optional[float] = field(
        default=None,
        metadata={
            "name": "Age",
            "type": "Element",
            "required": True,
        },
    )
    light_stress: Optional[float] = field(
        default=None,
        metadata={
            "name": "LightStress",
            "type": "Element",
            "required": True,
        },
    )
    time_lit_ratio: Optional[float] = field(
        default=None,
        metadata={
            "name": "TimeLitRatio",
            "type": "Element",
            "required": True,
        },
    )
    time_darkness_ratio: Optional[float] = field(
        default=None,
        metadata={
            "name": "TimeDarknessRatio",
            "type": "Element",
            "required": True,
        },
    )
    time_dehydrated: Optional[float] = field(
        default=None,
        metadata={
            "name": "TimeDehydrated",
            "type": "Element",
            "required": True,
        },
    )
    time_frozen: Optional[float] = field(
        default=None,
        metadata={
            "name": "TimeFrozen",
            "type": "Element",
            "required": True,
        },
    )
    time_over_heated: Optional[float] = field(
        default=None,
        metadata={
            "name": "TimeOverHeated",
            "type": "Element",
            "required": True,
        },
    )
    time_suffocated: Optional[float] = field(
        default=None,
        metadata={
            "name": "TimeSuffocated",
            "type": "Element",
            "required": True,
        },
    )
    time_low_pressure: Optional[float] = field(
        default=None,
        metadata={
            "name": "TimeLowPressure",
            "type": "Element",
            "required": True,
        },
    )
    time_high_pressure: Optional[float] = field(
        default=None,
        metadata={
            "name": "TimeHighPressure",
            "type": "Element",
            "required": True,
        },
    )
    time_polluted: Optional[float] = field(
        default=None,
        metadata={
            "name": "TimePolluted",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class PlantStatData:
    base: Optional[float] = field(
        default=None,
        metadata={
            "name": "Base",
            "type": "Attribute",
            "required": True,
        },
    )
    invert: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Invert",
            "type": "Attribute",
            "required": True,
        },
    )


class PlantStatusType(Enum):
    DEHYDRATED = "Dehydrated"
    LIT = "Lit"
    DARKNESS = "Darkness"
    LOW_TEMPERATURE = "LowTemperature"
    HIGH_TEMPERATURE = "HighTemperature"
    SUFFOCATED = "Suffocated"
    LOW_PRESSURE = "LowPressure"
    HIGH_PRESSURE = "HighPressure"
    UN_DESIRED_GAS = "UnDesiredGas"
    LOW_WATER_TEMPERATURE = "LowWaterTemperature"
    HIGH_WATER_TEMPERATURE = "HighWaterTemperature"


class PlayableAreaRule(Enum):
    NONE = "None"
    VALID = "Valid"
    WARNING = "Warning"
    INVALID = "Invalid"


@dataclass
class PlayerCookieSaveDataV1:
    version: Optional[int] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Element",
            "required": True,
        },
    )
    client_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ClientId",
            "type": "Element",
            "required": True,
        },
    )
    username: Optional[str] = field(
        default=None,
        metadata={
            "name": "Username",
            "type": "Element",
        },
    )
    password: Optional[str] = field(
        default=None,
        metadata={
            "name": "Password",
            "type": "Element",
        },
    )


@dataclass
class PrefabReference:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass
class Pressure:
    start: Optional[float] = field(
        default=None,
        metadata={
            "name": "Start",
            "type": "Element",
            "required": True,
        },
    )
    stop: Optional[float] = field(
        default=None,
        metadata={
            "name": "Stop",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class PressurekPa:
    pass


@dataclass
class ProcessingData:
    input_prefab: Optional[str] = field(
        default=None,
        metadata={
            "name": "InputPrefab",
            "type": "Element",
        },
    )
    output_prefab: Optional[str] = field(
        default=None,
        metadata={
            "name": "OutputPrefab",
            "type": "Element",
        },
    )
    time: Optional[float] = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Element",
            "required": True,
        },
    )
    in_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "In",
            "type": "Element",
            "required": True,
        },
    )
    out: Optional[int] = field(
        default=None,
        metadata={
            "name": "Out",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class QuarryCollectedOre:
    ore_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "OreName",
            "type": "Element",
        },
    )
    quantity: Optional[float] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RandomPoolData:
    index: Optional[int] = field(
        default=None,
        metadata={
            "name": "Index",
            "type": "Attribute",
            "required": True,
        },
    )
    weight: Optional[int] = field(
        default=None,
        metadata={
            "name": "Weight",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class RayMarchData:
    steps: Optional[int] = field(
        default=None,
        metadata={
            "name": "Steps",
            "type": "Attribute",
            "required": True,
        },
    )
    size: Optional[float] = field(
        default=None,
        metadata={
            "name": "Size",
            "type": "Attribute",
            "required": True,
        },
    )
    growth: Optional[float] = field(
        default=None,
        metadata={
            "name": "Growth",
            "type": "Attribute",
            "required": True,
        },
    )
    density: Optional[float] = field(
        default=None,
        metadata={
            "name": "Density",
            "type": "Attribute",
            "required": True,
        },
    )


class ReEntryProfile(Enum):
    NONE = "None"
    OPTIMAL = "Optimal"
    MEDIUM = "Medium"
    HIGH = "High"
    MAX = "Max"


@dataclass
class Reagent:
    reagent_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ReagentId",
            "type": "Element",
            "required": True,
        },
    )
    quantity: Optional[float] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ReagentData:
    flour: Optional[float] = field(
        default=None,
        metadata={
            "name": "Flour",
            "type": "Attribute",
            "required": True,
        },
    )
    milk: Optional[float] = field(
        default=None,
        metadata={
            "name": "Milk",
            "type": "Attribute",
            "required": True,
        },
    )
    egg: Optional[float] = field(
        default=None,
        metadata={
            "name": "Egg",
            "type": "Attribute",
            "required": True,
        },
    )
    iron: Optional[float] = field(
        default=None,
        metadata={
            "name": "Iron",
            "type": "Attribute",
            "required": True,
        },
    )
    gold: Optional[float] = field(
        default=None,
        metadata={
            "name": "Gold",
            "type": "Attribute",
            "required": True,
        },
    )
    carbon: Optional[float] = field(
        default=None,
        metadata={
            "name": "Carbon",
            "type": "Attribute",
            "required": True,
        },
    )
    uranium: Optional[float] = field(
        default=None,
        metadata={
            "name": "Uranium",
            "type": "Attribute",
            "required": True,
        },
    )
    copper: Optional[float] = field(
        default=None,
        metadata={
            "name": "Copper",
            "type": "Attribute",
            "required": True,
        },
    )
    steel: Optional[float] = field(
        default=None,
        metadata={
            "name": "Steel",
            "type": "Attribute",
            "required": True,
        },
    )
    hydrocarbon: Optional[float] = field(
        default=None,
        metadata={
            "name": "Hydrocarbon",
            "type": "Attribute",
            "required": True,
        },
    )
    silver: Optional[float] = field(
        default=None,
        metadata={
            "name": "Silver",
            "type": "Attribute",
            "required": True,
        },
    )
    nickel: Optional[float] = field(
        default=None,
        metadata={
            "name": "Nickel",
            "type": "Attribute",
            "required": True,
        },
    )
    lead: Optional[float] = field(
        default=None,
        metadata={
            "name": "Lead",
            "type": "Attribute",
            "required": True,
        },
    )
    electrum: Optional[float] = field(
        default=None,
        metadata={
            "name": "Electrum",
            "type": "Attribute",
            "required": True,
        },
    )
    invar: Optional[float] = field(
        default=None,
        metadata={
            "name": "Invar",
            "type": "Attribute",
            "required": True,
        },
    )
    constantan: Optional[float] = field(
        default=None,
        metadata={
            "name": "Constantan",
            "type": "Attribute",
            "required": True,
        },
    )
    solder: Optional[float] = field(
        default=None,
        metadata={
            "name": "Solder",
            "type": "Attribute",
            "required": True,
        },
    )
    plastic: Optional[float] = field(
        default=None,
        metadata={
            "name": "Plastic",
            "type": "Attribute",
            "required": True,
        },
    )
    silicon: Optional[float] = field(
        default=None,
        metadata={
            "name": "Silicon",
            "type": "Attribute",
            "required": True,
        },
    )
    salicylic_acid: Optional[float] = field(
        default=None,
        metadata={
            "name": "SalicylicAcid",
            "type": "Attribute",
            "required": True,
        },
    )
    alcohol: Optional[float] = field(
        default=None,
        metadata={
            "name": "Alcohol",
            "type": "Attribute",
            "required": True,
        },
    )
    oil: Optional[float] = field(
        default=None,
        metadata={
            "name": "Oil",
            "type": "Attribute",
            "required": True,
        },
    )
    potato: Optional[float] = field(
        default=None,
        metadata={
            "name": "Potato",
            "type": "Attribute",
            "required": True,
        },
    )
    tomato: Optional[float] = field(
        default=None,
        metadata={
            "name": "Tomato",
            "type": "Attribute",
            "required": True,
        },
    )
    fenoxitone: Optional[float] = field(
        default=None,
        metadata={
            "name": "Fenoxitone",
            "type": "Attribute",
            "required": True,
        },
    )
    color_red: Optional[float] = field(
        default=None,
        metadata={
            "name": "ColorRed",
            "type": "Attribute",
            "required": True,
        },
    )
    color_green: Optional[float] = field(
        default=None,
        metadata={
            "name": "ColorGreen",
            "type": "Attribute",
            "required": True,
        },
    )
    color_blue: Optional[float] = field(
        default=None,
        metadata={
            "name": "ColorBlue",
            "type": "Attribute",
            "required": True,
        },
    )
    color_yellow: Optional[float] = field(
        default=None,
        metadata={
            "name": "ColorYellow",
            "type": "Attribute",
            "required": True,
        },
    )
    color_orange: Optional[float] = field(
        default=None,
        metadata={
            "name": "ColorOrange",
            "type": "Attribute",
            "required": True,
        },
    )
    pumpkin: Optional[float] = field(
        default=None,
        metadata={
            "name": "Pumpkin",
            "type": "Attribute",
            "required": True,
        },
    )
    rice: Optional[float] = field(
        default=None,
        metadata={
            "name": "Rice",
            "type": "Attribute",
            "required": True,
        },
    )
    waspaloy: Optional[float] = field(
        default=None,
        metadata={
            "name": "Waspaloy",
            "type": "Attribute",
            "required": True,
        },
    )
    stellite: Optional[float] = field(
        default=None,
        metadata={
            "name": "Stellite",
            "type": "Attribute",
            "required": True,
        },
    )
    inconel: Optional[float] = field(
        default=None,
        metadata={
            "name": "Inconel",
            "type": "Attribute",
            "required": True,
        },
    )
    hastelloy: Optional[float] = field(
        default=None,
        metadata={
            "name": "Hastelloy",
            "type": "Attribute",
            "required": True,
        },
    )
    astroloy: Optional[float] = field(
        default=None,
        metadata={
            "name": "Astroloy",
            "type": "Attribute",
            "required": True,
        },
    )
    cobalt: Optional[float] = field(
        default=None,
        metadata={
            "name": "Cobalt",
            "type": "Attribute",
            "required": True,
        },
    )
    corn: Optional[float] = field(
        default=None,
        metadata={
            "name": "Corn",
            "type": "Attribute",
            "required": True,
        },
    )
    wheat: Optional[float] = field(
        default=None,
        metadata={
            "name": "Wheat",
            "type": "Attribute",
            "required": True,
        },
    )
    biomass: Optional[float] = field(
        default=None,
        metadata={
            "name": "Biomass",
            "type": "Attribute",
            "required": True,
        },
    )
    soy: Optional[float] = field(
        default=None,
        metadata={
            "name": "Soy",
            "type": "Attribute",
            "required": True,
        },
    )
    mushroom: Optional[float] = field(
        default=None,
        metadata={
            "name": "Mushroom",
            "type": "Attribute",
            "required": True,
        },
    )
    sugar: Optional[float] = field(
        default=None,
        metadata={
            "name": "Sugar",
            "type": "Attribute",
            "required": True,
        },
    )
    cocoa: Optional[float] = field(
        default=None,
        metadata={
            "name": "Cocoa",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ReagentSaveData:
    type_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeName",
            "type": "Element",
        },
    )
    quantity: Optional[float] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ReagentTradeData:
    reagent: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reagent",
            "type": "Element",
        },
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Record:
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Element",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )


@dataclass
class RecordReagent:
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Element",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )
    unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
        },
    )


@dataclass
class ReferencableSaveData:
    reference_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ReferenceId",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RequirementWrapper:
    base_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "BaseValue",
            "type": "Element",
            "required": True,
        },
    )
    min_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "MinValue",
            "type": "Element",
            "required": True,
        },
    )
    current_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "CurrentValue",
            "type": "Element",
            "required": True,
        },
    )
    max_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "MaxValue",
            "type": "Element",
            "required": True,
        },
    )


class ResearchPodType(Enum):
    UNDEFINED = "Undefined"
    RED = "Red"
    GREEN = "Green"
    BLUE = "Blue"
    YELLOW = "Yellow"
    MAX = "Max"


class ResearchSort(Enum):
    UNDEFINED = "Undefined"
    MILITARY = "Military"
    PRODUCTION = "Production"
    AUTOMATION = "Automation"
    TOOLS = "Tools"
    ORGANICS = "Organics"
    CONSTRUCTION = "Construction"
    LOGIC = "Logic"
    VEHICLES = "Vehicles"
    MAX = "Max"


class ReverbType(Enum):
    FLAT = "Flat"
    SPATIAL = "Spatial"
    NONE = "None"
    QUIET = "Quiet"
    FLAT_LOUD = "FlatLoud"


@dataclass
class RingReference:
    enabled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Enabled",
            "type": "Attribute",
            "required": True,
        },
    )


class RocketMode(Enum):
    INVALID = "Invalid"
    NONE = "None"
    MINE = "Mine"
    SURVEY = "Survey"
    DISCOVER = "Discover"
    CHART = "Chart"
    DEPLOY = "Deploy"


@dataclass
class RocketName:
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        },
    )


class RocketState(Enum):
    NONE = "None"
    ON_LAUNCH_MOUNT = "OnLaunchMount"
    LAUNCHING = "Launching"
    IN_SPACE = "InSpace"
    LANDING = "Landing"


@dataclass
class RoomRuleConditionData:
    pass


class RoomType(Enum):
    UNDEFINED = "Undefined"
    DEFAULT = "Default"
    MANUFACTURING = "Manufacturing"
    KITCHEN = "Kitchen"
    BEDROOM = "Bedroom"
    HYDROPONICS = "Hydroponics"


class SpdaentryType(Enum):
    UNDEFINED = "Undefined"
    GUIDES = "Guides"
    LORE = "Lore"
    MAXIMUM = "Maximum"


@dataclass
class SpdahomePageButtonOverride:
    class Meta:
        name = "SPDAHomePageButtonOverride"

    category_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CategoryName",
            "type": "Element",
        },
    )
    thing_name_for_image: Optional[str] = field(
        default=None,
        metadata={
            "name": "ThingNameForImage",
            "type": "Element",
        },
    )
    linked_page_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "LinkedPageKey",
            "type": "Element",
        },
    )


@dataclass
class SpdathingOverideData:
    class Meta:
        name = "SPDAThingOverideData"

    parent_list_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParentListKey",
            "type": "Element",
        },
    )
    thing_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ThingName",
            "type": "Element",
        },
    )
    hide_in_spda: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HideInSPDA",
            "type": "Element",
            "required": True,
        },
    )
    custom_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomCategory",
            "type": "Element",
        },
    )


@dataclass
class SeekData:
    attempts: Optional[int] = field(
        default=None,
        metadata={
            "name": "Attempts",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SerializedClientInfo:
    client_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ClientId",
            "type": "Element",
            "required": True,
        },
    )
    start_location_hash: Optional[int] = field(
        default=None,
        metadata={
            "name": "StartLocationHash",
            "type": "Element",
            "required": True,
        },
    )
    spawn_point_reference: Optional[int] = field(
        default=None,
        metadata={
            "name": "SpawnPointReference",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SerializedId:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass
class SerializedReferenceId:
    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SettingBase:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


class ShuttleType(Enum):
    NONE = "None"
    SMALL = "Small"
    SMALL_GAS = "SmallGas"
    MEDIUM = "Medium"
    MEDIUM_GAS = "MediumGas"
    LARGE = "Large"
    LARGE_GAS = "LargeGas"
    MEDIUM_PLANE = "MediumPlane"
    LARGE_PLANE = "LargePlane"


class ShuttleVariant(Enum):
    NONE = "None"
    GAS = "Gas"


@dataclass
class SlotCondition:
    chance: Optional[float] = field(
        default=None,
        metadata={
            "name": "Chance",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SlotIcon:
    path: Optional[str] = field(
        default=None,
        metadata={
            "name": "Path",
            "type": "Attribute",
        },
    )


@dataclass
class SlotIdReference:
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
        },
    )


class SpatialReference(Enum):
    VALUE_2_D = "2D"
    VALUE_3_D = "3D"
    SMALL = "Small"
    LARGE = "Large"
    MEDIUM = "Medium"
    MEDIUM_SMALL = "MediumSmall"
    MEDIUM_LARGE = "MediumLarge"


@dataclass
class SpatialSoundData:
    doppler_level: Optional[float] = field(
        default=None,
        metadata={
            "name": "DopplerLevel",
            "type": "Element",
            "required": True,
        },
    )
    spread: Optional[float] = field(
        default=None,
        metadata={
            "name": "Spread",
            "type": "Element",
            "required": True,
        },
    )
    volume_rolloff_type: Optional[int] = field(
        default=None,
        metadata={
            "name": "VolumeRolloffType",
            "type": "Element",
            "required": True,
        },
    )
    min_distance: Optional[float] = field(
        default=None,
        metadata={
            "name": "MinDistance",
            "type": "Element",
            "required": True,
        },
    )
    max_distance: Optional[float] = field(
        default=None,
        metadata={
            "name": "MaxDistance",
            "type": "Element",
            "required": True,
        },
    )
    reverb_zone_mix: Optional[float] = field(
        default=None,
        metadata={
            "name": "ReverbZoneMix",
            "type": "Element",
            "required": True,
        },
    )


class SpawnEvent(Enum):
    NONE = "None"
    NEW_WORLD = "NewWorld"
    NEW_PLAYER_KIT = "NewPlayerKit"
    RESPAWN_PLAYER_KIT = "RespawnPlayerKit"
    NEW_PLAYER = "NewPlayer"
    RESPAWN_PLAYER = "RespawnPlayer"


class SpawnPositionRule(Enum):
    NONE = "None"
    RANDOM = "Random"
    RADIAL = "Radial"
    EXPLICIT = "Explicit"


class SpeciesClass(Enum):
    NONE = "None"
    HUMAN = "Human"
    ZRILIAN = "Zrilian"
    ROBOT = "Robot"


@dataclass
class SpriteReference:
    path: Optional[str] = field(
        default=None,
        metadata={
            "name": "Path",
            "type": "Attribute",
        },
    )


@dataclass
class StarData:
    minimum: Optional[float] = field(
        default=None,
        metadata={
            "name": "Minimum",
            "type": "Attribute",
            "required": True,
        },
    )
    brightness: Optional[float] = field(
        default=None,
        metadata={
            "name": "Brightness",
            "type": "Attribute",
            "required": True,
        },
    )
    fade_height: Optional[float] = field(
        default=None,
        metadata={
            "name": "FadeHeight",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class StationDrillHeadProperties:
    pass


@dataclass
class StationFoundInInsert:
    name_of_thing: Optional[str] = field(
        default=None,
        metadata={
            "name": "NameOfThing",
            "type": "Element",
        },
    )
    quantity_of_thing: Optional[str] = field(
        default=None,
        metadata={
            "name": "QuantityOfThing",
            "type": "Element",
        },
    )


@dataclass
class StationInstruction:
    text: Optional[str] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
        },
    )
    index: Optional[str] = field(
        default=None,
        metadata={
            "name": "Index",
            "type": "Element",
        },
    )
    info: Optional[str] = field(
        default=None,
        metadata={
            "name": "Info",
            "type": "Element",
        },
    )


@dataclass
class StationLifeRequirement:
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )
    gene: Optional[str] = field(
        default=None,
        metadata={
            "name": "Gene",
            "type": "Element",
        },
    )
    value_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "ValueSize",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class StationLogicInsert:
    logic_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LogicName",
            "type": "Element",
        },
    )
    logic_access_types: Optional[str] = field(
        default=None,
        metadata={
            "name": "LogicAccessTypes",
            "type": "Element",
        },
    )


@dataclass
class StationSuitProperties:
    pass


@dataclass
class StringReference:
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
        },
    )


class StructureNetworkType(Enum):
    NONE = "None"
    LANDING_PAD = "LandingPad"
    PIPE = "Pipe"
    CHUTE = "Chute"
    ROCKET = "Rocket"
    LAUNCH_PAD = "LaunchPad"
    ROBOTIC_ARM = "RoboticArm"
    CABLE = "Cable"


@dataclass
class Temperature:
    start: Optional[float] = field(
        default=None,
        metadata={
            "name": "Start",
            "type": "Element",
            "required": True,
        },
    )
    stop: Optional[float] = field(
        default=None,
        metadata={
            "name": "Stop",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class TemperatureKelvin:
    pass


class TemperatureType(Enum):
    KELVIN = "Kelvin"
    CELSIUS = "Celsius"


class TextureFormat(Enum):
    ALPHA8 = "Alpha8"
    ARGB4444 = "ARGB4444"
    RGB24 = "RGB24"
    RGBA32 = "RGBA32"
    ARGB32 = "ARGB32"
    RGB565 = "RGB565"
    R16 = "R16"
    DXT1 = "DXT1"
    DXT5 = "DXT5"
    RGBA4444 = "RGBA4444"
    BGRA32 = "BGRA32"
    RHALF = "RHalf"
    RGHALF = "RGHalf"
    RGBAHALF = "RGBAHalf"
    RFLOAT = "RFloat"
    RGFLOAT = "RGFloat"
    RGBAFLOAT = "RGBAFloat"
    YUY2 = "YUY2"
    RGB9E5_FLOAT = "RGB9e5Float"
    BC4 = "BC4"
    BC5 = "BC5"
    BC6_H = "BC6H"
    BC7 = "BC7"
    DXT1_CRUNCHED = "DXT1Crunched"
    DXT5_CRUNCHED = "DXT5Crunched"
    PVRTC_RGB2 = "PVRTC_RGB2"
    PVRTC_RGBA2 = "PVRTC_RGBA2"
    PVRTC_RGB4 = "PVRTC_RGB4"
    PVRTC_RGBA4 = "PVRTC_RGBA4"
    ETC_RGB4 = "ETC_RGB4"
    EAC_R = "EAC_R"
    EAC_R_SIGNED = "EAC_R_SIGNED"
    EAC_RG = "EAC_RG"
    EAC_RG_SIGNED = "EAC_RG_SIGNED"
    ETC2_RGB = "ETC2_RGB"
    ETC2_RGBA1 = "ETC2_RGBA1"
    ETC2_RGBA8 = "ETC2_RGBA8"
    ASTC_4X4 = "ASTC_4x4"
    ASTC_5X5 = "ASTC_5x5"
    ASTC_6X6 = "ASTC_6x6"
    ASTC_8X8 = "ASTC_8x8"
    ASTC_10X10 = "ASTC_10x10"
    ASTC_12X12 = "ASTC_12x12"
    RG16 = "RG16"
    R8 = "R8"
    ETC_RGB4_CRUNCHED = "ETC_RGB4Crunched"
    ETC2_RGBA8_CRUNCHED = "ETC2_RGBA8Crunched"
    ASTC_HDR_4X4 = "ASTC_HDR_4x4"
    ASTC_HDR_5X5 = "ASTC_HDR_5x5"
    ASTC_HDR_6X6 = "ASTC_HDR_6x6"
    ASTC_HDR_8X8 = "ASTC_HDR_8x8"
    ASTC_HDR_10X10 = "ASTC_HDR_10x10"
    ASTC_HDR_12X12 = "ASTC_HDR_12x12"
    RG32 = "RG32"
    RGB48 = "RGB48"
    RGBA64 = "RGBA64"


class TextureLoadType(Enum):
    NONE = "None"
    PRELOAD = "Preload"
    ON_REQUEST = "OnRequest"


@dataclass
class ThingModData:
    prefab_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrefabName",
            "type": "Element",
        },
    )
    surface_area_scale: Optional[float] = field(
        default=None,
        metadata={
            "name": "SurfaceAreaScale",
            "type": "Element",
            "required": True,
        },
    )
    thermodynamics_scale: Optional[float] = field(
        default=None,
        metadata={
            "name": "ThermodynamicsScale",
            "type": "Element",
            "required": True,
        },
    )
    solar_heating_scale: Optional[float] = field(
        default=None,
        metadata={
            "name": "SolarHeatingScale",
            "type": "Element",
            "required": True,
        },
    )
    shatter_temperature: Optional[float] = field(
        default=None,
        metadata={
            "name": "ShatterTemperature",
            "type": "Element",
            "required": True,
        },
    )
    flashpoint_temperature: Optional[float] = field(
        default=None,
        metadata={
            "name": "FlashpointTemperature",
            "type": "Element",
            "required": True,
        },
    )
    autoignition_temperature: Optional[float] = field(
        default=None,
        metadata={
            "name": "AutoignitionTemperature",
            "type": "Element",
            "required": True,
        },
    )
    burn_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "BurnTime",
            "type": "Element",
            "required": True,
        },
    )
    energy_released_when_burning: Optional[float] = field(
        default=None,
        metadata={
            "name": "EnergyReleasedWhenBurning",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class TimeSpanReference:
    days: Optional[float] = field(
        default=None,
        metadata={
            "name": "Days",
            "type": "Attribute",
            "required": True,
        },
    )
    hours: Optional[float] = field(
        default=None,
        metadata={
            "name": "Hours",
            "type": "Attribute",
            "required": True,
        },
    )
    minutes: Optional[float] = field(
        default=None,
        metadata={
            "name": "Minutes",
            "type": "Attribute",
            "required": True,
        },
    )
    seconds: Optional[float] = field(
        default=None,
        metadata={
            "name": "Seconds",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TransactionSaveData:
    reference_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ReferenceId",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class TransformData:
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    y: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    z: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    rx: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    ry: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    rz: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TreeDepthModifer:
    value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )
    mul: Optional[float] = field(
        default=None,
        metadata={
            "name": "Mul",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class UshortReference:
    value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ValueRange:
    minimum: Optional[float] = field(
        default=None,
        metadata={
            "name": "Minimum",
            "type": "Attribute",
            "required": True,
        },
    )
    maximum: Optional[float] = field(
        default=None,
        metadata={
            "name": "Maximum",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Vector2:
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    y: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Vector2Int:
    x: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    y: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Vector2Reference:
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    y: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Vector3:
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    y: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    z: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


class VentDirection(Enum):
    INWARD = "Inward"
    OUTWARD = "Outward"


@dataclass
class VoiceNotificationData:
    notification: Optional[str] = field(
        default=None,
        metadata={
            "name": "Notification",
            "type": "Element",
        },
    )
    is_enabled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsEnabled",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class VolumeLitres:
    pass


@dataclass
class WeatherManagerSavedData:
    current_weather_event_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurrentWeatherEventId",
            "type": "Element",
        },
    )
    is_weather_event_running: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsWeatherEventRunning",
            "type": "Element",
            "required": True,
        },
    )
    is_weather_event_scheduled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsWeatherEventScheduled",
            "type": "Element",
            "required": True,
        },
    )
    weather_start_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "WeatherStartTime",
            "type": "Element",
            "required": True,
        },
    )
    weather_event_length: Optional[float] = field(
        default=None,
        metadata={
            "name": "WeatherEventLength",
            "type": "Element",
            "required": True,
        },
    )
    days_since_last_weather_event: Optional[int] = field(
        default=None,
        metadata={
            "name": "DaysSinceLastWeatherEvent",
            "type": "Element",
            "required": True,
        },
    )
    last_event_cool_down: Optional[int] = field(
        default=None,
        metadata={
            "name": "LastEventCoolDown",
            "type": "Element",
            "required": True,
        },
    )


class WeightedMode(Enum):
    NONE = "None"
    IN = "In"
    OUT = "Out"
    BOTH = "Both"


@dataclass
class Window:
    slot: Optional[int] = field(
        default=None,
        metadata={
            "name": "Slot",
            "type": "Attribute",
            "required": True,
        },
    )
    hash: Optional[int] = field(
        default=None,
        metadata={
            "name": "Hash",
            "type": "Attribute",
            "required": True,
        },
    )
    open: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Open",
            "type": "Attribute",
            "required": True,
        },
    )
    docked: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Docked",
            "type": "Attribute",
            "required": True,
        },
    )
    x: Optional[float] = field(
        default=None,
        metadata={
            "name": "X",
            "type": "Attribute",
            "required": True,
        },
    )
    y: Optional[float] = field(
        default=None,
        metadata={
            "name": "Y",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class WorldEventData:
    text: Optional[str] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Attribute",
        },
    )
    date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "DateTime",
            "type": "Attribute",
        },
    )


@dataclass
class WorldGrid:
    pass


@dataclass
class WorldMetaData:
    game: Optional[str] = field(
        default=None,
        metadata={
            "name": "Game",
            "type": "Element",
        },
    )
    game_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "GameVersion",
            "type": "Element",
        },
    )
    date_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "DateTime",
            "type": "Element",
            "required": True,
        },
    )
    days_past: Optional[int] = field(
        default=None,
        metadata={
            "name": "DaysPast",
            "type": "Element",
            "required": True,
        },
    )
    world_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "WorldName",
            "type": "Element",
        },
    )
    world_file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "WorldFileName",
            "type": "Element",
        },
    )
    work_shop_file_handle: Optional[int] = field(
        default=None,
        metadata={
            "name": "WorkShopFileHandle",
            "type": "Element",
            "required": True,
        },
    )
    number_of_rooms: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfRooms",
            "type": "Element",
            "required": True,
        },
    )
    number_of_pipe_networks: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfPipeNetworks",
            "type": "Element",
            "required": True,
        },
    )
    number_of_cable_networks: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfCableNetworks",
            "type": "Element",
            "required": True,
        },
    )
    number_of_things: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfThings",
            "type": "Element",
            "required": True,
        },
    )
    number_of_atmospheres: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfAtmospheres",
            "type": "Element",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass
class WorldObjectiveSaveData:
    reference_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ReferenceId",
            "type": "Attribute",
            "required": True,
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "required": True,
        },
    )
    triggered: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Triggered",
            "type": "Attribute",
            "required": True,
        },
    )
    completed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Completed",
            "type": "Attribute",
            "required": True,
        },
    )
    dismissed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Dismissed",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class AchievementChainData(AchievementData):
    point_of_interest: list[SerializedId] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterest",
            "type": "Element",
        },
    )


@dataclass
class AchievementSurvivalData(AchievementData):
    days_lived: Optional[int] = field(
        default=None,
        metadata={
            "name": "DaysLived",
            "type": "Attribute",
            "required": True,
        },
    )
    difficulty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Difficulty",
            "type": "Attribute",
        },
    )


@dataclass
class AirControlVent:
    reference_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ReferenceId",
            "type": "Element",
            "required": True,
        },
    )
    direction: Optional[VentDirection] = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class AmbientLightingReference:
    sky: Optional[ColorRgb] = field(
        default=None,
        metadata={
            "name": "Sky",
            "type": "Element",
        },
    )
    equator: Optional[ColorRgb] = field(
        default=None,
        metadata={
            "name": "Equator",
            "type": "Element",
        },
    )
    ground: Optional[ColorRgb] = field(
        default=None,
        metadata={
            "name": "Ground",
            "type": "Element",
        },
    )


@dataclass
class AnimCurveKey:
    time: Optional[float] = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )
    in_tangent: Optional[float] = field(
        default=None,
        metadata={
            "name": "InTangent",
            "type": "Attribute",
            "required": True,
        },
    )
    out_tangent: Optional[float] = field(
        default=None,
        metadata={
            "name": "OutTangent",
            "type": "Attribute",
            "required": True,
        },
    )
    in_weight: Optional[float] = field(
        default=None,
        metadata={
            "name": "InWeight",
            "type": "Attribute",
            "required": True,
        },
    )
    out_weight: Optional[float] = field(
        default=None,
        metadata={
            "name": "OutWeight",
            "type": "Attribute",
            "required": True,
        },
    )
    weighted_mode: Optional[WeightedMode] = field(
        default=None,
        metadata={
            "name": "WeightedMode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ArrayOfContactSlotSaveData:
    contact_slot_save_data: list[ContactSlotSaveData] = field(
        default_factory=list,
        metadata={
            "name": "ContactSlotSaveData",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfFabricatorJob:
    job: list[FabricatorJob] = field(
        default_factory=list,
        metadata={
            "name": "Job",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfGasTradeData:
    gas_trade_data: list[GasTradeData] = field(
        default_factory=list,
        metadata={
            "name": "GasTradeData",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfGeneWrapper:
    gene_wrapper: list[GeneWrapper] = field(
        default_factory=list,
        metadata={
            "name": "GeneWrapper",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfGradientAlphaKey:
    gradient_alpha_key: list[GradientAlphaKey] = field(
        default_factory=list,
        metadata={
            "name": "GradientAlphaKey",
            "type": "Element",
        },
    )


@dataclass
class ArrayOfGrid3:
    grid: list[Grid3] = field(
        default_factory=list,
        metadata={
            "name": "Grid",
            "type": "Element",
        },
    )


@dataclass
class ArrayOfInteractableState:
    state: list[InteractableState] = field(
        default_factory=list,
        metadata={
            "name": "State",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfProcessingData:
    processing_data: list[ProcessingData] = field(
        default_factory=list,
        metadata={
            "name": "ProcessingData",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfReagentSaveData:
    reagent: list[ReagentSaveData] = field(
        default_factory=list,
        metadata={
            "name": "Reagent",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfReagentTradeData:
    reagent_trade_data: list[ReagentTradeData] = field(
        default_factory=list,
        metadata={
            "name": "ReagentTradeData",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfRecord:
    record: list[Record] = field(
        default_factory=list,
        metadata={
            "name": "Record",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfRecordReagent:
    record_reagent: list[RecordReagent] = field(
        default_factory=list,
        metadata={
            "name": "RecordReagent",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfRocketName:
    rocket_name: list[RocketName] = field(
        default_factory=list,
        metadata={
            "name": "RocketName",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfSpdahomePageButtonOverride:
    class Meta:
        name = "ArrayOfSPDAHomePageButtonOverride"

    spdahome_page_button_override: list[SpdahomePageButtonOverride] = field(
        default_factory=list,
        metadata={
            "name": "SPDAHomePageButtonOverride",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfSpdathingOverideData:
    class Meta:
        name = "ArrayOfSPDAThingOverideData"

    spdathing_overide_data: list[SpdathingOverideData] = field(
        default_factory=list,
        metadata={
            "name": "SPDAThingOverideData",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfStarData:
    star: list[StarData] = field(
        default_factory=list,
        metadata={
            "name": "Star",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfStationFoundInInsert:
    station_found_in_insert: list[StationFoundInInsert] = field(
        default_factory=list,
        metadata={
            "name": "StationFoundInInsert",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfStationInstruction:
    station_instruction: list[StationInstruction] = field(
        default_factory=list,
        metadata={
            "name": "StationInstruction",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfStationLifeRequirement:
    station_life_requirement: list[StationLifeRequirement] = field(
        default_factory=list,
        metadata={
            "name": "StationLifeRequirement",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfStationLogicInsert:
    station_logic_insert: list[StationLogicInsert] = field(
        default_factory=list,
        metadata={
            "name": "StationLogicInsert",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfThingModData:
    thing_mod_data: list[ThingModData] = field(
        default_factory=list,
        metadata={
            "name": "ThingModData",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfVoiceNotificationData:
    voice_notification_data: list[VoiceNotificationData] = field(
        default_factory=list,
        metadata={
            "name": "VoiceNotificationData",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfWorldGrid:
    world_grid: list[WorldGrid] = field(
        default_factory=list,
        metadata={
            "name": "WorldGrid",
            "type": "Element",
        },
    )


@dataclass
class ArrayOfWorldObjectiveSaveData:
    objective: list[WorldObjectiveSaveData] = field(
        default_factory=list,
        metadata={
            "name": "Objective",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class AtmosphereSaveData(ReferencableSaveData):
    position: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "Position",
            "type": "Element",
            "required": True,
        },
    )
    oxygen: Optional[float] = field(
        default=None,
        metadata={
            "name": "Oxygen",
            "type": "Element",
            "required": True,
        },
    )
    nitrogen: Optional[float] = field(
        default=None,
        metadata={
            "name": "Nitrogen",
            "type": "Element",
            "required": True,
        },
    )
    carbon_dioxide: Optional[float] = field(
        default=None,
        metadata={
            "name": "CarbonDioxide",
            "type": "Element",
            "required": True,
        },
    )
    volatiles: Optional[float] = field(
        default=None,
        metadata={
            "name": "Volatiles",
            "type": "Element",
            "required": True,
        },
    )
    chlorine: Optional[float] = field(
        default=None,
        metadata={
            "name": "Chlorine",
            "type": "Element",
            "required": True,
        },
    )
    water: Optional[float] = field(
        default=None,
        metadata={
            "name": "Water",
            "type": "Element",
            "required": True,
        },
    )
    polluted_water: Optional[float] = field(
        default=None,
        metadata={
            "name": "PollutedWater",
            "type": "Element",
            "required": True,
        },
    )
    nitrous_oxide: Optional[float] = field(
        default=None,
        metadata={
            "name": "NitrousOxide",
            "type": "Element",
            "required": True,
        },
    )
    liquid_nitrogen: Optional[float] = field(
        default=None,
        metadata={
            "name": "LiquidNitrogen",
            "type": "Element",
            "required": True,
        },
    )
    liquid_oxygen: Optional[float] = field(
        default=None,
        metadata={
            "name": "LiquidOxygen",
            "type": "Element",
            "required": True,
        },
    )
    liquid_volatiles: Optional[float] = field(
        default=None,
        metadata={
            "name": "LiquidVolatiles",
            "type": "Element",
            "required": True,
        },
    )
    steam: Optional[float] = field(
        default=None,
        metadata={
            "name": "Steam",
            "type": "Element",
            "required": True,
        },
    )
    liquid_carbon_dioxide: Optional[float] = field(
        default=None,
        metadata={
            "name": "LiquidCarbonDioxide",
            "type": "Element",
            "required": True,
        },
    )
    liquid_pollutant: Optional[float] = field(
        default=None,
        metadata={
            "name": "LiquidPollutant",
            "type": "Element",
            "required": True,
        },
    )
    liquid_nitrous_oxide: Optional[float] = field(
        default=None,
        metadata={
            "name": "LiquidNitrousOxide",
            "type": "Element",
            "required": True,
        },
    )
    hydrogen: Optional[float] = field(
        default=None,
        metadata={
            "name": "Hydrogen",
            "type": "Element",
            "required": True,
        },
    )
    liquid_hydrogen: Optional[float] = field(
        default=None,
        metadata={
            "name": "LiquidHydrogen",
            "type": "Element",
            "required": True,
        },
    )
    energy: Optional[float] = field(
        default=None,
        metadata={
            "name": "Energy",
            "type": "Element",
            "required": True,
        },
    )
    volume: Optional[float] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
            "required": True,
        },
    )
    direction: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Element",
            "required": True,
        },
    )
    network_reference_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "NetworkReferenceId",
            "type": "Element",
            "required": True,
        },
    )
    thing_reference_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ThingReferenceId",
            "type": "Element",
            "required": True,
        },
    )
    clean_burn_rate: Optional[float] = field(
        default=None,
        metadata={
            "name": "CleanBurnRate",
            "type": "Element",
            "required": True,
        },
    )
    mothership_reference_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "MothershipReferenceId",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class BooleanStateWrapper:
    state: Optional[PlantStatusType] = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Element",
            "required": True,
        },
    )
    value: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class BuildStateAction(ActionData):
    index: Optional[int] = field(
        default=None,
        metadata={
            "name": "Index",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class BuildStateCondition(ConditionData):
    is_completed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsCompleted",
            "type": "Attribute",
            "required": True,
        },
    )
    can_manufacture: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CanManufacture",
            "type": "Attribute",
            "required": True,
        },
    )
    machine_tier: Optional[MachineTier] = field(
        default=None,
        metadata={
            "name": "MachineTier",
            "type": "Attribute",
            "required": True,
        },
    )
    block_gravity: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BlockGravity",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class BuySaveData(TransactionSaveData):
    required: Optional[int] = field(
        default=None,
        metadata={
            "name": "Required",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class CelestialBodySaveData(CelestialSaveData):
    orbit: Optional[DoubleReference] = field(
        default=None,
        metadata={
            "name": "Orbit",
            "type": "Element",
        },
    )


@dataclass
class Chance(ChanceData):
    class Meta:
        nillable = True


@dataclass
class ChannelData:
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    index: Optional[int] = field(
        default=None,
        metadata={
            "name": "Index",
            "type": "Element",
            "required": True,
        },
    )
    priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "Priority",
            "type": "Element",
            "required": True,
        },
    )
    volume: Optional[float] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
            "required": True,
        },
    )
    pitch: Optional[float] = field(
        default=None,
        metadata={
            "name": "Pitch",
            "type": "Element",
            "required": True,
        },
    )
    spatial_reference: Optional[SpatialReference] = field(
        default=None,
        metadata={
            "name": "SpatialReference",
            "type": "Element",
            "required": True,
        },
    )
    reverb: Optional[ReverbType] = field(
        default=None,
        metadata={
            "name": "Reverb",
            "type": "Element",
            "required": True,
        },
    )
    bypass_reverb_zones: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BypassReverbZones",
            "type": "Element",
            "required": True,
        },
    )
    spatial_settings: Optional[SpatialSoundData] = field(
        default=None,
        metadata={
            "name": "SpatialSettings",
            "type": "Element",
        },
    )
    local_mixer_group: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocalMixerGroup",
            "type": "Element",
        },
    )
    external_mixer_group: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExternalMixerGroup",
            "type": "Element",
        },
    )
    vacuum_mixer_group: Optional[str] = field(
        default=None,
        metadata={
            "name": "VacuumMixerGroup",
            "type": "Element",
        },
    )
    occluded_mixer_group: Optional[str] = field(
        default=None,
        metadata={
            "name": "OccludedMixerGroup",
            "type": "Element",
        },
    )
    occlusion_type: Optional[OcclusionType] = field(
        default=None,
        metadata={
            "name": "OcclusionType",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ChargeAction(ActionData):
    state: Optional[BatteryCellState] = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Color(ColorRgb):
    class Meta:
        nillable = True


@dataclass
class Color32Reference(ColorReference):
    r: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    g: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    b: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    a: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ColorFloat4Reference(ColorReference):
    r: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    g: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    b: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    a: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ColorPower(ColorRgb):
    power: Optional[float] = field(
        default=None,
        metadata={
            "name": "Power",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ConditionComparable(ConditionData):
    compare: Optional[CompareOperator] = field(
        default=None,
        metadata={
            "name": "Compare",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ContainsConditionData(RoomRuleConditionData):
    prefab: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prefab",
            "type": "Attribute",
        },
    )


@dataclass
class ControllerData:
    controller_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName",
            "type": "Element",
        },
    )
    controller: Optional[Controller] = field(
        default=None,
        metadata={
            "name": "Controller",
            "type": "Element",
            "required": True,
        },
    )
    axis: Optional[ControllerAxis] = field(
        default=None,
        metadata={
            "name": "Axis",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class CursorThingCondition(ConditionData):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass
class CustomNameCondition(ConditionData):
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
        },
    )


@dataclass
class DelayedAction(ActionData):
    delay: Optional[TimeSpanReference] = field(
        default=None,
        metadata={
            "name": "Delay",
            "type": "Element",
        },
    )


@dataclass
class DynamicThingModData(ThingModData):
    atmosphere_dampening_scale: Optional[float] = field(
        default=None,
        metadata={
            "name": "AtmosphereDampeningScale",
            "type": "Element",
            "required": True,
        },
    )
    trade_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "TradeValue",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class EnumReferenceOfEntityState:
    value: Optional[EntityState] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Environment(SlotCondition):
    type_value: Optional[SpeciesClass] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class FilterReference:
    prefab_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrefabName",
            "type": "Element",
        },
    )
    slot_type: Optional[Class] = field(
        default=None,
        metadata={
            "name": "SlotType",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class GameAudioClipsData:
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    channel_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChannelName",
            "type": "Element",
        },
    )
    looping: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Looping",
            "type": "Element",
            "required": True,
        },
    )
    looping_one_shots: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LoopingOneShots",
            "type": "Element",
            "required": True,
        },
    )
    random_start_time: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RandomStartTime",
            "type": "Element",
            "required": True,
        },
    )
    random_pitch: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RandomPitch",
            "type": "Element",
            "required": True,
        },
    )
    random_pitch_range_high: Optional[float] = field(
        default=None,
        metadata={
            "name": "RandomPitchRangeHigh",
            "type": "Element",
            "required": True,
        },
    )
    random_pitch_range_low: Optional[float] = field(
        default=None,
        metadata={
            "name": "RandomPitchRangeLow",
            "type": "Element",
            "required": True,
        },
    )
    delay: Optional[float] = field(
        default=None,
        metadata={
            "name": "Delay",
            "type": "Element",
            "required": True,
        },
    )
    fade_in: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FadeIn",
            "type": "Element",
            "required": True,
        },
    )
    fade_out: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FadeOut",
            "type": "Element",
            "required": True,
        },
    )
    fade_down: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FadeDown",
            "type": "Element",
            "required": True,
        },
    )
    fade_down_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "FadeDownTime",
            "type": "Element",
            "required": True,
        },
    )
    fade_down_target: Optional[float] = field(
        default=None,
        metadata={
            "name": "FadeDownTarget",
            "type": "Element",
            "required": True,
        },
    )
    fade_pitch: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FadePitch",
            "type": "Element",
            "required": True,
        },
    )
    fade_in_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "FadeInTime",
            "type": "Element",
            "required": True,
        },
    )
    fade_out_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "FadeOutTime",
            "type": "Element",
            "required": True,
        },
    )
    clip_names: Optional[ArrayOfString4] = field(
        default=None,
        metadata={
            "name": "ClipNames",
            "type": "Element",
        },
    )
    concurrency_settings: Optional[ArrayOfString5] = field(
        default=None,
        metadata={
            "name": "ConcurrencySettings",
            "type": "Element",
        },
    )


@dataclass
class GasAction(ActionData):
    type_value: list[GasTypeValue] = field(
        default_factory=list,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "tokens": True,
        },
    )
    moles: Optional[float] = field(
        default=None,
        metadata={
            "name": "Moles",
            "type": "Attribute",
            "required": True,
        },
    )
    litres: Optional[float] = field(
        default=None,
        metadata={
            "name": "Litres",
            "type": "Attribute",
            "required": True,
        },
    )
    celsius: Optional[float] = field(
        default=None,
        metadata={
            "name": "Celsius",
            "type": "Attribute",
            "required": True,
        },
    )
    kelvin: Optional[float] = field(
        default=None,
        metadata={
            "name": "Kelvin",
            "type": "Attribute",
            "required": True,
        },
    )
    energy: Optional[float] = field(
        default=None,
        metadata={
            "name": "Energy",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class GasPressureData:
    type_value: list[GasTypeValue] = field(
        default_factory=list,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "tokens": True,
        },
    )
    partial_pressure: Optional[float] = field(
        default=None,
        metadata={
            "name": "PartialPressure",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class GasQuantityData:
    type_value: list[GasTypeValue] = field(
        default_factory=list,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "tokens": True,
        },
    )
    moles: Optional[float] = field(
        default=None,
        metadata={
            "name": "Moles",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Gene(GeneWrapper):
    class Meta:
        nillable = True


@dataclass
class GeneAction(ActionData):
    id: Optional[Gene1] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class GlobalGasMixSaveData:
    oxygen: Optional[DoubleReference] = field(
        default=None,
        metadata={
            "name": "Oxygen",
            "type": "Element",
        },
    )
    nitrogen: Optional[DoubleReference] = field(
        default=None,
        metadata={
            "name": "Nitrogen",
            "type": "Element",
        },
    )
    carbon_dioxide: Optional[DoubleReference] = field(
        default=None,
        metadata={
            "name": "CarbonDioxide",
            "type": "Element",
        },
    )
    volatiles: Optional[DoubleReference] = field(
        default=None,
        metadata={
            "name": "Volatiles",
            "type": "Element",
        },
    )
    pollutant: Optional[DoubleReference] = field(
        default=None,
        metadata={
            "name": "Pollutant",
            "type": "Element",
        },
    )
    water: Optional[DoubleReference] = field(
        default=None,
        metadata={
            "name": "Water",
            "type": "Element",
        },
    )
    polluted_water: Optional[DoubleReference] = field(
        default=None,
        metadata={
            "name": "PollutedWater",
            "type": "Element",
        },
    )
    nitrous_oxide: Optional[DoubleReference] = field(
        default=None,
        metadata={
            "name": "NitrousOxide",
            "type": "Element",
        },
    )
    liquid_nitrogen: Optional[DoubleReference] = field(
        default=None,
        metadata={
            "name": "LiquidNitrogen",
            "type": "Element",
        },
    )
    liquid_oxygen: Optional[DoubleReference] = field(
        default=None,
        metadata={
            "name": "LiquidOxygen",
            "type": "Element",
        },
    )
    liquid_volatiles: Optional[DoubleReference] = field(
        default=None,
        metadata={
            "name": "LiquidVolatiles",
            "type": "Element",
        },
    )
    steam: Optional[DoubleReference] = field(
        default=None,
        metadata={
            "name": "Steam",
            "type": "Element",
        },
    )
    liquid_carbon_dioxide: Optional[DoubleReference] = field(
        default=None,
        metadata={
            "name": "LiquidCarbonDioxide",
            "type": "Element",
        },
    )
    liquid_pollutant: Optional[DoubleReference] = field(
        default=None,
        metadata={
            "name": "LiquidPollutant",
            "type": "Element",
        },
    )
    liquid_nitrous_oxide: Optional[DoubleReference] = field(
        default=None,
        metadata={
            "name": "LiquidNitrousOxide",
            "type": "Element",
        },
    )
    hydrogen: Optional[DoubleReference] = field(
        default=None,
        metadata={
            "name": "Hydrogen",
            "type": "Element",
        },
    )
    liquid_hydrogen: Optional[DoubleReference] = field(
        default=None,
        metadata={
            "name": "LiquidHydrogen",
            "type": "Element",
        },
    )
    volume: Optional[DoubleReference] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
        },
    )


@dataclass
class GlobalMoleData:
    type_value: list[GasTypeValue] = field(
        default_factory=list,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "tokens": True,
        },
    )
    quantity: Optional[float] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class GlobalTemperatureFloatOffset(GlobalTemperatureOffsetData):
    day: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "Day",
            "type": "Element",
        },
    )
    night: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "Night",
            "type": "Element",
        },
    )


@dataclass
class GradientColorKey:
    color: Optional[Color1] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    time: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class GradientColorKeyData:
    color: Optional[Color1] = field(
        default=None,
        metadata={
            "name": "Color",
            "type": "Element",
            "required": True,
        },
    )
    time: Optional[float] = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class InCellCondition(ConditionData):
    x: Optional[int] = field(
        default=None,
        metadata={
            "name": "X",
            "type": "Attribute",
            "required": True,
        },
    )
    y: Optional[int] = field(
        default=None,
        metadata={
            "name": "Y",
            "type": "Attribute",
            "required": True,
        },
    )
    z: Optional[int] = field(
        default=None,
        metadata={
            "name": "Z",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class InteractableCondition(ConditionData):
    action: Optional[InteractableType] = field(
        default=None,
        metadata={
            "name": "Action",
            "type": "Attribute",
            "required": True,
        },
    )
    state: Optional[int] = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class InventoryData(DynamicThingData):
    slot_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "SlotId",
            "type": "Element",
            "required": True,
        },
    )
    type_value: Optional[Class] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "required": True,
        },
    )
    stack_size: Optional[float] = field(
        default=None,
        metadata={
            "name": "StackSize",
            "type": "Element",
            "required": True,
        },
    )
    species_class: Optional[SpeciesClass] = field(
        default=None,
        metadata={
            "name": "SpeciesClass",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class JetPackModData(ThingModData):
    max_speed: Optional[float] = field(
        default=None,
        metadata={
            "name": "MaxSpeed",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class KeyItem:
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    key: Optional[KeyCode] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class KitMetaData(MessageBaseOfKitMetaData):
    body: Optional[str] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )
    head: Optional[str] = field(
        default=None,
        metadata={
            "name": "Head",
            "type": "Element",
        },
    )
    hair: Optional[str] = field(
        default=None,
        metadata={
            "name": "Hair",
            "type": "Element",
        },
    )
    eyes: Optional[str] = field(
        default=None,
        metadata={
            "name": "Eyes",
            "type": "Element",
        },
    )
    facial_hair: Optional[str] = field(
        default=None,
        metadata={
            "name": "FacialHair",
            "type": "Element",
        },
    )
    skin_colour: Optional[str] = field(
        default=None,
        metadata={
            "name": "SkinColour",
            "type": "Element",
        },
    )
    eye_colour: Optional[str] = field(
        default=None,
        metadata={
            "name": "EyeColour",
            "type": "Element",
        },
    )
    hair_colours: Optional[ArrayOfString3] = field(
        default=None,
        metadata={
            "name": "HairColours",
            "type": "Element",
        },
    )


@dataclass
class LocalizedStringReference(StringReference):
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    color: Optional[str] = field(
        default=None,
        metadata={
            "name": "Color",
            "type": "Attribute",
        },
    )


@dataclass
class LogicActionSave:
    device_reference_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "DeviceReferenceId",
            "type": "Element",
            "required": True,
        },
    )
    type_value: Optional[LogicType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "required": True,
        },
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LogicConditionSave:
    device_reference_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "DeviceReferenceId",
            "type": "Element",
            "required": True,
        },
    )
    type_value: Optional[LogicType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "required": True,
        },
    )
    operation: Optional[ConditionOperation] = field(
        default=None,
        metadata={
            "name": "Operation",
            "type": "Element",
            "required": True,
        },
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )
    is_disconnected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsDisconnected",
            "type": "Element",
            "required": True,
        },
    )
    is_true: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsTrue",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LogicStackItemData(DoubleReference):
    index: Optional[int] = field(
        default=None,
        metadata={
            "name": "Index",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class LogicValueAction(ActionData):
    type_value: Optional[LogicType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class MapDisplayData:
    icon: Optional[NodeIcon] = field(
        default=None,
        metadata={
            "name": "Icon",
            "type": "Element",
        },
    )
    offset: Optional[Vector2Reference] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
        },
    )
    dynamic_panel: Optional[DynamicPanelData] = field(
        default=None,
        metadata={
            "name": "DynamicPanel",
            "type": "Element",
        },
    )
    x: Optional[int] = field(
        default=None,
        metadata={
            "name": "X",
            "type": "Attribute",
            "required": True,
        },
    )
    y: Optional[int] = field(
        default=None,
        metadata={
            "name": "Y",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class MapNodeReference(SerializedReferenceId):
    parent: Optional[SerializedReferenceId] = field(
        default=None,
        metadata={
            "name": "Parent",
            "type": "Element",
        },
    )


@dataclass
class Material(MaterialReference):
    class Meta:
        nillable = True


@dataclass
class ModAbout:
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    author: Optional[str] = field(
        default=None,
        metadata={
            "name": "Author",
            "type": "Element",
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Element",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
        },
    )
    workshop_handle: Optional[int] = field(
        default=None,
        metadata={
            "name": "WorkshopHandle",
            "type": "Element",
            "required": True,
        },
    )
    tags: Optional[ArrayOfString] = field(
        default=None,
        metadata={
            "name": "Tags",
            "type": "Element",
        },
    )


@dataclass
class Mole:
    read_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReadOnly",
            "type": "Element",
            "required": True,
        },
    )
    is_cachable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsCachable",
            "type": "Element",
            "required": True,
        },
    )
    quantity_dirty: Optional[bool] = field(
        default=None,
        metadata={
            "name": "QuantityDirty",
            "type": "Element",
            "required": True,
        },
    )
    energy_dirty: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EnergyDirty",
            "type": "Element",
            "required": True,
        },
    )
    energy: Optional[MoleEnergy] = field(
        default=None,
        metadata={
            "name": "Energy",
            "type": "Element",
            "required": True,
        },
    )
    quantity: Optional[MoleQuantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class MoleMixture:
    oxygen: Optional[float] = field(
        default=None,
        metadata={
            "name": "Oxygen",
            "type": "Element",
            "required": True,
        },
    )
    nitrogen: Optional[float] = field(
        default=None,
        metadata={
            "name": "Nitrogen",
            "type": "Element",
            "required": True,
        },
    )
    carbon_dioxide: Optional[float] = field(
        default=None,
        metadata={
            "name": "CarbonDioxide",
            "type": "Element",
            "required": True,
        },
    )
    volatiles: Optional[float] = field(
        default=None,
        metadata={
            "name": "Volatiles",
            "type": "Element",
            "required": True,
        },
    )
    pollutant: Optional[float] = field(
        default=None,
        metadata={
            "name": "Pollutant",
            "type": "Element",
            "required": True,
        },
    )
    water: Optional[float] = field(
        default=None,
        metadata={
            "name": "Water",
            "type": "Element",
            "required": True,
        },
    )
    polluted_water: Optional[float] = field(
        default=None,
        metadata={
            "name": "PollutedWater",
            "type": "Element",
            "required": True,
        },
    )
    nitrous_oxide: Optional[float] = field(
        default=None,
        metadata={
            "name": "NitrousOxide",
            "type": "Element",
            "required": True,
        },
    )
    liquid_nitrogen: Optional[float] = field(
        default=None,
        metadata={
            "name": "LiquidNitrogen",
            "type": "Element",
            "required": True,
        },
    )
    liquid_oxygen: Optional[float] = field(
        default=None,
        metadata={
            "name": "LiquidOxygen",
            "type": "Element",
            "required": True,
        },
    )
    liquid_volatiles: Optional[float] = field(
        default=None,
        metadata={
            "name": "LiquidVolatiles",
            "type": "Element",
            "required": True,
        },
    )
    steam: Optional[float] = field(
        default=None,
        metadata={
            "name": "Steam",
            "type": "Element",
            "required": True,
        },
    )
    liquid_carbon_dioxide: Optional[float] = field(
        default=None,
        metadata={
            "name": "LiquidCarbonDioxide",
            "type": "Element",
            "required": True,
        },
    )
    liquid_pollutant: Optional[float] = field(
        default=None,
        metadata={
            "name": "LiquidPollutant",
            "type": "Element",
            "required": True,
        },
    )
    liquid_nitrous_oxide: Optional[float] = field(
        default=None,
        metadata={
            "name": "LiquidNitrousOxide",
            "type": "Element",
            "required": True,
        },
    )
    hydrogen: Optional[float] = field(
        default=None,
        metadata={
            "name": "Hydrogen",
            "type": "Element",
            "required": True,
        },
    )
    liquid_hydrogen: Optional[float] = field(
        default=None,
        metadata={
            "name": "LiquidHydrogen",
            "type": "Element",
            "required": True,
        },
    )
    rule: Optional[MixRule] = field(
        default=None,
        metadata={
            "name": "Rule",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class MovePlayerAction(ActionData):
    slot_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SlotId",
            "type": "Attribute",
        },
    )
    slot_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "SlotIndex",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class NetworkCondition(ConditionData):
    type_value: Optional[StructureNetworkType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Object:
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    hide_flags: list[HideFlagsValue] = field(
        default_factory=list,
        metadata={
            "name": "hideFlags",
            "type": "Element",
            "tokens": True,
        },
    )


@dataclass
class Objective(WorldObjectiveSaveData):
    class Meta:
        nillable = True


@dataclass
class ObjectiveCompleteCondition(ConditionData):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass
class OrbitSimulationSaveData:
    accumulated_time: Optional[DoubleReference] = field(
        default=None,
        metadata={
            "name": "AccumulatedTime",
            "type": "Element",
        },
    )
    simulation_time: Optional[DoubleReference] = field(
        default=None,
        metadata={
            "name": "SimulationTime",
            "type": "Element",
        },
    )


@dataclass
class OrganicReagent(Reagent):
    pass


@dataclass
class PercentAction(ActionData):
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Plane(SlotCondition):
    type_value: Optional[ShuttleType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class PlanetPrefab:
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    position: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "Position",
            "type": "Element",
            "required": True,
        },
    )
    rotation: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "Rotation",
            "type": "Element",
            "required": True,
        },
    )
    scale: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "Scale",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class PlantStageData:
    mesh: Optional[MeshReference] = field(
        default=None,
        metadata={
            "name": "Mesh",
            "type": "Element",
        },
    )
    length: Optional[float] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Attribute",
            "required": True,
        },
    )
    mature: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Mature",
            "type": "Attribute",
            "required": True,
        },
    )
    seeding: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Seeding",
            "type": "Attribute",
            "required": True,
        },
    )
    dead: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Dead",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class PlantStatusCondition(ConditionData):
    status: Optional[PlantStatusType] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class PlayerCookie(PlayerCookieSaveDataV1):
    class Meta:
        nillable = True


@dataclass
class PreSpawnedCondition(ConditionData):
    value: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class QuantityAction(ActionData):
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Quaternion:
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    y: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    z: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    w: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    euler_angles: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "eulerAngles",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RandomPool(RandomPoolData):
    class Meta:
        nillable = True


@dataclass
class Range(ValueRange):
    class Meta:
        nillable = True


@dataclass
class RecordThing(Record):
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
        },
    )


@dataclass
class RegionCondition(ConditionData):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass
class ResearchPodData:
    research_type: Optional[ResearchPodType] = field(
        default=None,
        metadata={
            "name": "ResearchType",
            "type": "Element",
            "required": True,
        },
    )
    quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RocketSaveData(ReferencableSaveData):
    rocket_network_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "RocketNetworkId",
            "type": "Element",
            "required": True,
        },
    )
    progress: Optional[float] = field(
        default=None,
        metadata={
            "name": "Progress",
            "type": "Element",
            "required": True,
        },
    )
    target_node_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "TargetNodeId",
            "type": "Element",
            "required": True,
        },
    )
    current_node_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "CurrentNodeId",
            "type": "Element",
            "required": True,
        },
    )
    custom_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomName",
            "type": "Element",
        },
    )
    rocket_state: Optional[RocketState] = field(
        default=None,
        metadata={
            "name": "RocketState",
            "type": "Element",
            "required": True,
        },
    )
    rocket_mode: Optional[RocketMode] = field(
        default=None,
        metadata={
            "name": "RocketMode",
            "type": "Element",
            "required": True,
        },
    )
    re_entry_profile: Optional[ReEntryProfile] = field(
        default=None,
        metadata={
            "name": "ReEntryProfile",
            "type": "Element",
            "required": True,
        },
    )
    has_parent_transform: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasParentTransform",
            "type": "Element",
            "required": True,
        },
    )
    rocket_transform_position: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "RocketTransformPosition",
            "type": "Element",
            "required": True,
        },
    )
    parented_position: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "ParentedPosition",
            "type": "Element",
            "required": True,
        },
    )
    target_position: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "TargetPosition",
            "type": "Element",
            "required": True,
        },
    )
    park_location: Optional[Vector2Int] = field(
        default=None,
        metadata={
            "name": "ParkLocation",
            "type": "Element",
            "required": True,
        },
    )
    velocity: Optional[float] = field(
        default=None,
        metadata={
            "name": "Velocity",
            "type": "Element",
            "required": True,
        },
    )
    acceleration: Optional[float] = field(
        default=None,
        metadata={
            "name": "Acceleration",
            "type": "Element",
            "required": True,
        },
    )
    auto_shut_off: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AutoShutOff",
            "type": "Element",
            "required": True,
        },
    )
    auto_land: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AutoLand",
            "type": "Element",
            "required": True,
        },
    )
    max_recorded_thrust: Optional[float] = field(
        default=None,
        metadata={
            "name": "MaxRecordedThrust",
            "type": "Element",
            "required": True,
        },
    )
    orbital_position: Optional[float] = field(
        default=None,
        metadata={
            "name": "OrbitalPosition",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RoomCondition(ConditionData):
    room_type: Optional[RoomType] = field(
        default=None,
        metadata={
            "name": "RoomType",
            "type": "Attribute",
            "required": True,
        },
    )
    min_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinSize",
            "type": "Attribute",
            "required": True,
        },
    )
    max_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxSize",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SeekDepthData(SeekData):
    value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SeekSurfaceData(SeekData):
    pass


@dataclass
class SellSaveData(TransactionSaveData):
    stock: Optional[int] = field(
        default=None,
        metadata={
            "name": "Stock",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SetReagents(ActionData):
    flour: Optional[float] = field(
        default=None,
        metadata={
            "name": "Flour",
            "type": "Attribute",
            "required": True,
        },
    )
    milk: Optional[float] = field(
        default=None,
        metadata={
            "name": "Milk",
            "type": "Attribute",
            "required": True,
        },
    )
    egg: Optional[float] = field(
        default=None,
        metadata={
            "name": "Egg",
            "type": "Attribute",
            "required": True,
        },
    )
    iron: Optional[float] = field(
        default=None,
        metadata={
            "name": "Iron",
            "type": "Attribute",
            "required": True,
        },
    )
    gold: Optional[float] = field(
        default=None,
        metadata={
            "name": "Gold",
            "type": "Attribute",
            "required": True,
        },
    )
    carbon: Optional[float] = field(
        default=None,
        metadata={
            "name": "Carbon",
            "type": "Attribute",
            "required": True,
        },
    )
    uranium: Optional[float] = field(
        default=None,
        metadata={
            "name": "Uranium",
            "type": "Attribute",
            "required": True,
        },
    )
    copper: Optional[float] = field(
        default=None,
        metadata={
            "name": "Copper",
            "type": "Attribute",
            "required": True,
        },
    )
    steel: Optional[float] = field(
        default=None,
        metadata={
            "name": "Steel",
            "type": "Attribute",
            "required": True,
        },
    )
    hydrocarbon: Optional[float] = field(
        default=None,
        metadata={
            "name": "Hydrocarbon",
            "type": "Attribute",
            "required": True,
        },
    )
    silver: Optional[float] = field(
        default=None,
        metadata={
            "name": "Silver",
            "type": "Attribute",
            "required": True,
        },
    )
    nickel: Optional[float] = field(
        default=None,
        metadata={
            "name": "Nickel",
            "type": "Attribute",
            "required": True,
        },
    )
    lead: Optional[float] = field(
        default=None,
        metadata={
            "name": "Lead",
            "type": "Attribute",
            "required": True,
        },
    )
    electrum: Optional[float] = field(
        default=None,
        metadata={
            "name": "Electrum",
            "type": "Attribute",
            "required": True,
        },
    )
    invar: Optional[float] = field(
        default=None,
        metadata={
            "name": "Invar",
            "type": "Attribute",
            "required": True,
        },
    )
    constantan: Optional[float] = field(
        default=None,
        metadata={
            "name": "Constantan",
            "type": "Attribute",
            "required": True,
        },
    )
    solder: Optional[float] = field(
        default=None,
        metadata={
            "name": "Solder",
            "type": "Attribute",
            "required": True,
        },
    )
    plastic: Optional[float] = field(
        default=None,
        metadata={
            "name": "Plastic",
            "type": "Attribute",
            "required": True,
        },
    )
    silicon: Optional[float] = field(
        default=None,
        metadata={
            "name": "Silicon",
            "type": "Attribute",
            "required": True,
        },
    )
    salicylic_acid: Optional[float] = field(
        default=None,
        metadata={
            "name": "SalicylicAcid",
            "type": "Attribute",
            "required": True,
        },
    )
    alcohol: Optional[float] = field(
        default=None,
        metadata={
            "name": "Alcohol",
            "type": "Attribute",
            "required": True,
        },
    )
    oil: Optional[float] = field(
        default=None,
        metadata={
            "name": "Oil",
            "type": "Attribute",
            "required": True,
        },
    )
    potato: Optional[float] = field(
        default=None,
        metadata={
            "name": "Potato",
            "type": "Attribute",
            "required": True,
        },
    )
    tomato: Optional[float] = field(
        default=None,
        metadata={
            "name": "Tomato",
            "type": "Attribute",
            "required": True,
        },
    )
    fenoxitone: Optional[float] = field(
        default=None,
        metadata={
            "name": "Fenoxitone",
            "type": "Attribute",
            "required": True,
        },
    )
    color_red: Optional[float] = field(
        default=None,
        metadata={
            "name": "ColorRed",
            "type": "Attribute",
            "required": True,
        },
    )
    color_green: Optional[float] = field(
        default=None,
        metadata={
            "name": "ColorGreen",
            "type": "Attribute",
            "required": True,
        },
    )
    color_blue: Optional[float] = field(
        default=None,
        metadata={
            "name": "ColorBlue",
            "type": "Attribute",
            "required": True,
        },
    )
    color_yellow: Optional[float] = field(
        default=None,
        metadata={
            "name": "ColorYellow",
            "type": "Attribute",
            "required": True,
        },
    )
    color_orange: Optional[float] = field(
        default=None,
        metadata={
            "name": "ColorOrange",
            "type": "Attribute",
            "required": True,
        },
    )
    pumpkin: Optional[float] = field(
        default=None,
        metadata={
            "name": "Pumpkin",
            "type": "Attribute",
            "required": True,
        },
    )
    rice: Optional[float] = field(
        default=None,
        metadata={
            "name": "Rice",
            "type": "Attribute",
            "required": True,
        },
    )
    waspaloy: Optional[float] = field(
        default=None,
        metadata={
            "name": "Waspaloy",
            "type": "Attribute",
            "required": True,
        },
    )
    stellite: Optional[float] = field(
        default=None,
        metadata={
            "name": "Stellite",
            "type": "Attribute",
            "required": True,
        },
    )
    inconel: Optional[float] = field(
        default=None,
        metadata={
            "name": "Inconel",
            "type": "Attribute",
            "required": True,
        },
    )
    hastelloy: Optional[float] = field(
        default=None,
        metadata={
            "name": "Hastelloy",
            "type": "Attribute",
            "required": True,
        },
    )
    astroloy: Optional[float] = field(
        default=None,
        metadata={
            "name": "Astroloy",
            "type": "Attribute",
            "required": True,
        },
    )
    cobalt: Optional[float] = field(
        default=None,
        metadata={
            "name": "Cobalt",
            "type": "Attribute",
            "required": True,
        },
    )
    corn: Optional[float] = field(
        default=None,
        metadata={
            "name": "Corn",
            "type": "Attribute",
            "required": True,
        },
    )
    wheat: Optional[float] = field(
        default=None,
        metadata={
            "name": "Wheat",
            "type": "Attribute",
            "required": True,
        },
    )
    biomass: Optional[float] = field(
        default=None,
        metadata={
            "name": "Biomass",
            "type": "Attribute",
            "required": True,
        },
    )
    soy: Optional[float] = field(
        default=None,
        metadata={
            "name": "Soy",
            "type": "Attribute",
            "required": True,
        },
    )
    mushroom: Optional[float] = field(
        default=None,
        metadata={
            "name": "Mushroom",
            "type": "Attribute",
            "required": True,
        },
    )
    sugar: Optional[float] = field(
        default=None,
        metadata={
            "name": "Sugar",
            "type": "Attribute",
            "required": True,
        },
    )
    cocoa: Optional[float] = field(
        default=None,
        metadata={
            "name": "Cocoa",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Shuttle(SlotCondition):
    type_value: Optional[ShuttleType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SmallerThanConditionData(RoomRuleConditionData):
    size: Optional[int] = field(
        default=None,
        metadata={
            "name": "Size",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SoundEffectCondition:
    type_value: Optional[InteractableType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "required": True,
        },
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SourceCodeAction(ActionData):
    text: Optional[str] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
        },
    )
    size: Optional[int] = field(
        default=None,
        metadata={
            "name": "Size",
            "type": "Element",
            "required": True,
        },
    )
    size_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "SizeText",
            "type": "Element",
        },
    )
    text_checksum: Optional[int] = field(
        default=None,
        metadata={
            "name": "TextChecksum",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SpaceMapNodeActionData:
    achievement: Optional[AchievementData] = field(
        default=None,
        metadata={
            "name": "Achievement",
            "type": "Element",
        },
    )
    repeating: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Repeating",
            "type": "Attribute",
            "required": True,
        },
    )
    difficulty: Optional[int] = field(
        default=None,
        metadata={
            "name": "Difficulty",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SpawnContentsData:
    gastype: list[GasTypeValue] = field(
        default_factory=list,
        metadata={
            "name": "Gastype",
            "type": "Element",
            "tokens": True,
        },
    )
    quantity: Optional[float] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SpawnGas(MessageBaseOfSpawnGas):
    type_value: list[GasTypeValue] = field(
        default_factory=list,
        metadata={
            "name": "Type",
            "type": "Element",
            "tokens": True,
        },
    )
    quantity: Optional[float] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        },
    )
    kelvin: Optional[float] = field(
        default=None,
        metadata={
            "name": "Kelvin",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SpawnPositionListData:
    transform: list[TransformData] = field(
        default_factory=list,
        metadata={
            "name": "Transform",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Species(ConditionData):
    id: Optional[SpeciesClass] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Star(StarData):
    class Meta:
        nillable = True


@dataclass
class StateWrapper:
    state: Optional[PlantStatusType] = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Element",
            "required": True,
        },
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class StockData(IntRangeData):
    bulk: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Bulk",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SurfaceCondition(ConditionData):
    value: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SurvivalPropertyAction(ActionData):
    type_value: Optional[EntitySurvivalProperty] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    percent: Optional[float] = field(
        default=None,
        metadata={
            "name": "Percent",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TemperatureRangeCondition(ConditionData):
    unit: Optional[TemperatureType] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Attribute",
            "required": True,
        },
    )
    min: Optional[float] = field(
        default=None,
        metadata={
            "name": "Min",
            "type": "Attribute",
            "required": True,
        },
    )
    max: Optional[float] = field(
        default=None,
        metadata={
            "name": "Max",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TextureReference:
    tiling: Optional[Vector2Reference] = field(
        default=None,
        metadata={
            "name": "Tiling",
            "type": "Element",
        },
    )
    path: Optional[str] = field(
        default=None,
        metadata={
            "name": "Path",
            "type": "Attribute",
        },
    )
    format: Optional[TextureFormat] = field(
        default=None,
        metadata={
            "name": "Format",
            "type": "Attribute",
            "required": True,
        },
    )
    linear: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Linear",
            "type": "Attribute",
            "required": True,
        },
    )
    mip_mapped: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MipMapped",
            "type": "Attribute",
            "required": True,
        },
    )
    load_type: Optional[TextureLoadType] = field(
        default=None,
        metadata={
            "name": "LoadType",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ThingPrefabCondition(ConditionData):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass
class TimeSpan(TimeSpanReference):
    class Meta:
        nillable = True


@dataclass
class TraderContactCondition(ConditionData):
    is_resolved: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsResolved",
            "type": "Attribute",
            "required": True,
        },
    )
    is_contacted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsContacted",
            "type": "Attribute",
            "required": True,
        },
    )
    is_landed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsLanded",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TraderCrashEventData(WorldEventData):
    pad_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "PadId",
            "type": "Element",
            "required": True,
        },
    )
    collision_object_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "CollisionObjectId",
            "type": "Element",
            "required": True,
        },
    )
    position: Optional[Float3] = field(
        default=None,
        metadata={
            "name": "Position",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class TraderEnteredRangeEventData(WorldEventData):
    pass


@dataclass
class TraderLeftRangeEventData(WorldEventData):
    pass


@dataclass
class TraderSlotTraderSelectData:
    id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Id",
            "type": "Element",
        },
    )
    operator: Optional[LogicOperator] = field(
        default=None,
        metadata={
            "name": "Operator",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TraderSlotWorldData:
    id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Id",
            "type": "Element",
        },
    )
    operator: Optional[LogicOperator] = field(
        default=None,
        metadata={
            "name": "Operator",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Ui:
    class Meta:
        name = "UI"

    window: list[Window] = field(
        default_factory=list,
        metadata={
            "name": "Window",
            "type": "Element",
        },
    )
    selected_button: Optional[int] = field(
        default=None,
        metadata={
            "name": "SelectedButton",
            "type": "Attribute",
            "required": True,
        },
    )
    active_hand_slot: Optional[int] = field(
        default=None,
        metadata={
            "name": "ActiveHandSlot",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Vector3Reference(Vector2Reference):
    z: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class VeinModifierData:
    depth: list[TreeDepthModifer] = field(
        default_factory=list,
        metadata={
            "name": "Depth",
            "type": "Element",
        },
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class WindowSaveData:
    slot_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "SlotId",
            "type": "Element",
            "required": True,
        },
    )
    string_hash: Optional[int] = field(
        default=None,
        metadata={
            "name": "StringHash",
            "type": "Element",
            "required": True,
        },
    )
    is_open: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsOpen",
            "type": "Element",
            "required": True,
        },
    )
    is_undocked: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsUndocked",
            "type": "Element",
            "required": True,
        },
    )
    position: Optional[Vector2] = field(
        default=None,
        metadata={
            "name": "Position",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class WorldConditionBase(SerializedId):
    pass


@dataclass
class Alcohol(OrganicReagent):
    pass


@dataclass
class AmbientLighting(AmbientLightingReference):
    class Meta:
        nillable = True


@dataclass
class AnimationCurveData:
    key: list[AnimCurveKey] = field(
        default_factory=list,
        metadata={
            "name": "Key",
            "type": "Element",
        },
    )


@dataclass
class AnyConditionData(RoomRuleConditionData):
    any: list[AnyConditionData] = field(
        default_factory=list,
        metadata={
            "name": "Any",
            "type": "Element",
        },
    )
    all: list[AllConditionData] = field(
        default_factory=list,
        metadata={
            "name": "All",
            "type": "Element",
        },
    )
    contains: list[ContainsConditionData] = field(
        default_factory=list,
        metadata={
            "name": "Contains",
            "type": "Element",
        },
    )
    smaller_than: list[SmallerThanConditionData] = field(
        default_factory=list,
        metadata={
            "name": "SmallerThan",
            "type": "Element",
        },
    )


@dataclass
class ArrayOfAirControlVent:
    active_vent: list[AirControlVent] = field(
        default_factory=list,
        metadata={
            "name": "ActiveVent",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfAtmosphereSaveData:
    atmosphere_save_data: list[AtmosphereSaveData] = field(
        default_factory=list,
        metadata={
            "name": "AtmosphereSaveData",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfBooleanStateWrapper:
    state: list[BooleanStateWrapper] = field(
        default_factory=list,
        metadata={
            "name": "State",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfBuySaveData:
    buy: list[BuySaveData] = field(
        default_factory=list,
        metadata={
            "name": "Buy",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfChannelData:
    channel: list[ChannelData] = field(
        default_factory=list,
        metadata={
            "name": "Channel",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfChoice1:
    trader_crash_event_data: list[TraderCrashEventData] = field(
        default_factory=list,
        metadata={
            "name": "TraderCrashEventData",
            "type": "Element",
            "nillable": True,
        },
    )
    trader_entered_range_event_data: list[TraderEnteredRangeEventData] = field(
        default_factory=list,
        metadata={
            "name": "TraderEnteredRangeEventData",
            "type": "Element",
            "nillable": True,
        },
    )
    trader_left_range_event_data: list[TraderLeftRangeEventData] = field(
        default_factory=list,
        metadata={
            "name": "TraderLeftRangeEventData",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfFilterReference:
    filter: list[FilterReference] = field(
        default_factory=list,
        metadata={
            "name": "Filter",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfGameAudioClipsData:
    clip: list[GameAudioClipsData] = field(
        default_factory=list,
        metadata={
            "name": "Clip",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfGradientColorKey:
    gradient_color_key: list[GradientColorKey] = field(
        default_factory=list,
        metadata={
            "name": "GradientColorKey",
            "type": "Element",
        },
    )


@dataclass
class ArrayOfInventoryData:
    inventory_data: list[InventoryData] = field(
        default_factory=list,
        metadata={
            "name": "InventoryData",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfKeyItem:
    key_item: list[KeyItem] = field(
        default_factory=list,
        metadata={
            "name": "KeyItem",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfLogicActionSave:
    action: list[LogicActionSave] = field(
        default_factory=list,
        metadata={
            "name": "Action",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfLogicConditionSave:
    condition: list[LogicConditionSave] = field(
        default_factory=list,
        metadata={
            "name": "Condition",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfPlanetPrefab:
    prefab: list[PlanetPrefab] = field(
        default_factory=list,
        metadata={
            "name": "Prefab",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfPlanetPrefab1:
    planet_prefab: list[PlanetPrefab] = field(
        default_factory=list,
        metadata={
            "name": "PlanetPrefab",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfRecordThing:
    record_thing: list[RecordThing] = field(
        default_factory=list,
        metadata={
            "name": "RecordThing",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfResearchPodData:
    pod_dat: list[ResearchPodData] = field(
        default_factory=list,
        metadata={
            "name": "PodDat",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfRocketSaveData:
    rocket_save_data: list[RocketSaveData] = field(
        default_factory=list,
        metadata={
            "name": "RocketSaveData",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfSellSaveData:
    sell: list[SellSaveData] = field(
        default_factory=list,
        metadata={
            "name": "Sell",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfSoundEffectCondition:
    condition: list[SoundEffectCondition] = field(
        default_factory=list,
        metadata={
            "name": "Condition",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfSpawnGas:
    spawn_gas: list[SpawnGas] = field(
        default_factory=list,
        metadata={
            "name": "SpawnGas",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfStateWrapper:
    state: list[StateWrapper] = field(
        default_factory=list,
        metadata={
            "name": "State",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfWindowSaveData:
    window_save_data: list[WindowSaveData] = field(
        default_factory=list,
        metadata={
            "name": "WindowSaveData",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class Astroloy(OrganicReagent):
    pass


@dataclass
class Biomass(OrganicReagent):
    pass


@dataclass
class BranchAttemptsData(VeinModifierData):
    pass


@dataclass
class Carbon(OrganicReagent):
    pass


@dataclass
class CelestialReference:
    name: Optional[LocalizedStringReference] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    hidden: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Hidden",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CelestialRotation(Vector3Reference):
    pass


@dataclass
class ChartData(SpaceMapNodeActionData):
    pass


@dataclass
class Cheese(OrganicReagent):
    pass


@dataclass
class CloudTextureReference(TextureReference):
    shadow: Optional[CloudShadowReference] = field(
        default=None,
        metadata={
            "name": "Shadow",
            "type": "Element",
        },
    )
    distortion: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "Distortion",
            "type": "Element",
        },
    )
    speed: Optional[float] = field(
        default=None,
        metadata={
            "name": "Speed",
            "type": "Attribute",
            "required": True,
        },
    )
    opacity: Optional[float] = field(
        default=None,
        metadata={
            "name": "Opacity",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Cobalt(OrganicReagent):
    pass


@dataclass
class Cocoa(OrganicReagent):
    pass


@dataclass
class ColorBlue(OrganicReagent):
    pass


@dataclass
class ColorGreen(OrganicReagent):
    pass


@dataclass
class ColorOrange(OrganicReagent):
    pass


@dataclass
class ColorRed(OrganicReagent):
    pass


@dataclass
class ColorYellow(OrganicReagent):
    pass


@dataclass
class ConditionCollection:
    plane: list[Plane] = field(
        default_factory=list,
        metadata={
            "name": "Plane",
            "type": "Element",
        },
    )
    shuttle: list[Shuttle] = field(
        default_factory=list,
        metadata={
            "name": "Shuttle",
            "type": "Element",
        },
    )
    environment: list[Environment] = field(
        default_factory=list,
        metadata={
            "name": "Environment",
            "type": "Element",
        },
    )
    weight: Optional[int] = field(
        default=None,
        metadata={
            "name": "Weight",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Constantan(OrganicReagent):
    pass


@dataclass
class Copper(OrganicReagent):
    pass


@dataclass
class Corn(OrganicReagent):
    pass


@dataclass
class CurrentState(BooleanStateWrapper):
    class Meta:
        nillable = True


@dataclass
class DataCollection:
    name: Optional[LocalizedStringReference] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass
class Decay(ConditionComparable):
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class DeployData(SpaceMapNodeActionData):
    type_value: Optional[DeployType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class DepositMaterialReagentMixData(SetReagents):
    weight: Optional[float] = field(
        default=None,
        metadata={
            "name": "Weight",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class DepthCondition(ConditionComparable):
    depth_attribute: Optional[float] = field(
        default=None,
        metadata={
            "name": "Depth",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Difficulty(ConditionComparable):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass
class DifficultySetting(SettingBase):
    name: Optional[LocalizedStringReference] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    description: Optional[LocalizedStringReference] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
        },
    )
    preview_button: Optional[TextureReference] = field(
        default=None,
        metadata={
            "name": "PreviewButton",
            "type": "Element",
        },
    )
    robot_battery_rate: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "RobotBatteryRate",
            "type": "Element",
        },
    )
    hunger_rate: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "HungerRate",
            "type": "Element",
        },
    )
    hydration_rate: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "HydrationRate",
            "type": "Element",
        },
    )
    jetpack_rate: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "JetpackRate",
            "type": "Element",
        },
    )
    breathing_rate: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "BreathingRate",
            "type": "Element",
        },
    )
    lung_damage_rate: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "LungDamageRate",
            "type": "Element",
        },
    )
    offline_metabolism: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "OfflineMetabolism",
            "type": "Element",
        },
    )
    mining_yield: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "MiningYield",
            "type": "Element",
        },
    )
    eat_while_helmet_closed: Optional[BoolReference] = field(
        default=None,
        metadata={
            "name": "EatWhileHelmetClosed",
            "type": "Element",
        },
    )
    drink_while_helmet_closed: Optional[BoolReference] = field(
        default=None,
        metadata={
            "name": "DrinkWhileHelmetClosed",
            "type": "Element",
        },
    )
    weather_lander_damage_rate: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "WeatherLanderDamageRate",
            "type": "Element",
        },
    )
    food_decay_rate: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "FoodDecayRate",
            "type": "Element",
        },
    )
    mood_rate: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "MoodRate",
            "type": "Element",
        },
    )
    hygiene_rate: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "HygieneRate",
            "type": "Element",
        },
    )
    starting_weather_multiplier: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "StartingWeatherMultiplier",
            "type": "Element",
        },
    )
    creative: Optional[BoolReference] = field(
        default=None,
        metadata={
            "name": "Creative",
            "type": "Element",
        },
    )
    space_map_distance_multiplier: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "SpaceMapDistanceMultiplier",
            "type": "Element",
        },
    )
    respawn_condition: Optional[SerializedId] = field(
        default=None,
        metadata={
            "name": "RespawnCondition",
            "type": "Element",
        },
    )
    achievements: Optional[BoolReference] = field(
        default=None,
        metadata={
            "name": "Achievements",
            "type": "Element",
        },
    )
    respawn_stress_time: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "RespawnStressTime",
            "type": "Element",
        },
    )
    respawn_stress_consumption_speed: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "RespawnStressConsumptionSpeed",
            "type": "Element",
        },
    )
    respawn_stress_tool_use_speed: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "RespawnStressToolUseSpeed",
            "type": "Element",
        },
    )
    respawn_stress_trade_penalty: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "RespawnStressTradePenalty",
            "type": "Element",
        },
    )
    good_hygiene_tool_speed_multiplier: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "GoodHygieneToolSpeedMultiplier",
            "type": "Element",
        },
    )
    mood_tool_speed_multiplier: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "MoodToolSpeedMultiplier",
            "type": "Element",
        },
    )
    default: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Default",
            "type": "Attribute",
            "required": True,
        },
    )
    hidden: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Hidden",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class DirectionalLightData:
    color: Optional[ColorFloat4Reference] = field(
        default=None,
        metadata={
            "name": "Color",
            "type": "Element",
        },
    )
    color32: Optional[Color32Reference] = field(
        default=None,
        metadata={
            "name": "Color32",
            "type": "Element",
        },
    )
    intensity: Optional[FloatRangeData] = field(
        default=None,
        metadata={
            "name": "Intensity",
            "type": "Element",
        },
    )
    frequency: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "Frequency",
            "type": "Element",
        },
    )


@dataclass
class Egg(OrganicReagent):
    pass


@dataclass
class Electrum(OrganicReagent):
    pass


@dataclass
class Energy(ConditionComparable):
    ratio: Optional[float] = field(
        default=None,
        metadata={
            "name": "Ratio",
            "type": "Attribute",
            "required": True,
        },
    )
    percent_attribute: Optional[float] = field(
        default=None,
        metadata={
            "name": "Percent",
            "type": "Attribute",
            "required": True,
        },
    )
    state: Optional[BatteryCellState] = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class EntityStateCondition(ConditionData):
    is_online: Optional[BoolReference] = field(
        default=None,
        metadata={
            "name": "IsOnline",
            "type": "Element",
        },
    )
    state: Optional[EnumReferenceOfEntityState] = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Element",
        },
    )


@dataclass
class Fenoxitone(OrganicReagent):
    pass


@dataclass
class Flour(OrganicReagent):
    pass


@dataclass
class FogData:
    color: Optional[ColorFloat4Reference] = field(
        default=None,
        metadata={
            "name": "Color",
            "type": "Element",
        },
    )
    color32: Optional[Color32Reference] = field(
        default=None,
        metadata={
            "name": "Color32",
            "type": "Element",
        },
    )
    start_distance: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartDistance",
            "type": "Attribute",
            "required": True,
        },
    )
    end_distance: Optional[float] = field(
        default=None,
        metadata={
            "name": "EndDistance",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class FresnelReference(ColorPower):
    rim_low: Optional[ColorRgb] = field(
        default=None,
        metadata={
            "name": "RimLow",
            "type": "Element",
        },
    )
    rim_high: Optional[ColorRgb] = field(
        default=None,
        metadata={
            "name": "RimHigh",
            "type": "Element",
        },
    )
    emission: Optional[float] = field(
        default=None,
        metadata={
            "name": "Emission",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class GasCondition(ConditionComparable):
    type_value: list[GasTypeValue] = field(
        default_factory=list,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "tokens": True,
        },
    )
    percent_attribute: Optional[int] = field(
        default=None,
        metadata={
            "name": "Percent",
            "type": "Attribute",
            "required": True,
        },
    )
    moles_attribute: Optional[int] = field(
        default=None,
        metadata={
            "name": "Moles",
            "type": "Attribute",
            "required": True,
        },
    )
    partial_pressure: Optional[float] = field(
        default=None,
        metadata={
            "name": "PartialPressure",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class GasMixture:
    oxygen: Optional[Mole] = field(
        default=None,
        metadata={
            "name": "Oxygen",
            "type": "Element",
            "required": True,
        },
    )
    nitrogen: Optional[Mole] = field(
        default=None,
        metadata={
            "name": "Nitrogen",
            "type": "Element",
            "required": True,
        },
    )
    carbon_dioxide: Optional[Mole] = field(
        default=None,
        metadata={
            "name": "CarbonDioxide",
            "type": "Element",
            "required": True,
        },
    )
    volatiles: Optional[Mole] = field(
        default=None,
        metadata={
            "name": "Volatiles",
            "type": "Element",
            "required": True,
        },
    )
    pollutant: Optional[Mole] = field(
        default=None,
        metadata={
            "name": "Pollutant",
            "type": "Element",
            "required": True,
        },
    )
    water: Optional[Mole] = field(
        default=None,
        metadata={
            "name": "Water",
            "type": "Element",
            "required": True,
        },
    )
    polluted_water: Optional[Mole] = field(
        default=None,
        metadata={
            "name": "PollutedWater",
            "type": "Element",
            "required": True,
        },
    )
    nitrous_oxide: Optional[Mole] = field(
        default=None,
        metadata={
            "name": "NitrousOxide",
            "type": "Element",
            "required": True,
        },
    )
    liquid_nitrogen: Optional[Mole] = field(
        default=None,
        metadata={
            "name": "LiquidNitrogen",
            "type": "Element",
            "required": True,
        },
    )
    liquid_oxygen: Optional[Mole] = field(
        default=None,
        metadata={
            "name": "LiquidOxygen",
            "type": "Element",
            "required": True,
        },
    )
    liquid_volatiles: Optional[Mole] = field(
        default=None,
        metadata={
            "name": "LiquidVolatiles",
            "type": "Element",
            "required": True,
        },
    )
    steam: Optional[Mole] = field(
        default=None,
        metadata={
            "name": "Steam",
            "type": "Element",
            "required": True,
        },
    )
    liquid_carbon_dioxide: Optional[Mole] = field(
        default=None,
        metadata={
            "name": "LiquidCarbonDioxide",
            "type": "Element",
            "required": True,
        },
    )
    liquid_pollutant: Optional[Mole] = field(
        default=None,
        metadata={
            "name": "LiquidPollutant",
            "type": "Element",
            "required": True,
        },
    )
    liquid_nitrous_oxide: Optional[Mole] = field(
        default=None,
        metadata={
            "name": "LiquidNitrousOxide",
            "type": "Element",
            "required": True,
        },
    )
    hydrogen: Optional[Mole] = field(
        default=None,
        metadata={
            "name": "Hydrogen",
            "type": "Element",
            "required": True,
        },
    )
    liquid_hydrogen: Optional[Mole] = field(
        default=None,
        metadata={
            "name": "LiquidHydrogen",
            "type": "Element",
            "required": True,
        },
    )
    total_energy: Optional[MoleEnergy] = field(
        default=None,
        metadata={
            "name": "TotalEnergy",
            "type": "Element",
            "required": True,
        },
    )
    is_cachable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsCachable",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class GasQuantityRatioData(GasQuantityData):
    ratio: Optional[float] = field(
        default=None,
        metadata={
            "name": "Ratio",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class GeneCollectionWrapper:
    plant_custom_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlantCustomName",
            "type": "Element",
        },
    )
    planter_custom_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlanterCustomName",
            "type": "Element",
        },
    )
    gene_wrappers: Optional[ArrayOfGeneWrapper] = field(
        default=None,
        metadata={
            "name": "GeneWrappers",
            "type": "Element",
        },
    )


@dataclass
class GlobalGasMixData:
    gas: list[GlobalMoleData] = field(
        default_factory=list,
        metadata={
            "name": "Gas",
            "type": "Element",
        },
    )


@dataclass
class Gold(OrganicReagent):
    pass


@dataclass
class GrowthStateCondition(ConditionComparable):
    value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )
    is_planted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsPlanted",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Hastelloy(OrganicReagent):
    pass


@dataclass
class Hydrocarbon(OrganicReagent):
    pass


@dataclass
class Inconel(OrganicReagent):
    pass


@dataclass
class InteractionAction(DelayedAction):
    type_value: Optional[InteractableType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Invar(OrganicReagent):
    pass


@dataclass
class Iron(OrganicReagent):
    pass


@dataclass
class Item(ThingPrefabCondition):
    slot_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SlotId",
            "type": "Attribute",
        },
    )
    slot_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "SlotIndex",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class LaunchPadNodeReference(MapNodeReference):
    is_orbital: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsOrbital",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class LavaData:
    height_texture: Optional[TextureReference] = field(
        default=None,
        metadata={
            "name": "HeightTexture",
            "type": "Element",
        },
    )
    min_height: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinHeight",
            "type": "Attribute",
            "required": True,
        },
    )
    max_height: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxHeight",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class LavaLakeProp:
    position: Optional[Vector3Reference] = field(
        default=None,
        metadata={
            "name": "Position",
            "type": "Element",
        },
    )
    rotation: Optional[Vector3Reference] = field(
        default=None,
        metadata={
            "name": "Rotation",
            "type": "Element",
        },
    )
    scale: Optional[Vector3Reference] = field(
        default=None,
        metadata={
            "name": "Scale",
            "type": "Element",
        },
    )


@dataclass
class Lead(OrganicReagent):
    pass


@dataclass
class LogicCondition(ConditionComparable):
    type_value: Optional[LogicType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class LogicStackData:
    stack: list[LogicStackItemData] = field(
        default_factory=list,
        metadata={
            "name": "Stack",
            "type": "Element",
        },
    )


@dataclass
class Milk(OrganicReagent):
    pass


@dataclass
class ModMetadata(ModAbout):
    class Meta:
        nillable = True


@dataclass
class Moles(ConditionComparable):
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class MomentumData(VeinModifierData):
    pass


@dataclass
class Mushroom(OrganicReagent):
    pass


@dataclass
class Nickel(OrganicReagent):
    pass


@dataclass
class Node(MapNodeReference):
    class Meta:
        nillable = True


@dataclass
class Oil(OrganicReagent):
    pass


@dataclass
class PendingSpawnAction:
    action: Optional[DelayedAction] = field(
        default=None,
        metadata={
            "name": "Action",
            "type": "Element",
        },
    )
    time_remaining: Optional[float] = field(
        default=None,
        metadata={
            "name": "TimeRemaining",
            "type": "Element",
            "required": True,
        },
    )
    thing: Optional[int] = field(
        default=None,
        metadata={
            "name": "Thing",
            "type": "Attribute",
            "required": True,
        },
    )
    player: Optional[int] = field(
        default=None,
        metadata={
            "name": "Player",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Percent(ConditionComparable):
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class PlanetaryAtmosphereSaveData:
    global_gas_mix: Optional[GlobalGasMixSaveData] = field(
        default=None,
        metadata={
            "name": "GlobalGasMix",
            "type": "Element",
        },
    )
    liquid_clouds: Optional[GlobalGasMixSaveData] = field(
        default=None,
        metadata={
            "name": "LiquidClouds",
            "type": "Element",
        },
    )
    ice_clouds: Optional[GlobalGasMixSaveData] = field(
        default=None,
        metadata={
            "name": "IceClouds",
            "type": "Element",
        },
    )
    ice_caps: Optional[GlobalGasMixSaveData] = field(
        default=None,
        metadata={
            "name": "IceCaps",
            "type": "Element",
        },
    )
    latent_energy_offset: Optional[DoubleReference] = field(
        default=None,
        metadata={
            "name": "LatentEnergyOffset",
            "type": "Element",
        },
    )
    energy_offset: Optional[DoubleReference] = field(
        default=None,
        metadata={
            "name": "EnergyOffset",
            "type": "Element",
        },
    )


@dataclass
class PlantRecordCondition(ConditionComparable):
    status: Optional[PlantStatusType] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class PlantSample:
    plant_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlantName",
            "type": "Element",
        },
    )
    genes: Optional[ArrayOfGeneWrapper] = field(
        default=None,
        metadata={
            "name": "Genes",
            "type": "Element",
        },
    )
    time_until_dehydration_damage: Optional[RequirementWrapper] = field(
        default=None,
        metadata={
            "name": "TimeUntilDehydrationDamage",
            "type": "Element",
            "required": True,
        },
    )
    time_until_undesired_gas_damage: Optional[RequirementWrapper] = field(
        default=None,
        metadata={
            "name": "TimeUntilUndesiredGasDamage",
            "type": "Element",
            "required": True,
        },
    )
    time_until_frozen_damage: Optional[RequirementWrapper] = field(
        default=None,
        metadata={
            "name": "TimeUntilFrozenDamage",
            "type": "Element",
            "required": True,
        },
    )
    time_until_over_heated_damage: Optional[RequirementWrapper] = field(
        default=None,
        metadata={
            "name": "TimeUntilOverHeatedDamage",
            "type": "Element",
            "required": True,
        },
    )
    time_until_suffocated_damage: Optional[RequirementWrapper] = field(
        default=None,
        metadata={
            "name": "TimeUntilSuffocatedDamage",
            "type": "Element",
            "required": True,
        },
    )
    time_until_low_pressure_damage: Optional[RequirementWrapper] = field(
        default=None,
        metadata={
            "name": "TimeUntilLowPressureDamage",
            "type": "Element",
            "required": True,
        },
    )
    time_until_high_pressure_damage: Optional[RequirementWrapper] = field(
        default=None,
        metadata={
            "name": "TimeUntilHighPressureDamage",
            "type": "Element",
            "required": True,
        },
    )
    light_per_day: Optional[RequirementWrapper] = field(
        default=None,
        metadata={
            "name": "LightPerDay",
            "type": "Element",
            "required": True,
        },
    )
    darkness_per_day: Optional[RequirementWrapper] = field(
        default=None,
        metadata={
            "name": "DarknessPerDay",
            "type": "Element",
            "required": True,
        },
    )
    time_until_light_damage: Optional[RequirementWrapper] = field(
        default=None,
        metadata={
            "name": "TimeUntilLightDamage",
            "type": "Element",
            "required": True,
        },
    )
    time_until_darkness_damage: Optional[RequirementWrapper] = field(
        default=None,
        metadata={
            "name": "TimeUntilDarknessDamage",
            "type": "Element",
            "required": True,
        },
    )
    water_usage: Optional[RequirementWrapper] = field(
        default=None,
        metadata={
            "name": "WaterUsage",
            "type": "Element",
            "required": True,
        },
    )
    gas_production: Optional[RequirementWrapper] = field(
        default=None,
        metadata={
            "name": "GasProduction",
            "type": "Element",
            "required": True,
        },
    )
    undesired_gas_resistance: Optional[RequirementWrapper] = field(
        default=None,
        metadata={
            "name": "UndesiredGasResistance",
            "type": "Element",
            "required": True,
        },
    )
    min_grow_temperature_c: Optional[RequirementWrapper] = field(
        default=None,
        metadata={
            "name": "MinGrowTemperatureC",
            "type": "Element",
            "required": True,
        },
    )
    min_ideal_grow_temperature_c: Optional[RequirementWrapper] = field(
        default=None,
        metadata={
            "name": "MinIdealGrowTemperatureC",
            "type": "Element",
            "required": True,
        },
    )
    max_grow_temperature_c: Optional[RequirementWrapper] = field(
        default=None,
        metadata={
            "name": "MaxGrowTemperatureC",
            "type": "Element",
            "required": True,
        },
    )
    max_ideal_grow_temperature_c: Optional[RequirementWrapper] = field(
        default=None,
        metadata={
            "name": "MaxIdealGrowTemperatureC",
            "type": "Element",
            "required": True,
        },
    )
    min_grow_pressure: Optional[RequirementWrapper] = field(
        default=None,
        metadata={
            "name": "MinGrowPressure",
            "type": "Element",
            "required": True,
        },
    )
    min_ideal_grow_pressure: Optional[RequirementWrapper] = field(
        default=None,
        metadata={
            "name": "MinIdealGrowPressure",
            "type": "Element",
            "required": True,
        },
    )
    max_grow_pressure: Optional[RequirementWrapper] = field(
        default=None,
        metadata={
            "name": "MaxGrowPressure",
            "type": "Element",
            "required": True,
        },
    )
    max_ideal_grow_pressure: Optional[RequirementWrapper] = field(
        default=None,
        metadata={
            "name": "MaxIdealGrowPressure",
            "type": "Element",
            "required": True,
        },
    )
    growth_speed_multiplier: Optional[RequirementWrapper] = field(
        default=None,
        metadata={
            "name": "GrowthSpeedMultiplier",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Plastic(OrganicReagent):
    pass


@dataclass
class PlayerCosmetics:
    species: Optional[SpeciesClass] = field(
        default=None,
        metadata={
            "name": "Species",
            "type": "Element",
            "required": True,
        },
    )
    species_class: Optional[SpeciesClass] = field(
        default=None,
        metadata={
            "name": "SpeciesClass",
            "type": "Element",
            "required": True,
        },
    )
    gender: Optional[Gender] = field(
        default=None,
        metadata={
            "name": "Gender",
            "type": "Element",
            "required": True,
        },
    )
    kit_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KitId",
            "type": "Element",
        },
    )
    meta_data: Optional[KitMetaData] = field(
        default=None,
        metadata={
            "name": "MetaData",
            "type": "Element",
        },
    )


@dataclass
class PopupAction(ActionData):
    title: Optional[LocalizedStringReference] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
        },
    )
    text: Optional[LocalizedStringReference] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
        },
    )
    delay: Optional[float] = field(
        default=None,
        metadata={
            "name": "Delay",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Potato(OrganicReagent):
    pass


@dataclass
class PressureCondition(ConditionComparable):
    k_pa: Optional[float] = field(
        default=None,
        metadata={
            "name": "kPa",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Pumpkin(OrganicReagent):
    pass


@dataclass
class Quantity(ConditionComparable):
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ReagentCondition(ConditionComparable):
    total: Optional[float] = field(
        default=None,
        metadata={
            "name": "Total",
            "type": "Attribute",
            "required": True,
        },
    )
    flour: Optional[float] = field(
        default=None,
        metadata={
            "name": "Flour",
            "type": "Attribute",
            "required": True,
        },
    )
    milk: Optional[float] = field(
        default=None,
        metadata={
            "name": "Milk",
            "type": "Attribute",
            "required": True,
        },
    )
    egg: Optional[float] = field(
        default=None,
        metadata={
            "name": "Egg",
            "type": "Attribute",
            "required": True,
        },
    )
    iron: Optional[float] = field(
        default=None,
        metadata={
            "name": "Iron",
            "type": "Attribute",
            "required": True,
        },
    )
    gold: Optional[float] = field(
        default=None,
        metadata={
            "name": "Gold",
            "type": "Attribute",
            "required": True,
        },
    )
    carbon: Optional[float] = field(
        default=None,
        metadata={
            "name": "Carbon",
            "type": "Attribute",
            "required": True,
        },
    )
    uranium: Optional[float] = field(
        default=None,
        metadata={
            "name": "Uranium",
            "type": "Attribute",
            "required": True,
        },
    )
    copper: Optional[float] = field(
        default=None,
        metadata={
            "name": "Copper",
            "type": "Attribute",
            "required": True,
        },
    )
    steel: Optional[float] = field(
        default=None,
        metadata={
            "name": "Steel",
            "type": "Attribute",
            "required": True,
        },
    )
    hydrocarbon: Optional[float] = field(
        default=None,
        metadata={
            "name": "Hydrocarbon",
            "type": "Attribute",
            "required": True,
        },
    )
    silver: Optional[float] = field(
        default=None,
        metadata={
            "name": "Silver",
            "type": "Attribute",
            "required": True,
        },
    )
    nickel: Optional[float] = field(
        default=None,
        metadata={
            "name": "Nickel",
            "type": "Attribute",
            "required": True,
        },
    )
    lead: Optional[float] = field(
        default=None,
        metadata={
            "name": "Lead",
            "type": "Attribute",
            "required": True,
        },
    )
    electrum: Optional[float] = field(
        default=None,
        metadata={
            "name": "Electrum",
            "type": "Attribute",
            "required": True,
        },
    )
    invar: Optional[float] = field(
        default=None,
        metadata={
            "name": "Invar",
            "type": "Attribute",
            "required": True,
        },
    )
    constantan: Optional[float] = field(
        default=None,
        metadata={
            "name": "Constantan",
            "type": "Attribute",
            "required": True,
        },
    )
    solder: Optional[float] = field(
        default=None,
        metadata={
            "name": "Solder",
            "type": "Attribute",
            "required": True,
        },
    )
    plastic: Optional[float] = field(
        default=None,
        metadata={
            "name": "Plastic",
            "type": "Attribute",
            "required": True,
        },
    )
    silicon: Optional[float] = field(
        default=None,
        metadata={
            "name": "Silicon",
            "type": "Attribute",
            "required": True,
        },
    )
    salicylic_acid: Optional[float] = field(
        default=None,
        metadata={
            "name": "SalicylicAcid",
            "type": "Attribute",
            "required": True,
        },
    )
    alcohol: Optional[float] = field(
        default=None,
        metadata={
            "name": "Alcohol",
            "type": "Attribute",
            "required": True,
        },
    )
    oil: Optional[float] = field(
        default=None,
        metadata={
            "name": "Oil",
            "type": "Attribute",
            "required": True,
        },
    )
    potato: Optional[float] = field(
        default=None,
        metadata={
            "name": "Potato",
            "type": "Attribute",
            "required": True,
        },
    )
    tomato: Optional[float] = field(
        default=None,
        metadata={
            "name": "Tomato",
            "type": "Attribute",
            "required": True,
        },
    )
    fenoxitone: Optional[float] = field(
        default=None,
        metadata={
            "name": "Fenoxitone",
            "type": "Attribute",
            "required": True,
        },
    )
    color_red: Optional[float] = field(
        default=None,
        metadata={
            "name": "ColorRed",
            "type": "Attribute",
            "required": True,
        },
    )
    color_green: Optional[float] = field(
        default=None,
        metadata={
            "name": "ColorGreen",
            "type": "Attribute",
            "required": True,
        },
    )
    color_blue: Optional[float] = field(
        default=None,
        metadata={
            "name": "ColorBlue",
            "type": "Attribute",
            "required": True,
        },
    )
    color_yellow: Optional[float] = field(
        default=None,
        metadata={
            "name": "ColorYellow",
            "type": "Attribute",
            "required": True,
        },
    )
    color_orange: Optional[float] = field(
        default=None,
        metadata={
            "name": "ColorOrange",
            "type": "Attribute",
            "required": True,
        },
    )
    pumpkin: Optional[float] = field(
        default=None,
        metadata={
            "name": "Pumpkin",
            "type": "Attribute",
            "required": True,
        },
    )
    rice: Optional[float] = field(
        default=None,
        metadata={
            "name": "Rice",
            "type": "Attribute",
            "required": True,
        },
    )
    waspaloy: Optional[float] = field(
        default=None,
        metadata={
            "name": "Waspaloy",
            "type": "Attribute",
            "required": True,
        },
    )
    stellite: Optional[float] = field(
        default=None,
        metadata={
            "name": "Stellite",
            "type": "Attribute",
            "required": True,
        },
    )
    inconel: Optional[float] = field(
        default=None,
        metadata={
            "name": "Inconel",
            "type": "Attribute",
            "required": True,
        },
    )
    hastelloy: Optional[float] = field(
        default=None,
        metadata={
            "name": "Hastelloy",
            "type": "Attribute",
            "required": True,
        },
    )
    astroloy: Optional[float] = field(
        default=None,
        metadata={
            "name": "Astroloy",
            "type": "Attribute",
            "required": True,
        },
    )
    cobalt: Optional[float] = field(
        default=None,
        metadata={
            "name": "Cobalt",
            "type": "Attribute",
            "required": True,
        },
    )
    corn: Optional[float] = field(
        default=None,
        metadata={
            "name": "Corn",
            "type": "Attribute",
            "required": True,
        },
    )
    wheat: Optional[float] = field(
        default=None,
        metadata={
            "name": "Wheat",
            "type": "Attribute",
            "required": True,
        },
    )
    biomass: Optional[float] = field(
        default=None,
        metadata={
            "name": "Biomass",
            "type": "Attribute",
            "required": True,
        },
    )
    soy: Optional[float] = field(
        default=None,
        metadata={
            "name": "Soy",
            "type": "Attribute",
            "required": True,
        },
    )
    mushroom: Optional[float] = field(
        default=None,
        metadata={
            "name": "Mushroom",
            "type": "Attribute",
            "required": True,
        },
    )
    sugar: Optional[float] = field(
        default=None,
        metadata={
            "name": "Sugar",
            "type": "Attribute",
            "required": True,
        },
    )
    cocoa: Optional[float] = field(
        default=None,
        metadata={
            "name": "Cocoa",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Recipe:
    flour: Optional[float] = field(
        default=None,
        metadata={
            "name": "Flour",
            "type": "Element",
            "required": True,
        },
    )
    milk: Optional[float] = field(
        default=None,
        metadata={
            "name": "Milk",
            "type": "Element",
            "required": True,
        },
    )
    egg: Optional[float] = field(
        default=None,
        metadata={
            "name": "Egg",
            "type": "Element",
            "required": True,
        },
    )
    iron: Optional[float] = field(
        default=None,
        metadata={
            "name": "Iron",
            "type": "Element",
            "required": True,
        },
    )
    gold: Optional[float] = field(
        default=None,
        metadata={
            "name": "Gold",
            "type": "Element",
            "required": True,
        },
    )
    carbon: Optional[float] = field(
        default=None,
        metadata={
            "name": "Carbon",
            "type": "Element",
            "required": True,
        },
    )
    uranium: Optional[float] = field(
        default=None,
        metadata={
            "name": "Uranium",
            "type": "Element",
            "required": True,
        },
    )
    copper: Optional[float] = field(
        default=None,
        metadata={
            "name": "Copper",
            "type": "Element",
            "required": True,
        },
    )
    steel: Optional[float] = field(
        default=None,
        metadata={
            "name": "Steel",
            "type": "Element",
            "required": True,
        },
    )
    hydrocarbon: Optional[float] = field(
        default=None,
        metadata={
            "name": "Hydrocarbon",
            "type": "Element",
            "required": True,
        },
    )
    silver: Optional[float] = field(
        default=None,
        metadata={
            "name": "Silver",
            "type": "Element",
            "required": True,
        },
    )
    nickel: Optional[float] = field(
        default=None,
        metadata={
            "name": "Nickel",
            "type": "Element",
            "required": True,
        },
    )
    lead: Optional[float] = field(
        default=None,
        metadata={
            "name": "Lead",
            "type": "Element",
            "required": True,
        },
    )
    electrum: Optional[float] = field(
        default=None,
        metadata={
            "name": "Electrum",
            "type": "Element",
            "required": True,
        },
    )
    invar: Optional[float] = field(
        default=None,
        metadata={
            "name": "Invar",
            "type": "Element",
            "required": True,
        },
    )
    constantan: Optional[float] = field(
        default=None,
        metadata={
            "name": "Constantan",
            "type": "Element",
            "required": True,
        },
    )
    solder: Optional[float] = field(
        default=None,
        metadata={
            "name": "Solder",
            "type": "Element",
            "required": True,
        },
    )
    plastic: Optional[float] = field(
        default=None,
        metadata={
            "name": "Plastic",
            "type": "Element",
            "required": True,
        },
    )
    silicon: Optional[float] = field(
        default=None,
        metadata={
            "name": "Silicon",
            "type": "Element",
            "required": True,
        },
    )
    salicylic_acid: Optional[float] = field(
        default=None,
        metadata={
            "name": "SalicylicAcid",
            "type": "Element",
            "required": True,
        },
    )
    alcohol: Optional[float] = field(
        default=None,
        metadata={
            "name": "Alcohol",
            "type": "Element",
            "required": True,
        },
    )
    oil: Optional[float] = field(
        default=None,
        metadata={
            "name": "Oil",
            "type": "Element",
            "required": True,
        },
    )
    potato: Optional[float] = field(
        default=None,
        metadata={
            "name": "Potato",
            "type": "Element",
            "required": True,
        },
    )
    tomato: Optional[float] = field(
        default=None,
        metadata={
            "name": "Tomato",
            "type": "Element",
            "required": True,
        },
    )
    fenoxitone: Optional[float] = field(
        default=None,
        metadata={
            "name": "Fenoxitone",
            "type": "Element",
            "required": True,
        },
    )
    color_red: Optional[float] = field(
        default=None,
        metadata={
            "name": "ColorRed",
            "type": "Element",
            "required": True,
        },
    )
    color_green: Optional[float] = field(
        default=None,
        metadata={
            "name": "ColorGreen",
            "type": "Element",
            "required": True,
        },
    )
    color_blue: Optional[float] = field(
        default=None,
        metadata={
            "name": "ColorBlue",
            "type": "Element",
            "required": True,
        },
    )
    color_yellow: Optional[float] = field(
        default=None,
        metadata={
            "name": "ColorYellow",
            "type": "Element",
            "required": True,
        },
    )
    color_orange: Optional[float] = field(
        default=None,
        metadata={
            "name": "ColorOrange",
            "type": "Element",
            "required": True,
        },
    )
    pumpkin: Optional[float] = field(
        default=None,
        metadata={
            "name": "Pumpkin",
            "type": "Element",
            "required": True,
        },
    )
    rice: Optional[float] = field(
        default=None,
        metadata={
            "name": "Rice",
            "type": "Element",
            "required": True,
        },
    )
    waspaloy: Optional[float] = field(
        default=None,
        metadata={
            "name": "Waspaloy",
            "type": "Element",
            "required": True,
        },
    )
    stellite: Optional[float] = field(
        default=None,
        metadata={
            "name": "Stellite",
            "type": "Element",
            "required": True,
        },
    )
    inconel: Optional[float] = field(
        default=None,
        metadata={
            "name": "Inconel",
            "type": "Element",
            "required": True,
        },
    )
    hastelloy: Optional[float] = field(
        default=None,
        metadata={
            "name": "Hastelloy",
            "type": "Element",
            "required": True,
        },
    )
    astroloy: Optional[float] = field(
        default=None,
        metadata={
            "name": "Astroloy",
            "type": "Element",
            "required": True,
        },
    )
    cobalt: Optional[float] = field(
        default=None,
        metadata={
            "name": "Cobalt",
            "type": "Element",
            "required": True,
        },
    )
    corn: Optional[float] = field(
        default=None,
        metadata={
            "name": "Corn",
            "type": "Element",
            "required": True,
        },
    )
    wheat: Optional[float] = field(
        default=None,
        metadata={
            "name": "Wheat",
            "type": "Element",
            "required": True,
        },
    )
    biomass: Optional[float] = field(
        default=None,
        metadata={
            "name": "Biomass",
            "type": "Element",
            "required": True,
        },
    )
    soy: Optional[float] = field(
        default=None,
        metadata={
            "name": "Soy",
            "type": "Element",
            "required": True,
        },
    )
    mushroom: Optional[float] = field(
        default=None,
        metadata={
            "name": "Mushroom",
            "type": "Element",
            "required": True,
        },
    )
    sugar: Optional[float] = field(
        default=None,
        metadata={
            "name": "Sugar",
            "type": "Element",
            "required": True,
        },
    )
    cocoa: Optional[float] = field(
        default=None,
        metadata={
            "name": "Cocoa",
            "type": "Element",
            "required": True,
        },
    )
    cheese: Optional[float] = field(
        default=None,
        metadata={
            "name": "Cheese",
            "type": "Element",
            "required": True,
        },
    )
    time: Optional[float] = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Element",
            "required": True,
        },
    )
    energy: Optional[float] = field(
        default=None,
        metadata={
            "name": "Energy",
            "type": "Element",
            "required": True,
        },
    )
    temperature: Optional[Temperature] = field(
        default=None,
        metadata={
            "name": "Temperature",
            "type": "Element",
            "required": True,
        },
    )
    pressure: Optional[Pressure] = field(
        default=None,
        metadata={
            "name": "Pressure",
            "type": "Element",
            "required": True,
        },
    )
    required_mix: Optional[MoleMixture] = field(
        default=None,
        metadata={
            "name": "RequiredMix",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Rice(OrganicReagent):
    pass


@dataclass
class RoomData:
    room_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "RoomId",
            "type": "Element",
            "required": True,
        },
    )
    will_save: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WillSave",
            "type": "Element",
            "required": True,
        },
    )
    grids: Optional[ArrayOfGrid3] = field(
        default=None,
        metadata={
            "name": "Grids",
            "type": "Element",
        },
    )


@dataclass
class RotatingCelestialBodySaveData(CelestialBodySaveData):
    axis: Optional[DoubleReference] = field(
        default=None,
        metadata={
            "name": "Axis",
            "type": "Element",
        },
    )


@dataclass
class SalicylicAcid(OrganicReagent):
    pass


@dataclass
class Silicon(OrganicReagent):
    pass


@dataclass
class Silver(OrganicReagent):
    pass


@dataclass
class SizeCondition(ConditionComparable):
    x: Optional[int] = field(
        default=None,
        metadata={
            "name": "X",
            "type": "Attribute",
            "required": True,
        },
    )
    y: Optional[int] = field(
        default=None,
        metadata={
            "name": "Y",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Solder(OrganicReagent):
    pass


@dataclass
class Soy(OrganicReagent):
    pass


@dataclass
class SpaceMapNodeMineData(SpaceMapNodeActionData):
    drill_level: Optional[int] = field(
        default=None,
        metadata={
            "name": "DrillLevel",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SpawnPositionData:
    offset: Optional[Vector3Reference] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
        },
    )
    rotation: Optional[Vector3Reference] = field(
        default=None,
        metadata={
            "name": "Rotation",
            "type": "Element",
        },
    )
    rule: Optional[SpawnPositionRule] = field(
        default=None,
        metadata={
            "name": "Rule",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Sprite(Object):
    pass


@dataclass
class State(StateWrapper):
    class Meta:
        nillable = True


@dataclass
class Steel(OrganicReagent):
    pass


@dataclass
class Stellite(OrganicReagent):
    pass


@dataclass
class StormEffectData:
    ray_march: Optional[RayMarchData] = field(
        default=None,
        metadata={
            "name": "RayMarch",
            "type": "Element",
        },
    )
    layer1: Optional[NoiseLayerData] = field(
        default=None,
        metadata={
            "name": "Layer1",
            "type": "Element",
        },
    )
    layer2: Optional[NoiseLayerData] = field(
        default=None,
        metadata={
            "name": "Layer2",
            "type": "Element",
        },
    )
    layer3: Optional[NoiseLayerData] = field(
        default=None,
        metadata={
            "name": "Layer3",
            "type": "Element",
        },
    )
    color1: Optional[Color32Reference] = field(
        default=None,
        metadata={
            "name": "Color1",
            "type": "Element",
        },
    )
    color2: Optional[Color32Reference] = field(
        default=None,
        metadata={
            "name": "Color2",
            "type": "Element",
        },
    )
    mask_color: Optional[Color32Reference] = field(
        default=None,
        metadata={
            "name": "MaskColor",
            "type": "Element",
        },
    )
    speed: Optional[float] = field(
        default=None,
        metadata={
            "name": "Speed",
            "type": "Attribute",
            "required": True,
        },
    )
    size: Optional[float] = field(
        default=None,
        metadata={
            "name": "Size",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Sugar(OrganicReagent):
    pass


@dataclass
class SurveyData(SpaceMapNodeActionData):
    pass


@dataclass
class SurvivalPropertyCondition(ConditionComparable):
    type_value: Optional[EntitySurvivalProperty] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    percent_attribute: Optional[float] = field(
        default=None,
        metadata={
            "name": "Percent",
            "type": "Attribute",
            "required": True,
        },
    )
    ratio: Optional[float] = field(
        default=None,
        metadata={
            "name": "Ratio",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TemperatureComparableCondition(ConditionComparable):
    celsius: Optional[float] = field(
        default=None,
        metadata={
            "name": "Celsius",
            "type": "Attribute",
            "required": True,
        },
    )
    kelvin: Optional[float] = field(
        default=None,
        metadata={
            "name": "Kelvin",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TemplateNodeReference(MapNodeReference):
    template_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TemplateId",
            "type": "Attribute",
        },
    )


@dataclass
class TextureReferenceWithValue(TextureReference):
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ThicknessData(VeinModifierData):
    pass


@dataclass
class ThingCountCondition(ConditionComparable):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Tomato(OrganicReagent):
    pass


@dataclass
class TradableItem:
    color: Optional[ColorSwatchReference] = field(
        default=None,
        metadata={
            "name": "Color",
            "type": "Element",
        },
    )
    name: Optional[LocalizedStringReference] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    slot_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SlotId",
            "type": "Attribute",
        },
    )
    slot_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "SlotIndex",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Uranium(OrganicReagent):
    pass


@dataclass
class VeinDirectionData(VeinModifierData):
    x: Optional[int] = field(
        default=None,
        metadata={
            "name": "X",
            "type": "Attribute",
            "required": True,
        },
    )
    y: Optional[int] = field(
        default=None,
        metadata={
            "name": "Y",
            "type": "Attribute",
            "required": True,
        },
    )
    z: Optional[int] = field(
        default=None,
        metadata={
            "name": "Z",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Waspaloy(OrganicReagent):
    pass


@dataclass
class Wheat(OrganicReagent):
    pass


@dataclass
class WorldAtmosphereSpawnData:
    gas: list[GasAction] = field(
        default_factory=list,
        metadata={
            "name": "Gas",
            "type": "Element",
        },
    )
    x: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    y: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    z: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    room_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "RoomId",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class WorldCollection(WorldConditionBase):
    world: list[SerializedId] = field(
        default_factory=list,
        metadata={
            "name": "World",
            "type": "Element",
        },
    )
    operator: Optional[LogicOperator] = field(
        default=None,
        metadata={
            "name": "Operator",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class WorldCondition(WorldConditionBase):
    pass


@dataclass
class WorldPrefs:
    interface: Optional[Ui] = field(
        default=None,
        metadata={
            "name": "Interface",
            "type": "Element",
        },
    )
    discovered_poi: list[int] = field(
        default_factory=list,
        metadata={
            "name": "DiscoveredPoi",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass
class AllConditionData(RoomRuleConditionData):
    any: list[AnyConditionData] = field(
        default_factory=list,
        metadata={
            "name": "Any",
            "type": "Element",
        },
    )
    all: list[AllConditionData] = field(
        default_factory=list,
        metadata={
            "name": "All",
            "type": "Element",
        },
    )
    contains: list[ContainsConditionData] = field(
        default_factory=list,
        metadata={
            "name": "Contains",
            "type": "Element",
        },
    )
    smaller_than: list[SmallerThanConditionData] = field(
        default_factory=list,
        metadata={
            "name": "SmallerThan",
            "type": "Element",
        },
    )


@dataclass
class ArrayOfDifficultySetting:
    difficulty_setting: list[DifficultySetting] = field(
        default_factory=list,
        metadata={
            "name": "DifficultySetting",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfGeneCollectionWrapper:
    gene_collections: list[GeneCollectionWrapper] = field(
        default_factory=list,
        metadata={
            "name": "GeneCollections",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfPendingSpawnAction:
    pending_spawn_action: list[PendingSpawnAction] = field(
        default_factory=list,
        metadata={
            "name": "PendingSpawnAction",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfRoomData:
    room: list[RoomData] = field(
        default_factory=list,
        metadata={
            "name": "Room",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfTradableItem:
    tradable_item: list[TradableItem] = field(
        default_factory=list,
        metadata={
            "name": "TradableItem",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class AtmosphericScatteringBlendData(DataCollection):
    gas: list[list[GasTypeValue]] = field(
        default_factory=list,
        metadata={
            "name": "Gas",
            "type": "Element",
            "tokens": True,
        },
    )
    rayleigh_color_ramp_color_key: Optional[ArrayOfGradientColorKey] = field(
        default=None,
        metadata={
            "name": "RayleighColorRampColorKey",
            "type": "Element",
        },
    )
    mie_color_ramp_color_key: Optional[ArrayOfGradientColorKey] = field(
        default=None,
        metadata={
            "name": "MieColorRampColorKey",
            "type": "Element",
        },
    )
    height_rayleigh_color: Optional[Color1] = field(
        default=None,
        metadata={
            "name": "HeightRayleighColor",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class AtmosphericScatteringData:
    rayleigh_color_ramp_color_key: Optional[ArrayOfGradientColorKey] = field(
        default=None,
        metadata={
            "name": "RayleighColorRampColorKey",
            "type": "Element",
        },
    )
    rayleigh_color_ramp_alpha_key: Optional[ArrayOfGradientAlphaKey] = field(
        default=None,
        metadata={
            "name": "RayleighColorRampAlphaKey",
            "type": "Element",
        },
    )
    rayleigh_color_ramp_mode: Optional[GradientMode] = field(
        default=None,
        metadata={
            "name": "RayleighColorRampMode",
            "type": "Element",
            "required": True,
        },
    )
    world_rayleigh_color_intensity: Optional[float] = field(
        default=None,
        metadata={
            "name": "WorldRayleighColorIntensity",
            "type": "Element",
            "required": True,
        },
    )
    world_rayleigh_density: Optional[float] = field(
        default=None,
        metadata={
            "name": "WorldRayleighDensity",
            "type": "Element",
            "required": True,
        },
    )
    world_rayleigh_extinction_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "WorldRayleighExtinctionFactor",
            "type": "Element",
            "required": True,
        },
    )
    world_rayleigh_indirect_scatter: Optional[float] = field(
        default=None,
        metadata={
            "name": "WorldRayleighIndirectScatter",
            "type": "Element",
            "required": True,
        },
    )
    world_mie_color_intensity: Optional[float] = field(
        default=None,
        metadata={
            "name": "WorldMieColorIntensity",
            "type": "Element",
            "required": True,
        },
    )
    mie_color_ramp_color_key: Optional[ArrayOfGradientColorKey] = field(
        default=None,
        metadata={
            "name": "MieColorRampColorKey",
            "type": "Element",
        },
    )
    mie_color_ramp_alpha_key: Optional[ArrayOfGradientAlphaKey] = field(
        default=None,
        metadata={
            "name": "MieColorRampAlphaKey",
            "type": "Element",
        },
    )
    mie_color_ramp_mode: Optional[GradientMode] = field(
        default=None,
        metadata={
            "name": "MieColorRampMode",
            "type": "Element",
            "required": True,
        },
    )
    world_mie_density: Optional[float] = field(
        default=None,
        metadata={
            "name": "WorldMieDensity",
            "type": "Element",
            "required": True,
        },
    )
    world_mie_extinction_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "WorldMieExtinctionFactor",
            "type": "Element",
            "required": True,
        },
    )
    world_mie_phase_anisotropy: Optional[float] = field(
        default=None,
        metadata={
            "name": "WorldMiePhaseAnisotropy",
            "type": "Element",
            "required": True,
        },
    )
    world_near_scatter_push: Optional[float] = field(
        default=None,
        metadata={
            "name": "WorldNearScatterPush",
            "type": "Element",
            "required": True,
        },
    )
    world_normal_distance: Optional[float] = field(
        default=None,
        metadata={
            "name": "WorldNormalDistance",
            "type": "Element",
            "required": True,
        },
    )
    height_rayleigh_color: Optional[Color1] = field(
        default=None,
        metadata={
            "name": "HeightRayleighColor",
            "type": "Element",
            "required": True,
        },
    )
    height_rayleigh_intensity: Optional[float] = field(
        default=None,
        metadata={
            "name": "HeightRayleighIntensity",
            "type": "Element",
            "required": True,
        },
    )
    height_rayleigh_density: Optional[float] = field(
        default=None,
        metadata={
            "name": "HeightRayleighDensity",
            "type": "Element",
            "required": True,
        },
    )
    height_mie_density: Optional[float] = field(
        default=None,
        metadata={
            "name": "HeightMieDensity",
            "type": "Element",
            "required": True,
        },
    )
    height_extinction_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "HeightExtinctionFactor",
            "type": "Element",
            "required": True,
        },
    )
    height_sea_level: Optional[float] = field(
        default=None,
        metadata={
            "name": "HeightSeaLevel",
            "type": "Element",
            "required": True,
        },
    )
    height_distance: Optional[float] = field(
        default=None,
        metadata={
            "name": "HeightDistance",
            "type": "Element",
            "required": True,
        },
    )
    height_plane_shift: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "HeightPlaneShift",
            "type": "Element",
            "required": True,
        },
    )
    height_near_scatter_push: Optional[float] = field(
        default=None,
        metadata={
            "name": "HeightNearScatterPush",
            "type": "Element",
            "required": True,
        },
    )
    height_normal_distance: Optional[float] = field(
        default=None,
        metadata={
            "name": "HeightNormalDistance",
            "type": "Element",
            "required": True,
        },
    )
    use_occlusion: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseOcclusion",
            "type": "Element",
            "required": True,
        },
    )
    occlusion_bias: Optional[float] = field(
        default=None,
        metadata={
            "name": "OcclusionBias",
            "type": "Element",
            "required": True,
        },
    )
    occlusion_bias_indirect: Optional[float] = field(
        default=None,
        metadata={
            "name": "OcclusionBiasIndirect",
            "type": "Element",
            "required": True,
        },
    )
    occlusion_bias_clouds: Optional[float] = field(
        default=None,
        metadata={
            "name": "OcclusionBiasClouds",
            "type": "Element",
            "required": True,
        },
    )
    occlusion_downscale: Optional[OcclusionDownscale] = field(
        default=None,
        metadata={
            "name": "OcclusionDownscale",
            "type": "Element",
            "required": True,
        },
    )
    occlusion_samples: Optional[OcclusionSamples] = field(
        default=None,
        metadata={
            "name": "OcclusionSamples",
            "type": "Element",
            "required": True,
        },
    )
    occlusion_depth_fixup: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OcclusionDepthFixup",
            "type": "Element",
            "required": True,
        },
    )
    occlusion_depth_threshold: Optional[float] = field(
        default=None,
        metadata={
            "name": "OcclusionDepthThreshold",
            "type": "Element",
            "required": True,
        },
    )
    occlusion_full_sky: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OcclusionFullSky",
            "type": "Element",
            "required": True,
        },
    )
    occlusion_bias_sky_rayleigh: Optional[float] = field(
        default=None,
        metadata={
            "name": "OcclusionBiasSkyRayleigh",
            "type": "Element",
            "required": True,
        },
    )
    occlusion_bias_sky_mie: Optional[float] = field(
        default=None,
        metadata={
            "name": "OcclusionBiasSkyMie",
            "type": "Element",
            "required": True,
        },
    )
    world_scale_exponent: Optional[float] = field(
        default=None,
        metadata={
            "name": "WorldScaleExponent",
            "type": "Element",
            "required": True,
        },
    )
    force_per_pixel: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ForcePerPixel",
            "type": "Element",
            "required": True,
        },
    )
    force_post_effect: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ForcePostEffect",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class AudioData:
    audio_clips_data: Optional[ArrayOfGameAudioClipsData] = field(
        default=None,
        metadata={
            "name": "AudioClipsData",
            "type": "Element",
        },
    )
    channel_data: Optional[ArrayOfChannelData] = field(
        default=None,
        metadata={
            "name": "ChannelData",
            "type": "Element",
        },
    )


@dataclass
class BlueprintData(DataCollection):
    mesh: Optional[MeshReference] = field(
        default=None,
        metadata={
            "name": "Mesh",
            "type": "Element",
        },
    )
    edge: list[EdgeData] = field(
        default_factory=list,
        metadata={
            "name": "Edge",
            "type": "Element",
        },
    )


@dataclass
class Celestial(CelestialReference):
    class Meta:
        nillable = True


@dataclass
class CelestialBodyTemplate(CelestialReference):
    orbit: Optional[OrbitData] = field(
        default=None,
        metadata={
            "name": "Orbit",
            "type": "Element",
        },
    )
    longitude_at_epoch: Optional[float] = field(
        default=None,
        metadata={
            "name": "LongitudeAtEpoch",
            "type": "Element",
            "required": True,
        },
    )
    color: Optional[ColorRgb] = field(
        default=None,
        metadata={
            "name": "Color",
            "type": "Element",
        },
    )
    sunrise_offset: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "SunriseOffset",
            "type": "Element",
        },
    )


@dataclass
class CelestialConstantsReference(CelestialReference):
    time_offset: Optional[TimeSpanReference] = field(
        default=None,
        metadata={
            "name": "TimeOffset",
            "type": "Element",
        },
    )
    body_scale: Optional[float] = field(
        default=None,
        metadata={
            "name": "BodyScale",
            "type": "Attribute",
            "required": True,
        },
    )
    skybox_scale: Optional[float] = field(
        default=None,
        metadata={
            "name": "SkyboxScale",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CompletedTutorialPopupAction(PopupAction):
    pass


@dataclass
class ConditionDataCollection:
    conditions: list[ConditionDataCollection] = field(
        default_factory=list,
        metadata={
            "name": "Conditions",
            "type": "Element",
        },
    )
    room: list[RoomCondition] = field(
        default_factory=list,
        metadata={
            "name": "Room",
            "type": "Element",
        },
    )
    custom_name: list[CustomNameCondition] = field(
        default_factory=list,
        metadata={
            "name": "CustomName",
            "type": "Element",
        },
    )
    prefab: list[ThingPrefabCondition] = field(
        default_factory=list,
        metadata={
            "name": "Prefab",
            "type": "Element",
        },
    )
    contact: list[TraderContactCondition] = field(
        default_factory=list,
        metadata={
            "name": "Contact",
            "type": "Element",
        },
    )
    size: list[SizeCondition] = field(
        default_factory=list,
        metadata={
            "name": "Size",
            "type": "Element",
        },
    )
    temperature: list[TemperatureComparableCondition] = field(
        default_factory=list,
        metadata={
            "name": "Temperature",
            "type": "Element",
        },
    )
    growth_state: list[GrowthStateCondition] = field(
        default_factory=list,
        metadata={
            "name": "GrowthState",
            "type": "Element",
        },
    )
    plant_status: list[PlantStatusCondition] = field(
        default_factory=list,
        metadata={
            "name": "PlantStatus",
            "type": "Element",
        },
    )
    plant_record: list[PlantRecordCondition] = field(
        default_factory=list,
        metadata={
            "name": "PlantRecord",
            "type": "Element",
        },
    )
    logic_type: list[LogicCondition] = field(
        default_factory=list,
        metadata={
            "name": "LogicType",
            "type": "Element",
        },
    )
    reagents: list[ReagentCondition] = field(
        default_factory=list,
        metadata={
            "name": "Reagents",
            "type": "Element",
        },
    )
    build_state: list[BuildStateCondition] = field(
        default_factory=list,
        metadata={
            "name": "BuildState",
            "type": "Element",
        },
    )
    interactable: list[InteractableCondition] = field(
        default_factory=list,
        metadata={
            "name": "Interactable",
            "type": "Element",
        },
    )
    decay: list[Decay] = field(
        default_factory=list,
        metadata={
            "name": "Decay",
            "type": "Element",
        },
    )
    quantity: list[Quantity] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
        },
    )
    gas: list[GasCondition] = field(
        default_factory=list,
        metadata={
            "name": "Gas",
            "type": "Element",
        },
    )
    pressure: list[PressureCondition] = field(
        default_factory=list,
        metadata={
            "name": "Pressure",
            "type": "Element",
        },
    )
    temperature_range: list[TemperatureRangeCondition] = field(
        default_factory=list,
        metadata={
            "name": "TemperatureRange",
            "type": "Element",
        },
    )
    item: list[Item] = field(
        default_factory=list,
        metadata={
            "name": "Item",
            "type": "Element",
        },
    )
    percent: list[Percent] = field(
        default_factory=list,
        metadata={
            "name": "Percent",
            "type": "Element",
        },
    )
    moles: list[Moles] = field(
        default_factory=list,
        metadata={
            "name": "Moles",
            "type": "Element",
        },
    )
    charge: list[Energy] = field(
        default_factory=list,
        metadata={
            "name": "Charge",
            "type": "Element",
        },
    )
    difficulty: list[Difficulty] = field(
        default_factory=list,
        metadata={
            "name": "Difficulty",
            "type": "Element",
        },
    )
    species: list[Species] = field(
        default_factory=list,
        metadata={
            "name": "Species",
            "type": "Element",
        },
    )
    pre_spawned: list[PreSpawnedCondition] = field(
        default_factory=list,
        metadata={
            "name": "PreSpawned",
            "type": "Element",
        },
    )
    in_cell: list[InCellCondition] = field(
        default_factory=list,
        metadata={
            "name": "InCell",
            "type": "Element",
        },
    )
    region: list[RegionCondition] = field(
        default_factory=list,
        metadata={
            "name": "Region",
            "type": "Element",
        },
    )
    surface: list[SurfaceCondition] = field(
        default_factory=list,
        metadata={
            "name": "Surface",
            "type": "Element",
        },
    )
    depth: list[DepthCondition] = field(
        default_factory=list,
        metadata={
            "name": "Depth",
            "type": "Element",
        },
    )
    hidden: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Hidden",
            "type": "Attribute",
            "required": True,
        },
    )
    operator: Optional[LogicOperator] = field(
        default=None,
        metadata={
            "name": "Operator",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class DepositCompositionData:
    ore: list[DepositMaterialOreData] = field(
        default_factory=list,
        metadata={
            "name": "Ore",
            "type": "Element",
        },
    )
    reagent_mix: list[DepositMaterialReagentMixData] = field(
        default_factory=list,
        metadata={
            "name": "ReagentMix",
            "type": "Element",
        },
    )
    ice: list[DepositMaterialGasData] = field(
        default_factory=list,
        metadata={
            "name": "Ice",
            "type": "Element",
        },
    )
    gas: list[DepositMaterialGasData] = field(
        default_factory=list,
        metadata={
            "name": "Gas",
            "type": "Element",
        },
    )
    hidden: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Hidden",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class FacialExpressionData(DataCollection):
    happy: Optional[float] = field(
        default=None,
        metadata={
            "name": "Happy",
            "type": "Attribute",
            "required": True,
        },
    )
    angry: Optional[float] = field(
        default=None,
        metadata={
            "name": "Angry",
            "type": "Attribute",
            "required": True,
        },
    )
    surprised: Optional[float] = field(
        default=None,
        metadata={
            "name": "Surprised",
            "type": "Attribute",
            "required": True,
        },
    )
    open: Optional[float] = field(
        default=None,
        metadata={
            "name": "Open",
            "type": "Attribute",
            "required": True,
        },
    )
    none: Optional[float] = field(
        default=None,
        metadata={
            "name": "None",
            "type": "Attribute",
            "required": True,
        },
    )
    dead: Optional[float] = field(
        default=None,
        metadata={
            "name": "Dead",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class FixedRotation(CelestialRotation):
    speed: Optional[float] = field(
        default=None,
        metadata={
            "name": "Speed",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class GameAudioEvent:
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    channel: Optional[int] = field(
        default=None,
        metadata={
            "name": "Channel",
            "type": "Element",
            "required": True,
        },
    )
    clips_data: Optional[GameAudioClipsData] = field(
        default=None,
        metadata={
            "name": "ClipsData",
            "type": "Element",
        },
    )
    stop_if_invalid: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StopIfInvalid",
            "type": "Element",
            "required": True,
        },
    )
    conditions: Optional[ArrayOfSoundEffectCondition] = field(
        default=None,
        metadata={
            "name": "Conditions",
            "type": "Element",
        },
    )
    build_state_conditions: Optional[ArrayOfInt] = field(
        default=None,
        metadata={
            "name": "BuildStateConditions",
            "type": "Element",
        },
    )


@dataclass
class GeneCollection(GeneCollectionWrapper):
    class Meta:
        nillable = True


@dataclass
class GlobalPlantSaveData:
    prefab_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrefabId",
            "type": "Element",
        },
    )
    gene_collection_wrapper: Optional[GeneCollectionWrapper] = field(
        default=None,
        metadata={
            "name": "GeneCollectionWrapper",
            "type": "Element",
        },
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class GlobalTemperatureCurveOffset(GlobalTemperatureOffsetData):
    day: Optional[AnimationCurveData] = field(
        default=None,
        metadata={
            "name": "Day",
            "type": "Element",
        },
    )
    night: Optional[AnimationCurveData] = field(
        default=None,
        metadata={
            "name": "Night",
            "type": "Element",
        },
    )


@dataclass
class LifeRequirementsData(DataCollection):
    liquid_per_tick: Optional[GasQuantityData] = field(
        default=None,
        metadata={
            "name": "LiquidPerTick",
            "type": "Element",
        },
    )
    inhaled: list[GasQuantityRatioData] = field(
        default_factory=list,
        metadata={
            "name": "Inhaled",
            "type": "Element",
        },
    )
    exhaled: list[GasQuantityData] = field(
        default_factory=list,
        metadata={
            "name": "Exhaled",
            "type": "Element",
        },
    )
    harmful_gas: list[GasPressureData] = field(
        default_factory=list,
        metadata={
            "name": "HarmfulGas",
            "type": "Element",
        },
    )
    water_usage: Optional[PlantStatData] = field(
        default=None,
        metadata={
            "name": "WaterUsage",
            "type": "Element",
        },
    )
    gas_production: Optional[PlantStatData] = field(
        default=None,
        metadata={
            "name": "GasProduction",
            "type": "Element",
        },
    )
    growth_speed_multiplier: Optional[PlantStatData] = field(
        default=None,
        metadata={
            "name": "GrowthSpeedMultiplier",
            "type": "Element",
        },
    )
    time_until_dehydration_damage: Optional[PlantStatData] = field(
        default=None,
        metadata={
            "name": "TimeUntilDehydrationDamage",
            "type": "Element",
        },
    )
    time_until_undesired_gas_damage: Optional[PlantStatData] = field(
        default=None,
        metadata={
            "name": "TimeUntilUndesiredGasDamage",
            "type": "Element",
        },
    )
    undesired_gas_resistance: Optional[PlantStatData] = field(
        default=None,
        metadata={
            "name": "UndesiredGasResistance",
            "type": "Element",
        },
    )
    time_until_frozen_damage: Optional[PlantStatData] = field(
        default=None,
        metadata={
            "name": "TimeUntilFrozenDamage",
            "type": "Element",
        },
    )
    time_until_over_heated_damage: Optional[PlantStatData] = field(
        default=None,
        metadata={
            "name": "TimeUntilOverHeatedDamage",
            "type": "Element",
        },
    )
    time_until_suffocated_damage: Optional[PlantStatData] = field(
        default=None,
        metadata={
            "name": "TimeUntilSuffocatedDamage",
            "type": "Element",
        },
    )
    time_until_low_pressure_damage: Optional[PlantStatData] = field(
        default=None,
        metadata={
            "name": "TimeUntilLowPressureDamage",
            "type": "Element",
        },
    )
    time_until_high_pressure_damage: Optional[PlantStatData] = field(
        default=None,
        metadata={
            "name": "TimeUntilHighPressureDamage",
            "type": "Element",
        },
    )
    time_until_light_damage: Optional[PlantStatData] = field(
        default=None,
        metadata={
            "name": "TimeUntilLightDamage",
            "type": "Element",
        },
    )
    time_until_darkness_damage: Optional[PlantStatData] = field(
        default=None,
        metadata={
            "name": "TimeUntilDarknessDamage",
            "type": "Element",
        },
    )
    light_per_day: Optional[PlantStatData] = field(
        default=None,
        metadata={
            "name": "LightPerDay",
            "type": "Element",
        },
    )
    darkness_per_day: Optional[PlantStatData] = field(
        default=None,
        metadata={
            "name": "DarknessPerDay",
            "type": "Element",
        },
    )
    grow_temperature_c: Optional[MultiPlantStatData] = field(
        default=None,
        metadata={
            "name": "GrowTemperatureC",
            "type": "Element",
        },
    )
    grow_pressure: Optional[MultiPlantStatData] = field(
        default=None,
        metadata={
            "name": "GrowPressure",
            "type": "Element",
        },
    )


@dataclass
class LogicStateSave:
    display_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "DisplayName",
            "type": "Element",
        },
    )
    conditions: Optional[ArrayOfLogicConditionSave] = field(
        default=None,
        metadata={
            "name": "Conditions",
            "type": "Element",
        },
    )
    actions: Optional[ArrayOfLogicActionSave] = field(
        default=None,
        metadata={
            "name": "Actions",
            "type": "Element",
        },
    )
    is_triggered: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsTriggered",
            "type": "Element",
            "required": True,
        },
    )
    next_logic_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "NextLogicIndex",
            "type": "Element",
            "required": True,
        },
    )
    false_logic_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "FalseLogicIndex",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class MinableVisualiserData(DataCollection):
    mesh: Optional[MeshReference] = field(
        default=None,
        metadata={
            "name": "Mesh",
            "type": "Element",
        },
    )
    color: Optional[ColorFloat4Reference] = field(
        default=None,
        metadata={
            "name": "Color",
            "type": "Element",
        },
    )
    color32: Optional[Color32Reference] = field(
        default=None,
        metadata={
            "name": "Color32",
            "type": "Element",
        },
    )
    terrain_color: Optional[ColorFloat4Reference] = field(
        default=None,
        metadata={
            "name": "TerrainColor",
            "type": "Element",
        },
    )
    terrain_color32: Optional[Color32Reference] = field(
        default=None,
        metadata={
            "name": "TerrainColor32",
            "type": "Element",
        },
    )
    type_value: Optional[MinableType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class NormalMapReference(TextureReferenceWithValue):
    pass


@dataclass
class ObjectiveConditionCollection:
    conditions: list[ObjectiveConditionCollection] = field(
        default_factory=list,
        metadata={
            "name": "Conditions",
            "type": "Element",
        },
    )
    contact: list[TraderContactCondition] = field(
        default_factory=list,
        metadata={
            "name": "Contact",
            "type": "Element",
        },
    )
    network: list[NetworkCondition] = field(
        default_factory=list,
        metadata={
            "name": "Network",
            "type": "Element",
        },
    )
    room: list[RoomCondition] = field(
        default_factory=list,
        metadata={
            "name": "Room",
            "type": "Element",
        },
    )
    prefab: list[ThingPrefabCondition] = field(
        default_factory=list,
        metadata={
            "name": "Prefab",
            "type": "Element",
        },
    )
    objective_complete: list[ObjectiveCompleteCondition] = field(
        default_factory=list,
        metadata={
            "name": "ObjectiveComplete",
            "type": "Element",
        },
    )
    player: list[EntityStateCondition] = field(
        default_factory=list,
        metadata={
            "name": "Player",
            "type": "Element",
        },
    )
    hidden: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Hidden",
            "type": "Attribute",
            "required": True,
        },
    )
    operator: Optional[LogicOperator] = field(
        default=None,
        metadata={
            "name": "Operator",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class PlayableBodyReference(CelestialReference):
    latitude: Optional[float] = field(
        default=None,
        metadata={
            "name": "Latitude",
            "type": "Attribute",
            "required": True,
        },
    )
    longitude: Optional[float] = field(
        default=None,
        metadata={
            "name": "Longitude",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class PlayerCookieSaveDataV2:
    dismissed_major_update_popup: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DismissedMajorUpdatePopup",
            "type": "Element",
            "required": True,
        },
    )
    dismissed_old_save_popup: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DismissedOldSavePopup",
            "type": "Element",
            "required": True,
        },
    )
    world: list[WorldPrefs] = field(
        default_factory=list,
        metadata={
            "name": "World",
            "type": "Element",
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
        },
    )
    client_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ClientId",
            "type": "Attribute",
            "required": True,
        },
    )
    username: Optional[str] = field(
        default=None,
        metadata={
            "name": "Username",
            "type": "Attribute",
        },
    )


@dataclass
class PreviewScene:
    camera_position: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "CameraPosition",
            "type": "Element",
            "required": True,
        },
    )
    camera_rotation: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "CameraRotation",
            "type": "Element",
            "required": True,
        },
    )
    sun_rotation: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "SunRotation",
            "type": "Element",
            "required": True,
        },
    )
    sun_prefab: Optional[str] = field(
        default=None,
        metadata={
            "name": "SunPrefab",
            "type": "Element",
        },
    )
    atmospheric_scattering: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AtmosphericScattering",
            "type": "Element",
            "required": True,
        },
    )
    lens_flare: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LensFlare",
            "type": "Element",
            "required": True,
        },
    )
    lens_flare_intensity: Optional[float] = field(
        default=None,
        metadata={
            "name": "LensFlareIntensity",
            "type": "Element",
            "required": True,
        },
    )
    sky_box_material: Optional[str] = field(
        default=None,
        metadata={
            "name": "SkyBoxMaterial",
            "type": "Element",
        },
    )
    prefabs: Optional[ArrayOfPlanetPrefab] = field(
        default=None,
        metadata={
            "name": "Prefabs",
            "type": "Element",
        },
    )
    fov: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class PrimaryBodyReference(CelestialReference):
    solar_constant: Optional[float] = field(
        default=None,
        metadata={
            "name": "SolarConstant",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ReagentMixture:
    flour: Optional[Flour] = field(
        default=None,
        metadata={
            "name": "Flour",
            "type": "Element",
        },
    )
    milk: Optional[Milk] = field(
        default=None,
        metadata={
            "name": "Milk",
            "type": "Element",
        },
    )
    egg: Optional[Egg] = field(
        default=None,
        metadata={
            "name": "Egg",
            "type": "Element",
        },
    )
    iron: Optional[Iron] = field(
        default=None,
        metadata={
            "name": "Iron",
            "type": "Element",
        },
    )
    gold: Optional[Gold] = field(
        default=None,
        metadata={
            "name": "Gold",
            "type": "Element",
        },
    )
    carbon: Optional[Carbon] = field(
        default=None,
        metadata={
            "name": "Carbon",
            "type": "Element",
        },
    )
    uranium: Optional[Uranium] = field(
        default=None,
        metadata={
            "name": "Uranium",
            "type": "Element",
        },
    )
    copper: Optional[Copper] = field(
        default=None,
        metadata={
            "name": "Copper",
            "type": "Element",
        },
    )
    steel: Optional[Steel] = field(
        default=None,
        metadata={
            "name": "Steel",
            "type": "Element",
        },
    )
    hydrocarbon: Optional[Hydrocarbon] = field(
        default=None,
        metadata={
            "name": "Hydrocarbon",
            "type": "Element",
        },
    )
    silver: Optional[Silver] = field(
        default=None,
        metadata={
            "name": "Silver",
            "type": "Element",
        },
    )
    nickel: Optional[Nickel] = field(
        default=None,
        metadata={
            "name": "Nickel",
            "type": "Element",
        },
    )
    lead: Optional[Lead] = field(
        default=None,
        metadata={
            "name": "Lead",
            "type": "Element",
        },
    )
    electrum: Optional[Electrum] = field(
        default=None,
        metadata={
            "name": "Electrum",
            "type": "Element",
        },
    )
    invar: Optional[Invar] = field(
        default=None,
        metadata={
            "name": "Invar",
            "type": "Element",
        },
    )
    constantan: Optional[Constantan] = field(
        default=None,
        metadata={
            "name": "Constantan",
            "type": "Element",
        },
    )
    solder: Optional[Solder] = field(
        default=None,
        metadata={
            "name": "Solder",
            "type": "Element",
        },
    )
    plastic: Optional[Plastic] = field(
        default=None,
        metadata={
            "name": "Plastic",
            "type": "Element",
        },
    )
    silicon: Optional[Silicon] = field(
        default=None,
        metadata={
            "name": "Silicon",
            "type": "Element",
        },
    )
    salicylic_acid: Optional[SalicylicAcid] = field(
        default=None,
        metadata={
            "name": "SalicylicAcid",
            "type": "Element",
        },
    )
    alcohol: Optional[Alcohol] = field(
        default=None,
        metadata={
            "name": "Alcohol",
            "type": "Element",
        },
    )
    oil: Optional[Oil] = field(
        default=None,
        metadata={
            "name": "Oil",
            "type": "Element",
        },
    )
    potato: Optional[Potato] = field(
        default=None,
        metadata={
            "name": "Potato",
            "type": "Element",
        },
    )
    tomato: Optional[Tomato] = field(
        default=None,
        metadata={
            "name": "Tomato",
            "type": "Element",
        },
    )
    fenoxitone: Optional[Fenoxitone] = field(
        default=None,
        metadata={
            "name": "Fenoxitone",
            "type": "Element",
        },
    )
    color_red: Optional[ColorRed] = field(
        default=None,
        metadata={
            "name": "ColorRed",
            "type": "Element",
        },
    )
    color_green: Optional[ColorGreen] = field(
        default=None,
        metadata={
            "name": "ColorGreen",
            "type": "Element",
        },
    )
    color_blue: Optional[ColorBlue] = field(
        default=None,
        metadata={
            "name": "ColorBlue",
            "type": "Element",
        },
    )
    color_yellow: Optional[ColorYellow] = field(
        default=None,
        metadata={
            "name": "ColorYellow",
            "type": "Element",
        },
    )
    color_orange: Optional[ColorOrange] = field(
        default=None,
        metadata={
            "name": "ColorOrange",
            "type": "Element",
        },
    )
    pumpkin: Optional[Pumpkin] = field(
        default=None,
        metadata={
            "name": "Pumpkin",
            "type": "Element",
        },
    )
    rice: Optional[Rice] = field(
        default=None,
        metadata={
            "name": "Rice",
            "type": "Element",
        },
    )
    waspaloy: Optional[Waspaloy] = field(
        default=None,
        metadata={
            "name": "Waspaloy",
            "type": "Element",
        },
    )
    stellite: Optional[Stellite] = field(
        default=None,
        metadata={
            "name": "Stellite",
            "type": "Element",
        },
    )
    inconel: Optional[Inconel] = field(
        default=None,
        metadata={
            "name": "Inconel",
            "type": "Element",
        },
    )
    hastelloy: Optional[Hastelloy] = field(
        default=None,
        metadata={
            "name": "Hastelloy",
            "type": "Element",
        },
    )
    astroloy: Optional[Astroloy] = field(
        default=None,
        metadata={
            "name": "Astroloy",
            "type": "Element",
        },
    )
    cobalt: Optional[Cobalt] = field(
        default=None,
        metadata={
            "name": "Cobalt",
            "type": "Element",
        },
    )
    corn: Optional[Corn] = field(
        default=None,
        metadata={
            "name": "Corn",
            "type": "Element",
        },
    )
    wheat: Optional[Wheat] = field(
        default=None,
        metadata={
            "name": "Wheat",
            "type": "Element",
        },
    )
    biomass: Optional[Biomass] = field(
        default=None,
        metadata={
            "name": "Biomass",
            "type": "Element",
        },
    )
    soy: Optional[Soy] = field(
        default=None,
        metadata={
            "name": "Soy",
            "type": "Element",
        },
    )
    mushroom: Optional[Mushroom] = field(
        default=None,
        metadata={
            "name": "Mushroom",
            "type": "Element",
        },
    )
    sugar: Optional[Sugar] = field(
        default=None,
        metadata={
            "name": "Sugar",
            "type": "Element",
        },
    )
    cocoa: Optional[Cocoa] = field(
        default=None,
        metadata={
            "name": "Cocoa",
            "type": "Element",
        },
    )
    cheese: Optional[Cheese] = field(
        default=None,
        metadata={
            "name": "Cheese",
            "type": "Element",
        },
    )


@dataclass
class RecipeData:
    prefab_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrefabName",
            "type": "Element",
        },
    )
    recipe: Optional[Recipe] = field(
        default=None,
        metadata={
            "name": "Recipe",
            "type": "Element",
            "required": True,
        },
    )
    recipe_tier: Optional[MachineTier] = field(
        default=None,
        metadata={
            "name": "RecipeTier",
            "type": "Element",
            "required": True,
        },
    )
    output: Optional[float] = field(
        default=None,
        metadata={
            "name": "Output",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Region(DataCollection):
    r: Optional[int] = field(
        default=None,
        metadata={
            "name": "R",
            "type": "Attribute",
            "required": True,
        },
    )
    g: Optional[int] = field(
        default=None,
        metadata={
            "name": "G",
            "type": "Attribute",
            "required": True,
        },
    )
    b: Optional[int] = field(
        default=None,
        metadata={
            "name": "B",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ResearchData:
    research_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResearchName",
            "type": "Element",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
        },
    )
    prefabs_unlocked: Optional[ArrayOfString1] = field(
        default=None,
        metadata={
            "name": "PrefabsUnlocked",
            "type": "Element",
        },
    )
    research_required: Optional[ArrayOfString2] = field(
        default=None,
        metadata={
            "name": "ResearchRequired",
            "type": "Element",
        },
    )
    pod_data_required: Optional[ArrayOfResearchPodData] = field(
        default=None,
        metadata={
            "name": "PodDataRequired",
            "type": "Element",
        },
    )
    research_sort_type: Optional[ResearchSort] = field(
        default=None,
        metadata={
            "name": "ResearchSortType",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Room:
    grids: Optional[ArrayOfWorldGrid] = field(
        default=None,
        metadata={
            "name": "Grids",
            "type": "Element",
        },
    )
    room_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "RoomId",
            "type": "Element",
            "required": True,
        },
    )
    will_save: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WillSave",
            "type": "Element",
            "required": True,
        },
    )
    frozen_contents: Optional[GasMixture] = field(
        default=None,
        metadata={
            "name": "FrozenContents",
            "type": "Element",
            "required": True,
        },
    )
    frozen_contents_lock: Optional[object] = field(
        default=None,
        metadata={
            "name": "FrozenContentsLock",
            "type": "Element",
        },
    )
    gas_mixture: Optional[GasMixture] = field(
        default=None,
        metadata={
            "name": "GasMixture",
            "type": "Element",
            "required": True,
        },
    )
    average_gas_mixture: Optional[GasMixture] = field(
        default=None,
        metadata={
            "name": "AverageGasMixture",
            "type": "Element",
            "required": True,
        },
    )
    volume: Optional[VolumeLitres] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
            "required": True,
        },
    )
    pressure: Optional[PressurekPa] = field(
        default=None,
        metadata={
            "name": "Pressure",
            "type": "Element",
            "required": True,
        },
    )
    temperature: Optional[TemperatureKelvin] = field(
        default=None,
        metadata={
            "name": "Temperature",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Select:
    conditions: list[ConditionCollection] = field(
        default_factory=list,
        metadata={
            "name": "Conditions",
            "type": "Element",
        },
    )


@dataclass
class SellItem(TradableItem):
    interaction: list[InteractionAction] = field(
        default_factory=list,
        metadata={
            "name": "Interaction",
            "type": "Element",
        },
    )
    move_player: list[MovePlayerAction] = field(
        default_factory=list,
        metadata={
            "name": "MovePlayer",
            "type": "Element",
        },
    )
    gene: list[GeneAction] = field(
        default_factory=list,
        metadata={
            "name": "Gene",
            "type": "Element",
        },
    )
    quantity: list[QuantityAction] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
        },
    )
    percent: list[PercentAction] = field(
        default_factory=list,
        metadata={
            "name": "Percent",
            "type": "Element",
        },
    )
    reagents: list[SetReagents] = field(
        default_factory=list,
        metadata={
            "name": "Reagents",
            "type": "Element",
        },
    )
    charge: list[ChargeAction] = field(
        default_factory=list,
        metadata={
            "name": "Charge",
            "type": "Element",
        },
    )
    gas: list[GasAction] = field(
        default_factory=list,
        metadata={
            "name": "Gas",
            "type": "Element",
        },
    )
    source_code: list[SourceCodeAction] = field(
        default_factory=list,
        metadata={
            "name": "SourceCode",
            "type": "Element",
        },
    )
    item: list[SellItem] = field(
        default_factory=list,
        metadata={
            "name": "Item",
            "type": "Element",
        },
    )


@dataclass
class ServerProvider(DataCollection):
    url: Optional[StringReference] = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Element",
        },
    )
    logo: Optional[TextureReference] = field(
        default=None,
        metadata={
            "name": "Logo",
            "type": "Element",
        },
    )


@dataclass
class SettingData:
    settings_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "SettingsVersion",
            "type": "Element",
        },
    )
    show_fps: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ShowFps",
            "type": "Element",
            "required": True,
        },
    )
    show_latency: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ShowLatency",
            "type": "Element",
            "required": True,
        },
    )
    auto_save: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AutoSave",
            "type": "Element",
            "required": True,
        },
    )
    save_interval: Optional[int] = field(
        default=None,
        metadata={
            "name": "SaveInterval",
            "type": "Element",
            "required": True,
        },
    )
    max_auto_saves: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxAutoSaves",
            "type": "Element",
            "required": True,
        },
    )
    max_quick_saves: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxQuickSaves",
            "type": "Element",
            "required": True,
        },
    )
    save_path: Optional[str] = field(
        default=None,
        metadata={
            "name": "SavePath",
            "type": "Element",
        },
    )
    hudscale: Optional[int] = field(
        default=None,
        metadata={
            "name": "HUDScale",
            "type": "Element",
            "required": True,
        },
    )
    tooltip_opacity: Optional[float] = field(
        default=None,
        metadata={
            "name": "TooltipOpacity",
            "type": "Element",
            "required": True,
        },
    )
    ingame_portrait: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IngamePortrait",
            "type": "Element",
            "required": True,
        },
    )
    extended_tooltips: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ExtendedTooltips",
            "type": "Element",
            "required": True,
        },
    )
    chat_fade_timer: Optional[float] = field(
        default=None,
        metadata={
            "name": "ChatFadeTimer",
            "type": "Element",
            "required": True,
        },
    )
    day_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "DayLength",
            "type": "Element",
            "required": True,
        },
    )
    legacy_inventory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LegacyInventory",
            "type": "Element",
            "required": True,
        },
    )
    show_slot_tool_tips: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ShowSlotToolTips",
            "type": "Element",
            "required": True,
        },
    )
    delete_skeleton_on_decay: Optional[DeleteSkeletonOnDecay] = field(
        default=None,
        metadata={
            "name": "DeleteSkeletonOnDecay",
            "type": "Element",
            "required": True,
        },
    )
    monitor: Optional[int] = field(
        default=None,
        metadata={
            "name": "Monitor",
            "type": "Element",
            "required": True,
        },
    )
    screen_width: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScreenWidth",
            "type": "Element",
        },
    )
    screen_height: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScreenHeight",
            "type": "Element",
        },
    )
    refresh_rate: Optional[int] = field(
        default=None,
        metadata={
            "name": "RefreshRate",
            "type": "Element",
            "required": True,
        },
    )
    graphic_quality: Optional[str] = field(
        default=None,
        metadata={
            "name": "GraphicQuality",
            "type": "Element",
        },
    )
    texture_quality: Optional[str] = field(
        default=None,
        metadata={
            "name": "TextureQuality",
            "type": "Element",
        },
    )
    full_screen: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FullScreen",
            "type": "Element",
            "required": True,
        },
    )
    vsync: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Vsync",
            "type": "Element",
            "required": True,
        },
    )
    shadows: Optional[str] = field(
        default=None,
        metadata={
            "name": "Shadows",
            "type": "Element",
        },
    )
    distant_shadows: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DistantShadows",
            "type": "Element",
            "required": True,
        },
    )
    shadow_resolution: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShadowResolution",
            "type": "Element",
        },
    )
    shadow_distance: Optional[int] = field(
        default=None,
        metadata={
            "name": "ShadowDistance",
            "type": "Element",
            "required": True,
        },
    )
    light_shadow_distance: Optional[int] = field(
        default=None,
        metadata={
            "name": "LightShadowDistance",
            "type": "Element",
            "required": True,
        },
    )
    room_control_tick_speed: Optional[int] = field(
        default=None,
        metadata={
            "name": "RoomControlTickSpeed",
            "type": "Element",
            "required": True,
        },
    )
    shadow_near_plane_offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "ShadowNearPlaneOffset",
            "type": "Element",
            "required": True,
        },
    )
    shadow_cascades: Optional[int] = field(
        default=None,
        metadata={
            "name": "ShadowCascades",
            "type": "Element",
            "required": True,
        },
    )
    shadow_cascade2_split: Optional[float] = field(
        default=None,
        metadata={
            "name": "ShadowCascade2Split",
            "type": "Element",
            "required": True,
        },
    )
    shadow_cascade4_split: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "ShadowCascade4Split",
            "type": "Element",
            "required": True,
        },
    )
    thing_shadow_mode: Optional[str] = field(
        default=None,
        metadata={
            "name": "ThingShadowMode",
            "type": "Element",
        },
    )
    thing_shadow_distance_multiplier: Optional[float] = field(
        default=None,
        metadata={
            "name": "ThingShadowDistanceMultiplier",
            "type": "Element",
            "required": True,
        },
    )
    render_distance: Optional[str] = field(
        default=None,
        metadata={
            "name": "RenderDistance",
            "type": "Element",
        },
    )
    world_origin: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WorldOrigin",
            "type": "Element",
            "required": True,
        },
    )
    brightness: Optional[int] = field(
        default=None,
        metadata={
            "name": "Brightness",
            "type": "Element",
            "required": True,
        },
    )
    field_of_view: Optional[int] = field(
        default=None,
        metadata={
            "name": "FieldOfView",
            "type": "Element",
            "required": True,
        },
    )
    color_blind: Optional[str] = field(
        default=None,
        metadata={
            "name": "ColorBlind",
            "type": "Element",
        },
    )
    particle_quality: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParticleQuality",
            "type": "Element",
        },
    )
    soft_particles: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SoftParticles",
            "type": "Element",
            "required": True,
        },
    )
    environment_elements: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EnvironmentElements",
            "type": "Element",
            "required": True,
        },
    )
    extended_terrain: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ExtendedTerrain",
            "type": "Element",
            "required": True,
        },
    )
    volume_light: Optional[str] = field(
        default=None,
        metadata={
            "name": "VolumeLight",
            "type": "Element",
        },
    )
    pixel_light_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "PixelLightCount",
            "type": "Element",
            "required": True,
        },
    )
    max_thing_lights: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxThingLights",
            "type": "Element",
            "required": True,
        },
    )
    antialiasing: Optional[str] = field(
        default=None,
        metadata={
            "name": "Antialiasing",
            "type": "Element",
        },
    )
    frame_lock: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrameLock",
            "type": "Element",
        },
    )
    atmospheric_scattering: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AtmosphericScattering",
            "type": "Element",
            "required": True,
        },
    )
    ambient_occlusion: Optional[str] = field(
        default=None,
        metadata={
            "name": "AmbientOcclusion",
            "type": "Element",
        },
    )
    lens_flares: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LensFlares",
            "type": "Element",
            "required": True,
        },
    )
    disable_water_visualizer: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DisableWaterVisualizer",
            "type": "Element",
            "required": True,
        },
    )
    clouds: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Clouds",
            "type": "Element",
            "required": True,
        },
    )
    helmet_overlay: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HelmetOverlay",
            "type": "Element",
            "required": True,
        },
    )
    weather_event_quality: Optional[str] = field(
        default=None,
        metadata={
            "name": "WeatherEventQuality",
            "type": "Element",
        },
    )
    terrain_detail: Optional[str] = field(
        default=None,
        metadata={
            "name": "TerrainDetail",
            "type": "Element",
        },
    )
    minable_distance: Optional[str] = field(
        default=None,
        metadata={
            "name": "MinableDistance",
            "type": "Element",
        },
    )
    terrain_distance: Optional[str] = field(
        default=None,
        metadata={
            "name": "TerrainDistance",
            "type": "Element",
        },
    )
    master_volume: Optional[int] = field(
        default=None,
        metadata={
            "name": "MasterVolume",
            "type": "Element",
            "required": True,
        },
    )
    sound_volume: Optional[int] = field(
        default=None,
        metadata={
            "name": "SoundVolume",
            "type": "Element",
            "required": True,
        },
    )
    voice_notification_volume: Optional[int] = field(
        default=None,
        metadata={
            "name": "VoiceNotificationVolume",
            "type": "Element",
            "required": True,
        },
    )
    music_volume: Optional[int] = field(
        default=None,
        metadata={
            "name": "MusicVolume",
            "type": "Element",
            "required": True,
        },
    )
    interface_volume: Optional[int] = field(
        default=None,
        metadata={
            "name": "InterfaceVolume",
            "type": "Element",
            "required": True,
        },
    )
    virtual_voices: Optional[int] = field(
        default=None,
        metadata={
            "name": "VirtualVoices",
            "type": "Element",
            "required": True,
        },
    )
    real_voices: Optional[int] = field(
        default=None,
        metadata={
            "name": "RealVoices",
            "type": "Element",
            "required": True,
        },
    )
    user_speaker_mode: Optional[AudioSpeakerMode] = field(
        default=None,
        metadata={
            "name": "UserSpeakerMode",
            "type": "Element",
            "required": True,
        },
    )
    server_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServerName",
            "type": "Element",
        },
    )
    start_local_host: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StartLocalHost",
            "type": "Element",
            "required": True,
        },
    )
    server_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ServerVisible",
            "type": "Element",
            "required": True,
        },
    )
    server_password: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServerPassword",
            "type": "Element",
        },
    )
    admin_password: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdminPassword",
            "type": "Element",
        },
    )
    server_auth_secret: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServerAuthSecret",
            "type": "Element",
        },
    )
    server_max_players: Optional[int] = field(
        default=None,
        metadata={
            "name": "ServerMaxPlayers",
            "type": "Element",
            "required": True,
        },
    )
    update_port: Optional[str] = field(
        default=None,
        metadata={
            "name": "UpdatePort",
            "type": "Element",
        },
    )
    game_port: Optional[str] = field(
        default=None,
        metadata={
            "name": "GamePort",
            "type": "Element",
        },
    )
    upnpenabled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UPNPEnabled",
            "type": "Element",
            "required": True,
        },
    )
    use_steam_p2_p: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseSteamP2P",
            "type": "Element",
            "required": True,
        },
    )
    disconnect_timeout: Optional[int] = field(
        default=None,
        metadata={
            "name": "DisconnectTimeout",
            "type": "Element",
            "required": True,
        },
    )
    network_debug_frequency: Optional[int] = field(
        default=None,
        metadata={
            "name": "NetworkDebugFrequency",
            "type": "Element",
            "required": True,
        },
    )
    local_ip_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocalIpAddress",
            "type": "Element",
        },
    )
    auto_pause_server: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AutoPauseServer",
            "type": "Element",
            "required": True,
        },
    )
    language_code: Optional[LanguageCode] = field(
        default=None,
        metadata={
            "name": "LanguageCode",
            "type": "Element",
            "required": True,
        },
    )
    voice_language_code: Optional[LanguageCode] = field(
        default=None,
        metadata={
            "name": "VoiceLanguageCode",
            "type": "Element",
            "required": True,
        },
    )
    voice: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Voice",
            "type": "Element",
            "required": True,
        },
    )
    popup_chat: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PopupChat",
            "type": "Element",
            "required": True,
        },
    )
    camera_sensitivity: Optional[int] = field(
        default=None,
        metadata={
            "name": "CameraSensitivity",
            "type": "Element",
            "required": True,
        },
    )
    keyboard: Optional[ArrayOfKeyItem] = field(
        default=None,
        metadata={
            "name": "Keyboard",
            "type": "Element",
        },
    )
    invert_mouse: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InvertMouse",
            "type": "Element",
            "required": True,
        },
    )
    invert_mouse_wheel_inventory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InvertMouseWheelInventory",
            "type": "Element",
            "required": True,
        },
    )
    menu_lite: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MenuLite",
            "type": "Element",
            "required": True,
        },
    )
    mouse_wheel_zoom: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MouseWheelZoom",
            "type": "Element",
            "required": True,
        },
    )
    first_run: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FirstRun",
            "type": "Element",
            "required": True,
        },
    )
    voice_notifications: Optional[ArrayOfVoiceNotificationData] = field(
        default=None,
        metadata={
            "name": "VoiceNotifications",
            "type": "Element",
        },
    )
    completed_tutorials: Optional[ArrayOfLong] = field(
        default=None,
        metadata={
            "name": "CompletedTutorials",
            "type": "Element",
        },
    )
    completed_scenarios: Optional[ArrayOfLong] = field(
        default=None,
        metadata={
            "name": "CompletedScenarios",
            "type": "Element",
        },
    )
    display_helper_hints: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DisplayHelperHints",
            "type": "Element",
            "required": True,
        },
    )
    auto_expand_helper_hints: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AutoExpandHelperHints",
            "type": "Element",
            "required": True,
        },
    )
    vertical_movement_axis: Optional[ControllerData] = field(
        default=None,
        metadata={
            "name": "VerticalMovementAxis",
            "type": "Element",
        },
    )
    horizontal_movement_axis: Optional[ControllerData] = field(
        default=None,
        metadata={
            "name": "HorizontalMovementAxis",
            "type": "Element",
        },
    )
    forward_movement_axis: Optional[ControllerData] = field(
        default=None,
        metadata={
            "name": "ForwardMovementAxis",
            "type": "Element",
        },
    )
    vertical_look_axis: Optional[ControllerData] = field(
        default=None,
        metadata={
            "name": "VerticalLookAxis",
            "type": "Element",
        },
    )
    horizontal_look_axis: Optional[ControllerData] = field(
        default=None,
        metadata={
            "name": "HorizontalLookAxis",
            "type": "Element",
        },
    )
    use_custom_work_threads_count: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseCustomWorkThreadsCount",
            "type": "Element",
            "required": True,
        },
    )
    min_worker_threads: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinWorkerThreads",
            "type": "Element",
            "required": True,
        },
    )
    min_completion_port_threads: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinCompletionPortThreads",
            "type": "Element",
            "required": True,
        },
    )
    max_worker_threads: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxWorkerThreads",
            "type": "Element",
            "required": True,
        },
    )
    max_completion_port_threads: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxCompletionPortThreads",
            "type": "Element",
            "required": True,
        },
    )
    max_concurrent_workers: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxConcurrentWorkers",
            "type": "Element",
            "required": True,
        },
    )
    coroutine_time_budget: Optional[float] = field(
        default=None,
        metadata={
            "name": "CoroutineTimeBudget",
            "type": "Element",
            "required": True,
        },
    )
    smooth_terrain: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SmoothTerrain",
            "type": "Element",
            "required": True,
        },
    )
    smooth_terrain_angle: Optional[float] = field(
        default=None,
        metadata={
            "name": "SmoothTerrainAngle",
            "type": "Element",
            "required": True,
        },
    )
    console_buffer_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "ConsoleBufferSize",
            "type": "Element",
            "required": True,
        },
    )
    legacy_cpu: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LegacyCpu",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SiteNodeReference(TemplateNodeReference):
    survey_points: Optional[IntReference] = field(
        default=None,
        metadata={
            "name": "SurveyPoints",
            "type": "Element",
        },
    )
    mineable_deposit: Optional[MineableDepositSaveData] = field(
        default=None,
        metadata={
            "name": "MineableDeposit",
            "type": "Element",
        },
    )


@dataclass
class SpaceMapSpriteData(DataCollection):
    map_display: Optional[MapDisplayData] = field(
        default=None,
        metadata={
            "name": "MapDisplay",
            "type": "Element",
        },
    )


@dataclass
class SpawnData(DataCollection):
    species: list[Species] = field(
        default_factory=list,
        metadata={
            "name": "Species",
            "type": "Element",
        },
    )
    difficulty: list[Difficulty] = field(
        default_factory=list,
        metadata={
            "name": "Difficulty",
            "type": "Element",
        },
    )
    survival_property: list[SurvivalPropertyAction] = field(
        default_factory=list,
        metadata={
            "name": "SurvivalProperty",
            "type": "Element",
        },
    )
    item: list[DynamicSpawnData] = field(
        default_factory=list,
        metadata={
            "name": "Item",
            "type": "Element",
        },
    )
    dynamic_thing: list[DynamicSpawnData] = field(
        default_factory=list,
        metadata={
            "name": "DynamicThing",
            "type": "Element",
        },
    )
    structure: list[StructureSpawnData] = field(
        default_factory=list,
        metadata={
            "name": "Structure",
            "type": "Element",
        },
    )
    world_atmosphere: list[WorldAtmosphereSpawnData] = field(
        default_factory=list,
        metadata={
            "name": "WorldAtmosphere",
            "type": "Element",
        },
    )
    spawn: list[SpawnData] = field(
        default_factory=list,
        metadata={
            "name": "Spawn",
            "type": "Element",
        },
    )
    position_list: list[SpawnPositionListData] = field(
        default_factory=list,
        metadata={
            "name": "PositionList",
            "type": "Element",
        },
    )
    event: Optional[SpawnEvent] = field(
        default=None,
        metadata={
            "name": "Event",
            "type": "Attribute",
            "required": True,
        },
    )
    hide_in_start_screen: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HideInStartScreen",
            "type": "Attribute",
            "required": True,
        },
    )
    show_in_spawn_menu: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ShowInSpawnMenu",
            "type": "Attribute",
            "required": True,
        },
    )
    start_screen_header: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartScreenHeader",
            "type": "Attribute",
        },
    )


@dataclass
class StartLocationData(DataCollection):
    position: Optional[Vector2Reference] = field(
        default=None,
        metadata={
            "name": "Position",
            "type": "Element",
        },
    )
    spawn_radius: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "SpawnRadius",
            "type": "Element",
        },
    )
    description: Optional[LocalizedStringReference] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
        },
    )


@dataclass
class StationBuildCostInsert:
    printer_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrinterName",
            "type": "Element",
        },
    )
    tier_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "TierName",
            "type": "Element",
        },
    )
    details: Optional[str] = field(
        default=None,
        metadata={
            "name": "Details",
            "type": "Element",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
        },
    )
    page_link: Optional[str] = field(
        default=None,
        metadata={
            "name": "PageLink",
            "type": "Element",
        },
    )
    printer_image: Optional[Sprite] = field(
        default=None,
        metadata={
            "name": "PrinterImage",
            "type": "Element",
        },
    )


@dataclass
class StationCategoryInsert:
    name_of_thing: Optional[str] = field(
        default=None,
        metadata={
            "name": "NameOfThing",
            "type": "Element",
        },
    )
    prefab_hash: Optional[int] = field(
        default=None,
        metadata={
            "name": "PrefabHash",
            "type": "Element",
            "required": True,
        },
    )
    page_link: Optional[str] = field(
        default=None,
        metadata={
            "name": "PageLink",
            "type": "Element",
        },
    )
    insert_image: Optional[Sprite] = field(
        default=None,
        metadata={
            "name": "InsertImage",
            "type": "Element",
        },
    )


@dataclass
class StationSlotsInsert:
    slot_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SlotName",
            "type": "Element",
        },
    )
    slot_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "SlotType",
            "type": "Element",
        },
    )
    slot_index: Optional[str] = field(
        default=None,
        metadata={
            "name": "SlotIndex",
            "type": "Element",
        },
    )
    slot_icon: Optional[Sprite] = field(
        default=None,
        metadata={
            "name": "SlotIcon",
            "type": "Element",
        },
    )


@dataclass
class StationStructureVersionInsert:
    structure_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "StructureVersion",
            "type": "Element",
        },
    )
    creation_multiplier: Optional[str] = field(
        default=None,
        metadata={
            "name": "CreationMultiplier",
            "type": "Element",
        },
    )
    energy_cost_multiplier: Optional[str] = field(
        default=None,
        metadata={
            "name": "EnergyCostMultiplier",
            "type": "Element",
        },
    )
    material_cost_multiplier: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaterialCostMultiplier",
            "type": "Element",
        },
    )
    build_time_multiplier: Optional[str] = field(
        default=None,
        metadata={
            "name": "BuildTimeMultiplier",
            "type": "Element",
        },
    )
    structure_image: Optional[Sprite] = field(
        default=None,
        metadata={
            "name": "StructureImage",
            "type": "Element",
        },
    )


@dataclass
class SynodicRotation(CelestialRotation):
    days: Optional[float] = field(
        default=None,
        metadata={
            "name": "Days",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TerraformingGasCurveData(AnimationCurveData):
    gas: list[GasTypeValue] = field(
        default_factory=list,
        metadata={
            "name": "Gas",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass
class TerrainProps:
    terrain_prop: list[LavaLakeProp] = field(
        default_factory=list,
        metadata={
            "name": "TerrainProp",
            "type": "Element",
        },
    )


@dataclass
class ThingSaveData(ReferencableSaveData):
    prefab_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrefabName",
            "type": "Element",
        },
    )
    custom_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomName",
            "type": "Element",
        },
    )
    world_position: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "WorldPosition",
            "type": "Element",
            "required": True,
        },
    )
    world_rotation: Optional[Quaternion] = field(
        default=None,
        metadata={
            "name": "WorldRotation",
            "type": "Element",
            "required": True,
        },
    )
    states: Optional[ArrayOfInteractableState] = field(
        default=None,
        metadata={
            "name": "States",
            "type": "Element",
        },
    )
    is_custom_name: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsCustomName",
            "type": "Element",
            "required": True,
        },
    )
    custom_color_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "CustomColorIndex",
            "type": "Element",
            "required": True,
        },
    )
    owner_steam_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "OwnerSteamId",
            "type": "Element",
            "required": True,
        },
    )
    reagents: Optional[ArrayOfReagentSaveData] = field(
        default=None,
        metadata={
            "name": "Reagents",
            "type": "Element",
        },
    )
    indestructable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Indestructable",
            "type": "Element",
            "required": True,
        },
    )
    damage_state: Optional[DamageUpdate] = field(
        default=None,
        metadata={
            "name": "DamageState",
            "type": "Element",
            "required": True,
        },
    )
    logic_stack: Optional[LogicStackData] = field(
        default=None,
        metadata={
            "name": "LogicStack",
            "type": "Element",
        },
    )


@dataclass
class TidalLocking(CelestialRotation):
    pass


@dataclass
class TraderInstanceSaveData:
    reference_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ReferenceId",
            "type": "Element",
            "required": True,
        },
    )
    trader_data_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "TraderDataId",
            "type": "Element",
            "required": True,
        },
    )
    seed: Optional[int] = field(
        default=None,
        metadata={
            "name": "Seed",
            "type": "Element",
            "required": True,
        },
    )
    buy_save_data: Optional[ArrayOfBuySaveData] = field(
        default=None,
        metadata={
            "name": "BuySaveData",
            "type": "Element",
        },
    )
    sell_save_data: Optional[ArrayOfSellSaveData] = field(
        default=None,
        metadata={
            "name": "SellSaveData",
            "type": "Element",
        },
    )
    checksum: Optional[str] = field(
        default=None,
        metadata={
            "name": "Checksum",
            "type": "Element",
        },
    )


@dataclass
class TransactionData(DataCollection):
    type_value: list[SlotIdReference] = field(
        default_factory=list,
        metadata={
            "name": "Type",
            "type": "Element",
        },
    )
    thumbnail: Optional[StringReference] = field(
        default=None,
        metadata={
            "name": "Thumbnail",
            "type": "Element",
        },
    )
    random_pool: Optional[RandomPoolData] = field(
        default=None,
        metadata={
            "name": "RandomPool",
            "type": "Element",
        },
    )
    chance: Optional[ChanceData] = field(
        default=None,
        metadata={
            "name": "Chance",
            "type": "Element",
        },
    )
    world: Optional[WorldCondition] = field(
        default=None,
        metadata={
            "name": "World",
            "type": "Element",
        },
    )
    worlds: Optional[WorldCollection] = field(
        default=None,
        metadata={
            "name": "Worlds",
            "type": "Element",
        },
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )
    custom_tool_tip_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomToolTipKey",
            "type": "Attribute",
        },
    )


@dataclass
class TraversableNodeReference(TemplateNodeReference):
    chart_points: Optional[IntReference] = field(
        default=None,
        metadata={
            "name": "ChartPoints",
            "type": "Element",
        },
    )
    discover_points: Optional[IntReference] = field(
        default=None,
        metadata={
            "name": "DiscoverPoints",
            "type": "Element",
        },
    )
    is_charted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsCharted",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class UserInterfaceSaveData:
    open_slots: Optional[ArrayOfWindowSaveData] = field(
        default=None,
        metadata={
            "name": "OpenSlots",
            "type": "Element",
        },
    )
    selected_button: Optional[int] = field(
        default=None,
        metadata={
            "name": "SelectedButton",
            "type": "Element",
            "required": True,
        },
    )
    active_hand_slot: Optional[int] = field(
        default=None,
        metadata={
            "name": "ActiveHandSlot",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class VeinGenerationData(DataCollection):
    direction: Optional[VeinDirectionData] = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Element",
        },
    )
    branch_attempts: Optional[BranchAttemptsData] = field(
        default=None,
        metadata={
            "name": "BranchAttempts",
            "type": "Element",
        },
    )
    momentum: Optional[MomentumData] = field(
        default=None,
        metadata={
            "name": "Momentum",
            "type": "Element",
        },
    )
    thickness: Optional[ThicknessData] = field(
        default=None,
        metadata={
            "name": "Thickness",
            "type": "Element",
        },
    )
    seek_surface: Optional[SeekSurfaceData] = field(
        default=None,
        metadata={
            "name": "SeekSurface",
            "type": "Element",
        },
    )
    seek_depth: Optional[SeekDepthData] = field(
        default=None,
        metadata={
            "name": "SeekDepth",
            "type": "Element",
        },
    )
    type_value: Optional[MinableType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    weight: Optional[float] = field(
        default=None,
        metadata={
            "name": "Weight",
            "type": "Attribute",
            "required": True,
        },
    )
    max_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxSize",
            "type": "Attribute",
            "required": True,
        },
    )
    max_depth: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxDepth",
            "type": "Attribute",
            "required": True,
        },
    )
    min_drop_quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinDropQuantity",
            "type": "Attribute",
            "required": True,
        },
    )
    max_drop_quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxDropQuantity",
            "type": "Attribute",
            "required": True,
        },
    )
    mining_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "MiningTime",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Worlds(WorldCollection):
    class Meta:
        nillable = True


@dataclass
class ArrayOfCelestialBodyTemplate:
    celestial_body: list[CelestialBodyTemplate] = field(
        default_factory=list,
        metadata={
            "name": "CelestialBody",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfGameAudioEvent:
    event: list[GameAudioEvent] = field(
        default_factory=list,
        metadata={
            "name": "Event",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfGlobalPlantSaveData:
    global_plant_save_data: list[GlobalPlantSaveData] = field(
        default_factory=list,
        metadata={
            "name": "GlobalPlantSaveData",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfLogicStateSave:
    logic_state: list[LogicStateSave] = field(
        default_factory=list,
        metadata={
            "name": "LogicState",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfRecipeData:
    recipe_data: list[RecipeData] = field(
        default_factory=list,
        metadata={
            "name": "RecipeData",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfResearchData:
    research_data: list[ResearchData] = field(
        default_factory=list,
        metadata={
            "name": "ResearchData",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfStationBuildCostInsert:
    station_build_cost_insert: list[StationBuildCostInsert] = field(
        default_factory=list,
        metadata={
            "name": "StationBuildCostInsert",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfStationCategoryInsert:
    station_category_insert: list[StationCategoryInsert] = field(
        default_factory=list,
        metadata={
            "name": "StationCategoryInsert",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfStationSlotsInsert:
    station_slots_insert: list[StationSlotsInsert] = field(
        default_factory=list,
        metadata={
            "name": "StationSlotsInsert",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfStationStructureVersionInsert:
    station_structure_version_insert: list[StationStructureVersionInsert] = field(
        default_factory=list,
        metadata={
            "name": "StationStructureVersionInsert",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfThingSaveData:
    thing_save_data: list[ThingSaveData] = field(
        default_factory=list,
        metadata={
            "name": "ThingSaveData",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class BuyItem(TradableItem):
    conditions: list[ConditionDataCollection] = field(
        default_factory=list,
        metadata={
            "name": "Conditions",
            "type": "Element",
        },
    )
    temperature: list[TemperatureComparableCondition] = field(
        default_factory=list,
        metadata={
            "name": "Temperature",
            "type": "Element",
        },
    )
    reagents: list[ReagentCondition] = field(
        default_factory=list,
        metadata={
            "name": "Reagents",
            "type": "Element",
        },
    )
    interactable: list[InteractableCondition] = field(
        default_factory=list,
        metadata={
            "name": "Interactable",
            "type": "Element",
        },
    )
    quantity: list[Quantity] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
        },
    )
    decay: list[Decay] = field(
        default_factory=list,
        metadata={
            "name": "Decay",
            "type": "Element",
        },
    )
    gas: list[GasCondition] = field(
        default_factory=list,
        metadata={
            "name": "Gas",
            "type": "Element",
        },
    )
    pressure: list[PressureCondition] = field(
        default_factory=list,
        metadata={
            "name": "Pressure",
            "type": "Element",
        },
    )
    temperature_range: list[TemperatureRangeCondition] = field(
        default_factory=list,
        metadata={
            "name": "TemperatureRange",
            "type": "Element",
        },
    )
    percent: list[Percent] = field(
        default_factory=list,
        metadata={
            "name": "Percent",
            "type": "Element",
        },
    )
    item: list[Item] = field(
        default_factory=list,
        metadata={
            "name": "Item",
            "type": "Element",
        },
    )
    moles: list[Moles] = field(
        default_factory=list,
        metadata={
            "name": "Moles",
            "type": "Element",
        },
    )
    charge: list[Energy] = field(
        default_factory=list,
        metadata={
            "name": "Charge",
            "type": "Element",
        },
    )
    difficulty: list[Difficulty] = field(
        default_factory=list,
        metadata={
            "name": "Difficulty",
            "type": "Element",
        },
    )
    species: list[Species] = field(
        default_factory=list,
        metadata={
            "name": "Species",
            "type": "Element",
        },
    )


@dataclass
class CelestialBodyReference(CelestialReference):
    fixed_rotation: Optional[FixedRotation] = field(
        default=None,
        metadata={
            "name": "FixedRotation",
            "type": "Element",
        },
    )
    synodic_rotation: Optional[SynodicRotation] = field(
        default=None,
        metadata={
            "name": "SynodicRotation",
            "type": "Element",
        },
    )
    tidal_locking: Optional[TidalLocking] = field(
        default=None,
        metadata={
            "name": "TidalLocking",
            "type": "Element",
        },
    )
    parent: Optional[str] = field(
        default=None,
        metadata={
            "name": "Parent",
            "type": "Attribute",
        },
    )


@dataclass
class CelestialConstants(CelestialConstantsReference):
    class Meta:
        nillable = True


@dataclass
class ContactSlotData:
    icon: Optional[SlotIcon] = field(
        default=None,
        metadata={
            "name": "Icon",
            "type": "Element",
        },
    )
    minimum_watts_visible: Optional[FloatRangeData] = field(
        default=None,
        metadata={
            "name": "MinimumWattsVisible",
            "type": "Element",
        },
    )
    watts_to_resolve: Optional[FloatRangeData] = field(
        default=None,
        metadata={
            "name": "WattsToResolve",
            "type": "Element",
        },
    )
    minimum_watts_to_contact: Optional[FloatRangeData] = field(
        default=None,
        metadata={
            "name": "MinimumWattsToContact",
            "type": "Element",
        },
    )
    seconds_to_contact: Optional[FloatRangeData] = field(
        default=None,
        metadata={
            "name": "SecondsToContact",
            "type": "Element",
        },
    )
    life_time: Optional[FloatRangeData] = field(
        default=None,
        metadata={
            "name": "LifeTime",
            "type": "Element",
        },
    )
    down_time: Optional[FloatRangeData] = field(
        default=None,
        metadata={
            "name": "DownTime",
            "type": "Element",
        },
    )
    bulk: Optional[BulkMultiplier] = field(
        default=None,
        metadata={
            "name": "Bulk",
            "type": "Element",
        },
    )
    select: Optional[Select] = field(
        default=None,
        metadata={
            "name": "Select",
            "type": "Element",
        },
    )
    trader: Optional[TraderSlotTraderSelectData] = field(
        default=None,
        metadata={
            "name": "Trader",
            "type": "Element",
        },
    )
    world: Optional[TraderSlotWorldData] = field(
        default=None,
        metadata={
            "name": "World",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass
class CustomThingData:
    blueprint: Optional[BlueprintData] = field(
        default=None,
        metadata={
            "name": "Blueprint",
            "type": "Element",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        },
    )


@dataclass
class DeepMinablesGenerationData(DataCollection):
    region: list[RegionCondition] = field(
        default_factory=list,
        metadata={
            "name": "Region",
            "type": "Element",
        },
    )
    conditions: list[ConditionDataCollection] = field(
        default_factory=list,
        metadata={
            "name": "Conditions",
            "type": "Element",
        },
    )
    quantity: Optional[IntRangeData] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
        },
    )
    time: Optional[IntRangeData] = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Element",
        },
    )
    reagent_mix: Optional[SetReagents] = field(
        default=None,
        metadata={
            "name": "ReagentMix",
            "type": "Element",
        },
    )


@dataclass
class DetailTextureGroup:
    albedo: Optional[TextureReference] = field(
        default=None,
        metadata={
            "name": "Albedo",
            "type": "Element",
        },
    )
    normal: Optional[NormalMapReference] = field(
        default=None,
        metadata={
            "name": "Normal",
            "type": "Element",
        },
    )
    displacement: Optional[TextureReferenceWithValue] = field(
        default=None,
        metadata={
            "name": "Displacement",
            "type": "Element",
        },
    )
    roughness: Optional[TextureReferenceWithValue] = field(
        default=None,
        metadata={
            "name": "Roughness",
            "type": "Element",
        },
    )
    emissive: Optional[TextureReferenceWithValue] = field(
        default=None,
        metadata={
            "name": "Emissive",
            "type": "Element",
        },
    )


@dataclass
class DynamicThingSaveData(ThingSaveData):
    parent_reference_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParentReferenceId",
            "type": "Element",
            "required": True,
        },
    )
    parent_slot_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParentSlotId",
            "type": "Element",
            "required": True,
        },
    )
    dragged: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Dragged",
            "type": "Element",
            "required": True,
        },
    )
    drag_offset: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "DragOffset",
            "type": "Element",
            "required": True,
        },
    )
    velocity: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "Velocity",
            "type": "Element",
            "required": True,
        },
    )
    angular_velocity: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "AngularVelocity",
            "type": "Element",
            "required": True,
        },
    )
    health_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "HealthCurrent",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class GlobalAtmosphereData:
    temperature: Optional[AnimationCurveData] = field(
        default=None,
        metadata={
            "name": "Temperature",
            "type": "Element",
        },
    )
    solar_radiation_temperature: Optional[GlobalTemperatureCurveOffset] = field(
        default=None,
        metadata={
            "name": "SolarRadiationTemperature",
            "type": "Element",
        },
    )
    ghgtemperature_offset: Optional[GlobalTemperatureCurveOffset] = field(
        default=None,
        metadata={
            "name": "GHGTemperatureOffset",
            "type": "Element",
        },
    )
    density_offset: Optional[GlobalTemperatureCurveOffset] = field(
        default=None,
        metadata={
            "name": "DensityOffset",
            "type": "Element",
        },
    )
    gas: Optional[GlobalGasMixData] = field(
        default=None,
        metadata={
            "name": "Gas",
            "type": "Element",
        },
    )
    volume: Optional[DoubleReference] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
        },
    )


@dataclass
class ItemModData(DynamicThingModData):
    inventory_scale: Optional[float] = field(
        default=None,
        metadata={
            "name": "InventoryScale",
            "type": "Element",
            "required": True,
        },
    )
    created_reagent_mixture: Optional[ReagentMixture] = field(
        default=None,
        metadata={
            "name": "CreatedReagentMixture",
            "type": "Element",
        },
    )


@dataclass
class LanderCapsuleSaveData(ThingSaveData):
    pass


@dataclass
class MacroTextureData:
    macro_texture_blend: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "MacroTextureBlend",
            "type": "Element",
        },
    )
    albedo: Optional[TextureReference] = field(
        default=None,
        metadata={
            "name": "Albedo",
            "type": "Element",
        },
    )
    normal: Optional[NormalMapReference] = field(
        default=None,
        metadata={
            "name": "Normal",
            "type": "Element",
        },
    )


@dataclass
class MinablesGenerationData(DataCollection):
    ore_vein: list[VeinGenerationData] = field(
        default_factory=list,
        metadata={
            "name": "OreVein",
            "type": "Element",
        },
    )
    conditions: list[ConditionDataCollection] = field(
        default_factory=list,
        metadata={
            "name": "Conditions",
            "type": "Element",
        },
    )
    region: list[RegionCondition] = field(
        default_factory=list,
        metadata={
            "name": "Region",
            "type": "Element",
        },
    )
    difficulty: list[Difficulty] = field(
        default_factory=list,
        metadata={
            "name": "Difficulty",
            "type": "Element",
        },
    )
    surface: list[SurfaceCondition] = field(
        default_factory=list,
        metadata={
            "name": "Surface",
            "type": "Element",
        },
    )
    depth: list[DepthCondition] = field(
        default_factory=list,
        metadata={
            "name": "Depth",
            "type": "Element",
        },
    )
    ore_density: Optional[float] = field(
        default=None,
        metadata={
            "name": "OreDensity",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class MineableDepositData:
    density: Optional[IntRangeData] = field(
        default=None,
        metadata={
            "name": "Density",
            "type": "Element",
        },
    )
    richness: Optional[IntRangeData] = field(
        default=None,
        metadata={
            "name": "Richness",
            "type": "Element",
        },
    )
    size: Optional[IntRangeData] = field(
        default=None,
        metadata={
            "name": "Size",
            "type": "Element",
        },
    )
    composition: Optional[DepositCompositionData] = field(
        default=None,
        metadata={
            "name": "Composition",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass
class PlayableAreaData(DataCollection):
    region: list[RegionCondition] = field(
        default_factory=list,
        metadata={
            "name": "Region",
            "type": "Element",
        },
    )
    conditions: list[ConditionDataCollection] = field(
        default_factory=list,
        metadata={
            "name": "Conditions",
            "type": "Element",
        },
    )
    rule: Optional[PlayableAreaRule] = field(
        default=None,
        metadata={
            "name": "Rule",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class PlayableBody(PlayableBodyReference):
    class Meta:
        nillable = True


@dataclass
class PointOfInterest(DataCollection):
    region: Optional[Region] = field(
        default=None,
        metadata={
            "name": "Region",
            "type": "Element",
        },
    )
    achievement: Optional[AchievementData] = field(
        default=None,
        metadata={
            "name": "Achievement",
            "type": "Element",
        },
    )
    description: Optional[LocalizedStringReference] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
        },
    )


@dataclass
class RegionSet(DataCollection):
    region: list[Region] = field(
        default_factory=list,
        metadata={
            "name": "Region",
            "type": "Element",
        },
    )
    texture: Optional[TextureReference] = field(
        default=None,
        metadata={
            "name": "Texture",
            "type": "Element",
        },
    )


@dataclass
class RoomTypeRuleData:
    any: Optional[AnyConditionData] = field(
        default=None,
        metadata={
            "name": "Any",
            "type": "Element",
        },
    )
    all: Optional[AllConditionData] = field(
        default=None,
        metadata={
            "name": "All",
            "type": "Element",
        },
    )
    contains: Optional[ContainsConditionData] = field(
        default=None,
        metadata={
            "name": "Contains",
            "type": "Element",
        },
    )
    smaller_than: Optional[SmallerThanConditionData] = field(
        default=None,
        metadata={
            "name": "SmallerThan",
            "type": "Element",
        },
    )
    room_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "RoomType",
            "type": "Attribute",
        },
    )


@dataclass
class RoundRobinStartLocationData(StartLocationData):
    start_location: list[StartLocationData] = field(
        default_factory=list,
        metadata={
            "name": "StartLocation",
            "type": "Element",
        },
    )


@dataclass
class SelectData:
    trade_items: Optional[ArrayOfTradableItem] = field(
        default=None,
        metadata={
            "name": "TradeItems",
            "type": "Element",
        },
    )


@dataclass
class StartConditionData(DataCollection):
    spawn: list[SpawnData] = field(
        default_factory=list,
        metadata={
            "name": "Spawn",
            "type": "Element",
        },
    )
    description: Optional[LocalizedStringReference] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
        },
    )
    preview_button: Optional[TextureReference] = field(
        default=None,
        metadata={
            "name": "PreviewButton",
            "type": "Element",
        },
    )
    world_inject: Optional[WorldCollection] = field(
        default=None,
        metadata={
            "name": "WorldInject",
            "type": "Element",
        },
    )
    is_default: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsDefault",
            "type": "Attribute",
            "required": True,
        },
    )
    is_brutal: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsBrutal",
            "type": "Attribute",
            "required": True,
        },
    )
    is_terrain_edit: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsTerrainEdit",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class StaticNodeReference(TraversableNodeReference):
    pass


@dataclass
class StationContactData:
    angle: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "Angle",
            "type": "Element",
            "required": True,
        },
    )
    contact_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContactName",
            "type": "Element",
        },
    )
    watts_to_resolve: Optional[float] = field(
        default=None,
        metadata={
            "name": "WattsToResolve",
            "type": "Element",
            "required": True,
        },
    )
    minimum_watts_to_resolve: Optional[float] = field(
        default=None,
        metadata={
            "name": "MinimumWattsToResolve",
            "type": "Element",
            "required": True,
        },
    )
    minimum_watts_to_contact: Optional[float] = field(
        default=None,
        metadata={
            "name": "MinimumWattsToContact",
            "type": "Element",
            "required": True,
        },
    )
    seconds_required_to_contact: Optional[float] = field(
        default=None,
        metadata={
            "name": "SecondsRequiredToContact",
            "type": "Element",
            "required": True,
        },
    )
    contacted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Contacted",
            "type": "Element",
            "required": True,
        },
    )
    lifetime: Optional[float] = field(
        default=None,
        metadata={
            "name": "Lifetime",
            "type": "Element",
            "required": True,
        },
    )
    reference_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ReferenceId",
            "type": "Element",
            "required": True,
        },
    )
    instance_save_data: Optional[TraderInstanceSaveData] = field(
        default=None,
        metadata={
            "name": "InstanceSaveData",
            "type": "Element",
        },
    )
    contact_slot_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ContactSlotId",
            "type": "Element",
            "required": True,
        },
    )
    shuttle_type: Optional[ShuttleType] = field(
        default=None,
        metadata={
            "name": "ShuttleType",
            "type": "Element",
            "required": True,
        },
    )
    required_pad_environment: Optional[SpeciesClass] = field(
        default=None,
        metadata={
            "name": "RequiredPadEnvironment",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class StructureSaveData(ThingSaveData):
    current_build_state: Optional[int] = field(
        default=None,
        metadata={
            "name": "CurrentBuildState",
            "type": "Element",
            "required": True,
        },
    )
    mothership_reference_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "MothershipReferenceId",
            "type": "Element",
            "required": True,
        },
    )
    has_spawned_wreckage: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasSpawnedWreckage",
            "type": "Element",
            "required": True,
        },
    )
    registered_world_position: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "RegisteredWorldPosition",
            "type": "Element",
            "required": True,
        },
    )
    registered_world_rotation: Optional[Quaternion] = field(
        default=None,
        metadata={
            "name": "RegisteredWorldRotation",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ThingSpawnData:
    color: Optional[ColorSwatchReference] = field(
        default=None,
        metadata={
            "name": "Color",
            "type": "Element",
        },
    )
    name: Optional[LocalizedStringReference] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    spawn_position: Optional[SpawnPositionData] = field(
        default=None,
        metadata={
            "name": "SpawnPosition",
            "type": "Element",
        },
    )
    logic: list[LogicValueAction] = field(
        default_factory=list,
        metadata={
            "name": "Logic",
            "type": "Element",
        },
    )
    build_state: list[BuildStateAction] = field(
        default_factory=list,
        metadata={
            "name": "BuildState",
            "type": "Element",
        },
    )
    interaction: list[InteractionAction] = field(
        default_factory=list,
        metadata={
            "name": "Interaction",
            "type": "Element",
        },
    )
    move_player: list[MovePlayerAction] = field(
        default_factory=list,
        metadata={
            "name": "MovePlayer",
            "type": "Element",
        },
    )
    gene: list[GeneAction] = field(
        default_factory=list,
        metadata={
            "name": "Gene",
            "type": "Element",
        },
    )
    quantity: list[QuantityAction] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
        },
    )
    percent: list[PercentAction] = field(
        default_factory=list,
        metadata={
            "name": "Percent",
            "type": "Element",
        },
    )
    reagents: list[SetReagents] = field(
        default_factory=list,
        metadata={
            "name": "Reagents",
            "type": "Element",
        },
    )
    charge: list[ChargeAction] = field(
        default_factory=list,
        metadata={
            "name": "Charge",
            "type": "Element",
        },
    )
    gas: list[GasAction] = field(
        default_factory=list,
        metadata={
            "name": "Gas",
            "type": "Element",
        },
    )
    source_code: list[SourceCodeAction] = field(
        default_factory=list,
        metadata={
            "name": "SourceCode",
            "type": "Element",
        },
    )
    species: list[Species] = field(
        default_factory=list,
        metadata={
            "name": "Species",
            "type": "Element",
        },
    )
    difficulty: list[Difficulty] = field(
        default_factory=list,
        metadata={
            "name": "Difficulty",
            "type": "Element",
        },
    )
    item: list[DynamicSpawnData] = field(
        default_factory=list,
        metadata={
            "name": "Item",
            "type": "Element",
        },
    )
    dynamic_thing: list[DynamicSpawnData] = field(
        default_factory=list,
        metadata={
            "name": "DynamicThing",
            "type": "Element",
        },
    )
    spawn: list[SpawnData] = field(
        default_factory=list,
        metadata={
            "name": "Spawn",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    hide_in_start_screen: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HideInStartScreen",
            "type": "Attribute",
            "required": True,
        },
    )
    expand_in_start_screen: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ExpandInStartScreen",
            "type": "Attribute",
            "required": True,
        },
    )
    show_deep_start_screen_tooltip: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ShowDeepStartScreenTooltip",
            "type": "Attribute",
            "required": True,
        },
    )
    start_screen_header: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartScreenHeader",
            "type": "Attribute",
        },
    )


@dataclass
class WeatherEvent(DataCollection):
    particle_id: Optional[StringReference] = field(
        default=None,
        metadata={
            "name": "ParticleId",
            "type": "Element",
        },
    )
    cool_down: Optional[IntRangeData] = field(
        default=None,
        metadata={
            "name": "CoolDown",
            "type": "Element",
        },
    )
    start_delay: Optional[FloatRangeData] = field(
        default=None,
        metadata={
            "name": "StartDelay",
            "type": "Element",
        },
    )
    duration: Optional[FloatRangeData] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
        },
    )
    storm_effect: Optional[StormEffectData] = field(
        default=None,
        metadata={
            "name": "StormEffect",
            "type": "Element",
        },
    )
    fog: Optional[FogData] = field(
        default=None,
        metadata={
            "name": "Fog",
            "type": "Element",
        },
    )
    temperature_offset: Optional[GlobalTemperatureFloatOffset] = field(
        default=None,
        metadata={
            "name": "TemperatureOffset",
            "type": "Element",
        },
    )
    temperature_offset_curve: Optional[GlobalTemperatureCurveOffset] = field(
        default=None,
        metadata={
            "name": "TemperatureOffsetCurve",
            "type": "Element",
        },
    )
    solar_ratio: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "SolarRatio",
            "type": "Element",
        },
    )
    wind_strength: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "WindStrength",
            "type": "Element",
        },
    )
    damage_multiplier: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "DamageMultiplier",
            "type": "Element",
        },
    )
    movement_speed_multiplier: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "MovementSpeedMultiplier",
            "type": "Element",
        },
    )
    directional_light: Optional[DirectionalLightData] = field(
        default=None,
        metadata={
            "name": "DirectionalLight",
            "type": "Element",
        },
    )
    solar_storm_camera_effect: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "SolarStormCameraEffect",
            "type": "Element",
        },
    )
    shell1_sound: Optional[StringReference] = field(
        default=None,
        metadata={
            "name": "Shell1Sound",
            "type": "Element",
        },
    )
    shell2_sound: Optional[StringReference] = field(
        default=None,
        metadata={
            "name": "Shell2Sound",
            "type": "Element",
        },
    )
    shell3_sound: Optional[StringReference] = field(
        default=None,
        metadata={
            "name": "Shell3Sound",
            "type": "Element",
        },
    )
    shell4_sound: Optional[StringReference] = field(
        default=None,
        metadata={
            "name": "Shell4Sound",
            "type": "Element",
        },
    )
    first_storm_delay: Optional[int] = field(
        default=None,
        metadata={
            "name": "FirstStormDelay",
            "type": "Attribute",
            "required": True,
        },
    )
    wind_sound: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WindSound",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class WorldObjective(DataCollection):
    info: Optional[LocalizedStringReference] = field(
        default=None,
        metadata={
            "name": "Info",
            "type": "Element",
        },
    )
    notice: list[LocalizedStringReference] = field(
        default_factory=list,
        metadata={
            "name": "Notice",
            "type": "Element",
        },
    )
    trigger: Optional[ObjectiveConditionCollection] = field(
        default=None,
        metadata={
            "name": "Trigger",
            "type": "Element",
        },
    )
    cursor_thing: list[CursorThingCondition] = field(
        default_factory=list,
        metadata={
            "name": "CursorThing",
            "type": "Element",
        },
    )
    contact: list[TraderContactCondition] = field(
        default_factory=list,
        metadata={
            "name": "Contact",
            "type": "Element",
        },
    )
    network: list[NetworkCondition] = field(
        default_factory=list,
        metadata={
            "name": "Network",
            "type": "Element",
        },
    )
    objective_complete: list[ObjectiveCompleteCondition] = field(
        default_factory=list,
        metadata={
            "name": "ObjectiveComplete",
            "type": "Element",
        },
    )
    prefab: list[ThingPrefabCondition] = field(
        default_factory=list,
        metadata={
            "name": "Prefab",
            "type": "Element",
        },
    )
    room: list[RoomCondition] = field(
        default_factory=list,
        metadata={
            "name": "Room",
            "type": "Element",
        },
    )
    player: list[EntityStateCondition] = field(
        default_factory=list,
        metadata={
            "name": "Player",
            "type": "Element",
        },
    )
    thing_count: list[ThingCountCondition] = field(
        default_factory=list,
        metadata={
            "name": "ThingCount",
            "type": "Element",
        },
    )
    conditions: list[ObjectiveConditionCollection] = field(
        default_factory=list,
        metadata={
            "name": "Conditions",
            "type": "Element",
        },
    )
    complete_tutorial_popup: list[CompletedTutorialPopupAction] = field(
        default_factory=list,
        metadata={
            "name": "CompleteTutorialPopup",
            "type": "Element",
        },
    )
    popup: list[PopupAction] = field(
        default_factory=list,
        metadata={
            "name": "Popup",
            "type": "Element",
        },
    )
    expand: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Expand",
            "type": "Attribute",
            "required": True,
        },
    )
    time: Optional[float] = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class AdvancedTabletSaveData(DynamicThingSaveData):
    current_indexed_slot: Optional[int] = field(
        default=None,
        metadata={
            "name": "CurrentIndexedSlot",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ArrayOfDynamicThingSaveData:
    dynamic_thing_save_data: list[DynamicThingSaveData] = field(
        default_factory=list,
        metadata={
            "name": "DynamicThingSaveData",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class ArrayOfStationContactData:
    station_contact_data: list[StationContactData] = field(
        default_factory=list,
        metadata={
            "name": "StationContactData",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class AtmosphericItemSaveData(DynamicThingSaveData):
    leak_ratio: Optional[float] = field(
        default=None,
        metadata={
            "name": "LeakRatio",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class AudioEventData:
    audio_channels: Optional[ArrayOfChannelData] = field(
        default=None,
        metadata={
            "name": "AudioChannels",
            "type": "Element",
        },
    )
    audio_events: Optional[ArrayOfGameAudioEvent] = field(
        default=None,
        metadata={
            "name": "AudioEvents",
            "type": "Element",
        },
    )


@dataclass
class BasketBaseSaveData(StructureSaveData):
    setting: Optional[int] = field(
        default=None,
        metadata={
            "name": "Setting",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class BatteryCellData(ItemModData):
    power_maximum: Optional[float] = field(
        default=None,
        metadata={
            "name": "PowerMaximum",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class BatteryCellSaveData(DynamicThingSaveData):
    power_stored: Optional[float] = field(
        default=None,
        metadata={
            "name": "PowerStored",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class BatterySaveData(StructureSaveData):
    power_stored: Optional[float] = field(
        default=None,
        metadata={
            "name": "PowerStored",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class BobbleHeadSaveData(DynamicThingSaveData):
    pass


@dataclass
class BrainSaveData(DynamicThingSaveData):
    client_steam_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ClientSteamId",
            "type": "Element",
            "required": True,
        },
    )
    identity: Optional[PlayerCosmetics] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class CableSaveSaveData(StructureSaveData):
    cable_network_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "CableNetworkId",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class CelestialBody(CelestialBodyReference):
    class Meta:
        nillable = True


@dataclass
class CelestialSpriteReference(CelestialBodyReference):
    material: Optional[StarData] = field(
        default=None,
        metadata={
            "name": "Material",
            "type": "Element",
        },
    )
    distance: Optional[ValueRange] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
        },
    )
    magnitude: Optional[float] = field(
        default=None,
        metadata={
            "name": "Magnitude",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ChuteDeviceSaveData(StructureSaveData):
    pass


@dataclass
class ChuteSaveData(StructureSaveData):
    chute_network_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ChuteNetworkId",
            "type": "Element",
            "required": True,
        },
    )
    next_neighbor_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "NextNeighborId",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ConsumableModData(ItemModData):
    max_quantity: Optional[float] = field(
        default=None,
        metadata={
            "name": "MaxQuantity",
            "type": "Element",
            "required": True,
        },
    )
    use_amount: Optional[float] = field(
        default=None,
        metadata={
            "name": "UseAmount",
            "type": "Element",
            "required": True,
        },
    )
    allow_splitting: Optional[str] = field(
        default=None,
        metadata={
            "name": "AllowSplitting",
            "type": "Element",
        },
    )


@dataclass
class ConsumableSaveData(DynamicThingSaveData):
    quantity: Optional[float] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ContactSlot(ContactSlotData):
    class Meta:
        nillable = True


@dataclass
class CrewModuleSaveData(StructureSaveData):
    partner_distance: Optional[int] = field(
        default=None,
        metadata={
            "name": "PartnerDistance",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class CustomItemData(CustomThingData):
    reagents: Optional[ReagentData] = field(
        default=None,
        metadata={
            "name": "Reagents",
            "type": "Element",
        },
    )


@dataclass
class CustomSeedData(CustomThingData):
    mesh: Optional[MeshReference] = field(
        default=None,
        metadata={
            "name": "Mesh",
            "type": "Element",
        },
    )
    texture: Optional[TextureReference] = field(
        default=None,
        metadata={
            "name": "Texture",
            "type": "Element",
        },
    )
    thumbnail: Optional[SpriteReference] = field(
        default=None,
        metadata={
            "name": "Thumbnail",
            "type": "Element",
        },
    )
    plant: Optional[PrefabReference] = field(
        default=None,
        metadata={
            "name": "Plant",
            "type": "Element",
        },
    )


@dataclass
class DeepMinablesRegionData(DataCollection):
    region_set: Optional[RegionSet] = field(
        default=None,
        metadata={
            "name": "RegionSet",
            "type": "Element",
        },
    )


@dataclass
class DetailTextureData:
    group_one: Optional[DetailTextureGroup] = field(
        default=None,
        metadata={
            "name": "GroupOne",
            "type": "Element",
        },
    )
    group_two: Optional[DetailTextureGroup] = field(
        default=None,
        metadata={
            "name": "GroupTwo",
            "type": "Element",
        },
    )
    uvscale: Optional[float] = field(
        default=None,
        metadata={
            "name": "UVScale",
            "type": "Attribute",
            "required": True,
        },
    )
    detail_fade_start: Optional[float] = field(
        default=None,
        metadata={
            "name": "DetailFadeStart",
            "type": "Attribute",
            "required": True,
        },
    )
    detail_fade_end: Optional[float] = field(
        default=None,
        metadata={
            "name": "DetailFadeEnd",
            "type": "Attribute",
            "required": True,
        },
    )
    fractal_depth_scale: Optional[float] = field(
        default=None,
        metadata={
            "name": "FractalDepthScale",
            "type": "Attribute",
            "required": True,
        },
    )
    lod_min: Optional[float] = field(
        default=None,
        metadata={
            "name": "LodMin",
            "type": "Attribute",
            "required": True,
        },
    )
    mipmap_bias: Optional[float] = field(
        default=None,
        metadata={
            "name": "MipmapBias",
            "type": "Attribute",
            "required": True,
        },
    )
    blend_sharpness: Optional[float] = field(
        default=None,
        metadata={
            "name": "BlendSharpness",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class DeviceAtmosphericSaveData(StructureSaveData):
    output_setting: Optional[float] = field(
        default=None,
        metadata={
            "name": "OutputSetting",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DeviceImportSaveData(StructureSaveData):
    import_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "ImportCount",
            "type": "Element",
            "required": True,
        },
    )
    import_state: Optional[int] = field(
        default=None,
        metadata={
            "name": "ImportState",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DiodeSlideSaveData(StructureSaveData):
    setting: Optional[float] = field(
        default=None,
        metadata={
            "name": "Setting",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DirtCanisterSaveData(DynamicThingSaveData):
    current_collected_dirt: Optional[float] = field(
        default=None,
        metadata={
            "name": "CurrentCollectedDirt",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DockSaveData(StructureSaveData):
    linked_dock_reference_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "LinkedDockReferenceID",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DoorSaveData(StructureSaveData):
    setting: Optional[float] = field(
        default=None,
        metadata={
            "name": "Setting",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DynamicComposterSaveData(DynamicThingSaveData):
    unprocessed_items: Optional[int] = field(
        default=None,
        metadata={
            "name": "UnprocessedItems",
            "type": "Element",
            "required": True,
        },
    )
    saved_decay_food_quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "SavedDecayFoodQuantity",
            "type": "Element",
            "required": True,
        },
    )
    saved_normal_food_quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "SavedNormalFoodQuantity",
            "type": "Element",
            "required": True,
        },
    )
    saved_biomass_quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "SavedBiomassQuantity",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DynamicGasCanisterSaveData(DynamicThingSaveData):
    output_setting: Optional[float] = field(
        default=None,
        metadata={
            "name": "OutputSetting",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DynamicSpawnData(ThingSpawnData):
    slot_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SlotId",
            "type": "Attribute",
        },
    )
    slot_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "SlotIndex",
            "type": "Attribute",
            "required": True,
        },
    )
    slot_class: Optional[Class] = field(
        default=None,
        metadata={
            "name": "SlotClass",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class DynamiteSaveData(DynamicThingSaveData):
    lifetime: Optional[float] = field(
        default=None,
        metadata={
            "name": "Lifetime",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ElevatorCarrageSaveData(DynamicThingSaveData):
    level_target: Optional[int] = field(
        default=None,
        metadata={
            "name": "LevelTarget",
            "type": "Element",
            "required": True,
        },
    )
    speed: Optional[float] = field(
        default=None,
        metadata={
            "name": "Speed",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class EntitySaveData(DynamicThingSaveData):
    state: Optional[EntityState] = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Element",
            "required": True,
        },
    )
    oxygenation: Optional[float] = field(
        default=None,
        metadata={
            "name": "Oxygenation",
            "type": "Element",
            "required": True,
        },
    )
    nutrition: Optional[float] = field(
        default=None,
        metadata={
            "name": "Nutrition",
            "type": "Element",
            "required": True,
        },
    )
    hydration: Optional[float] = field(
        default=None,
        metadata={
            "name": "Hydration",
            "type": "Element",
            "required": True,
        },
    )
    mood: Optional[float] = field(
        default=None,
        metadata={
            "name": "Mood",
            "type": "Element",
            "required": True,
        },
    )
    hygiene: Optional[float] = field(
        default=None,
        metadata={
            "name": "Hygiene",
            "type": "Element",
            "required": True,
        },
    )
    food_quality: Optional[float] = field(
        default=None,
        metadata={
            "name": "FoodQuality",
            "type": "Element",
            "required": True,
        },
    )
    respawn_stress_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "RespawnStressTime",
            "type": "Element",
            "required": True,
        },
    )
    movement_controller_control_mode: Optional[int] = field(
        default=None,
        metadata={
            "name": "MovementControllerControlMode",
            "type": "Element",
            "required": True,
        },
    )
    days_lived: Optional[int] = field(
        default=None,
        metadata={
            "name": "DaysLived",
            "type": "Element",
            "required": True,
        },
    )
    current_decay_time: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "CurrentDecayTime",
            "type": "Element",
        },
    )


@dataclass
class FabricatorSaveData(StructureSaveData):
    jobs: Optional[ArrayOfFabricatorJob] = field(
        default=None,
        metadata={
            "name": "Jobs",
            "type": "Element",
        },
    )
    current_job: Optional[FabricatorJob] = field(
        default=None,
        metadata={
            "name": "CurrentJob",
            "type": "Element",
        },
    )
    progress: Optional[float] = field(
        default=None,
        metadata={
            "name": "Progress",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class FertilizedEggSaveData(DynamicThingSaveData):
    egg_hatch_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "EggHatchTime",
            "type": "Element",
            "required": True,
        },
    )
    viable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Viable",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class GasCanisterData(ItemModData):
    max_pressure: Optional[float] = field(
        default=None,
        metadata={
            "name": "MaxPressure",
            "type": "Element",
            "required": True,
        },
    )
    litres: Optional[float] = field(
        default=None,
        metadata={
            "name": "Litres",
            "type": "Element",
            "required": True,
        },
    )
    pressure_per_tick: Optional[float] = field(
        default=None,
        metadata={
            "name": "PressurePerTick",
            "type": "Element",
            "required": True,
        },
    )
    spawn_contents: Optional[ArrayOfSpawnGas] = field(
        default=None,
        metadata={
            "name": "SpawnContents",
            "type": "Element",
        },
    )


@dataclass
class GasCanisterSaveData(DynamicThingSaveData):
    has_blown: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasBlown",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class GeographicRegionData(DataCollection):
    default_region_name: Optional[LocalizedStringReference] = field(
        default=None,
        metadata={
            "name": "DefaultRegionName",
            "type": "Element",
        },
    )
    region_set: Optional[RegionSet] = field(
        default=None,
        metadata={
            "name": "RegionSet",
            "type": "Element",
        },
    )


@dataclass
class GeyserSaveData(StructureSaveData):
    tapped: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Tapped",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class GrenadeSaveData(DynamicThingSaveData):
    lifetime: Optional[float] = field(
        default=None,
        metadata={
            "name": "Lifetime",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ImportExportSaveData(StructureSaveData):
    pass


@dataclass
class LandingPadModularDeviceSaveData(StructureSaveData):
    pad_network_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "PadNetworkId",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LandingPadSaveData(StructureSaveData):
    trader_reference_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "TraderReferenceID",
            "type": "Element",
            "required": True,
        },
    )
    parent_motherboard_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParentMotherboardID",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LaunchMountSaveData(StructureSaveData):
    linked_node_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "LinkedNodeId",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LogicBaseSaveData(StructureSaveData):
    setting: Optional[float] = field(
        default=None,
        metadata={
            "name": "Setting",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LogicMirrorSaveData(StructureSaveData):
    current_device_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "CurrentDeviceId",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class MotherboardSaveData(DynamicThingSaveData):
    linked_device_references: Optional[ArrayOfLong] = field(
        default=None,
        metadata={
            "name": "LinkedDeviceReferences",
            "type": "Element",
        },
    )
    flag: Optional[int] = field(
        default=None,
        metadata={
            "name": "Flag",
            "type": "Element",
            "required": True,
        },
    )
    master_motherboard: Optional[int] = field(
        default=None,
        metadata={
            "name": "MasterMotherboard",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class PadModularSaveData(StructureSaveData):
    pad_network_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "PadNetworkId",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class PictureFrameSaveData(StructureSaveData):
    picture_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "PictureIndex",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class PipeSaveData(StructureSaveData):
    pipe_network_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "PipeNetworkId",
            "type": "Element",
            "required": True,
        },
    )
    is_burst: list[PipeBurstValue] = field(
        default_factory=list,
        metadata={
            "name": "IsBurst",
            "type": "Element",
            "tokens": True,
        },
    )
    damage_record: list[PipeBurstValue] = field(
        default_factory=list,
        metadata={
            "name": "DamageRecord",
            "type": "Element",
            "tokens": True,
        },
    )


@dataclass
class PlantAnalyzerSaveData(DynamicThingSaveData):
    plant_sample: Optional[PlantSample] = field(
        default=None,
        metadata={
            "name": "PlantSample",
            "type": "Element",
        },
    )


@dataclass
class PlantGeneticSplicerSaveData(DynamicThingSaveData):
    splice_time_remaining: Optional[float] = field(
        default=None,
        metadata={
            "name": "SpliceTimeRemaining",
            "type": "Element",
            "required": True,
        },
    )
    gene_to_splice: Optional[int] = field(
        default=None,
        metadata={
            "name": "GeneToSplice",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class PlantSamplerSaveData(DynamicThingSaveData):
    plant_sample: Optional[PlantSample] = field(
        default=None,
        metadata={
            "name": "PlantSample",
            "type": "Element",
        },
    )


@dataclass
class ProgrammableChipSaveData(DynamicThingSaveData):
    registers: list[float] = field(
        default_factory=list,
        metadata={
            "name": "Registers",
            "type": "Element",
        },
    )
    source_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourceCode",
            "type": "Element",
        },
    )
    next_addr: Optional[int] = field(
        default=None,
        metadata={
            "name": "NextAddr",
            "type": "Element",
            "required": True,
        },
    )
    device_lables: Optional[ArrayOfString3] = field(
        default=None,
        metadata={
            "name": "DeviceLables",
            "type": "Element",
        },
    )
    aliases_keys: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AliasesKeys",
            "type": "Element",
        },
    )
    aliases_values: list[int] = field(
        default_factory=list,
        metadata={
            "name": "AliasesValues",
            "type": "Element",
        },
    )
    new_aliases_keys: list[str] = field(
        default_factory=list,
        metadata={
            "name": "NewAliasesKeys",
            "type": "Element",
        },
    )
    new_aliases_values_target: list[int] = field(
        default_factory=list,
        metadata={
            "name": "NewAliasesValuesTarget",
            "type": "Element",
        },
    )
    new_aliases_values_index: list[int] = field(
        default_factory=list,
        metadata={
            "name": "NewAliasesValuesIndex",
            "type": "Element",
        },
    )
    define_keys: list[str] = field(
        default_factory=list,
        metadata={
            "name": "DefineKeys",
            "type": "Element",
        },
    )
    define_values: list[float] = field(
        default_factory=list,
        metadata={
            "name": "DefineValues",
            "type": "Element",
        },
    )
    jump_tags_keys: list[str] = field(
        default_factory=list,
        metadata={
            "name": "JumpTagsKeys",
            "type": "Element",
        },
    )
    jump_tags_values: list[int] = field(
        default_factory=list,
        metadata={
            "name": "JumpTagsValues",
            "type": "Element",
        },
    )
    stack: list[float] = field(
        default_factory=list,
        metadata={
            "name": "Stack",
            "type": "Element",
        },
    )
    sleep_duration_remaining: Optional[float] = field(
        default=None,
        metadata={
            "name": "SleepDurationRemaining",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ProximitySensorSaveData(StructureSaveData):
    setting: Optional[int] = field(
        default=None,
        metadata={
            "name": "Setting",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RemoteDetonatorSaveData(DynamicThingSaveData):
    linked_explosives: list[int] = field(
        default_factory=list,
        metadata={
            "name": "LinkedExplosives",
            "type": "Element",
        },
    )


@dataclass
class ResearchPool:
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Element",
        },
    )
    research_dats: Optional[ArrayOfResearchData] = field(
        default=None,
        metadata={
            "name": "ResearchDats",
            "type": "Element",
        },
    )


@dataclass
class RobotSaveData(DynamicThingSaveData):
    target_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "TargetX",
            "type": "Element",
            "required": True,
        },
    )
    target_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "TargetY",
            "type": "Element",
            "required": True,
        },
    )
    target_z: Optional[float] = field(
        default=None,
        metadata={
            "name": "TargetZ",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RoboticArmDoorSaveData(StructureSaveData):
    pass


@dataclass
class RoboticArmRailBaseSaveData(StructureSaveData):
    robotic_arm_network_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "RoboticArmNetworkId",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RoboticArmRailDeviceBaseSaveData(StructureSaveData):
    robotic_arm_network_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "RoboticArmNetworkId",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RocketAvionicsSaveData(StructureSaveData):
    rocket_reference_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "RocketReferenceId",
            "type": "Element",
            "required": True,
        },
    )
    auto_shut_off: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AutoShutOff",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RocketCelestialTrackerSaveData(StructureSaveData):
    index: Optional[int] = field(
        default=None,
        metadata={
            "name": "Index",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RocketChuteUmbilicalFemaleSaveData(StructureSaveData):
    partner_distance: Optional[int] = field(
        default=None,
        metadata={
            "name": "PartnerDistance",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RocketChuteUmbilicalMaleSaveData(StructureSaveData):
    partner_umbilical_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "PartnerUmbilicalID",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RocketCrewUmbilicalSaveData(StructureSaveData):
    partner_umbilical_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "PartnerUmbilicalId",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RocketDataDownLinkSaveData(StructureSaveData):
    connected_ids: Optional[ArrayOfLong] = field(
        default=None,
        metadata={
            "name": "ConnectedIds",
            "type": "Element",
        },
    )


@dataclass
class RocketDataLinkSaveData(StructureSaveData):
    connected_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ConnectedId",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RocketGasUmbilicalMaleSaveData(StructureSaveData):
    partner_umbilical_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "PartnerUmbilicalId",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RocketPowerUmbilicalFemaleSaveData(StructureSaveData):
    power_stored: Optional[float] = field(
        default=None,
        metadata={
            "name": "PowerStored",
            "type": "Element",
            "required": True,
        },
    )
    partner_distance: Optional[int] = field(
        default=None,
        metadata={
            "name": "PartnerDistance",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RocketPowerUmbilicalMaleSaveData(StructureSaveData):
    power_stored: Optional[float] = field(
        default=None,
        metadata={
            "name": "PowerStored",
            "type": "Element",
            "required": True,
        },
    )
    partner_umbilical_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "PartnerUmbilicalId",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RocketScannerSaveData(StructureSaveData):
    current_cycle_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "CurrentCycleTime",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RotatableSaveData(StructureSaveData):
    horizontal: Optional[float] = field(
        default=None,
        metadata={
            "name": "Horizontal",
            "type": "Element",
            "required": True,
        },
    )
    vertical: Optional[float] = field(
        default=None,
        metadata={
            "name": "Vertical",
            "type": "Element",
            "required": True,
        },
    )
    target_horizontal: Optional[float] = field(
        default=None,
        metadata={
            "name": "TargetHorizontal",
            "type": "Element",
            "required": True,
        },
    )
    target_vertical: Optional[float] = field(
        default=None,
        metadata={
            "name": "TargetVertical",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RoverSaveData(DynamicThingSaveData):
    last_valid_playable_position: Optional[Vector2] = field(
        default=None,
        metadata={
            "name": "LastValidPlayablePosition",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SeedTraySaveData(DynamicThingSaveData):
    pass


@dataclass
class SelectBuyData(SelectData):
    item: list[BuyItem] = field(
        default_factory=list,
        metadata={
            "name": "Item",
            "type": "Element",
        },
    )


@dataclass
class SelectSellData(SelectData):
    item: list[SellItem] = field(
        default_factory=list,
        metadata={
            "name": "Item",
            "type": "Element",
        },
    )


@dataclass
class SolarPanelSaveData(StructureSaveData):
    horizontal: Optional[float] = field(
        default=None,
        metadata={
            "name": "Horizontal",
            "type": "Element",
            "required": True,
        },
    )
    vertical: Optional[float] = field(
        default=None,
        metadata={
            "name": "Vertical",
            "type": "Element",
            "required": True,
        },
    )
    target_horizontal: Optional[float] = field(
        default=None,
        metadata={
            "name": "TargetHorizontal",
            "type": "Element",
            "required": True,
        },
    )
    target_vertical: Optional[float] = field(
        default=None,
        metadata={
            "name": "TargetVertical",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SpaceMapNodeData(DataCollection):
    connection: list[NodeConnectionData] = field(
        default_factory=list,
        metadata={
            "name": "Connection",
            "type": "Element",
        },
    )
    map_display: Optional[MapDisplayData] = field(
        default=None,
        metadata={
            "name": "MapDisplay",
            "type": "Element",
        },
    )
    deposit: Optional[MineableDepositData] = field(
        default=None,
        metadata={
            "name": "Deposit",
            "type": "Element",
        },
    )
    mine: list[SpaceMapNodeMineData] = field(
        default_factory=list,
        metadata={
            "name": "Mine",
            "type": "Element",
        },
    )
    survey: list[SurveyData] = field(
        default_factory=list,
        metadata={
            "name": "Survey",
            "type": "Element",
        },
    )
    discover: list[DiscoverSiteData] = field(
        default_factory=list,
        metadata={
            "name": "Discover",
            "type": "Element",
        },
    )
    chart: list[ChartData] = field(
        default_factory=list,
        metadata={
            "name": "Chart",
            "type": "Element",
        },
    )
    deploy: list[DeployData] = field(
        default_factory=list,
        metadata={
            "name": "Deploy",
            "type": "Element",
        },
    )
    achievement_reached: Optional[AchievementData] = field(
        default=None,
        metadata={
            "name": "AchievementReached",
            "type": "Element",
        },
    )
    code: Optional[int] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        },
    )
    is_charted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsCharted",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SpaceMapSaveData(SerializedId):
    site_node: list[SiteNodeReference] = field(
        default_factory=list,
        metadata={
            "name": "SiteNode",
            "type": "Element",
        },
    )
    static_node: list[StaticNodeReference] = field(
        default_factory=list,
        metadata={
            "name": "StaticNode",
            "type": "Element",
        },
    )
    launch_pad_node: list[LaunchPadNodeReference] = field(
        default_factory=list,
        metadata={
            "name": "LaunchPadNode",
            "type": "Element",
        },
    )


@dataclass
class SpeakerSaveData(StructureSaveData):
    volume: Optional[float] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
            "required": True,
        },
    )
    clip_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "ClipTime",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SphericalBodyBase(CelestialBodyReference):
    color: Optional[ColorRgb] = field(
        default=None,
        metadata={
            "name": "Color",
            "type": "Element",
        },
    )
    texture: Optional[TextureReference] = field(
        default=None,
        metadata={
            "name": "Texture",
            "type": "Element",
        },
    )
    rotation: Optional[Vector3Reference] = field(
        default=None,
        metadata={
            "name": "Rotation",
            "type": "Element",
        },
    )
    radius_km: Optional[float] = field(
        default=None,
        metadata={
            "name": "RadiusKm",
            "type": "Attribute",
            "required": True,
        },
    )
    radius_au: Optional[float] = field(
        default=None,
        metadata={
            "name": "RadiusAu",
            "type": "Attribute",
            "required": True,
        },
    )
    scale: Optional[float] = field(
        default=None,
        metadata={
            "name": "Scale",
            "type": "Attribute",
            "required": True,
        },
    )
    can_occult: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CanOccult",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class StackableModData(ItemModData):
    max_quantity: Optional[float] = field(
        default=None,
        metadata={
            "name": "MaxQuantity",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class StackableSaveData(DynamicThingSaveData):
    quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class StationpediaPage:
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Element",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
        },
    )
    sort_priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "SortPriority",
            "type": "Element",
            "required": True,
        },
    )
    important_page: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ImportantPage",
            "type": "Element",
            "required": True,
        },
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
        },
    )
    construct_with_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConstructWithText",
            "type": "Element",
        },
    )
    prefab_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrefabName",
            "type": "Element",
        },
    )
    prefab_hash: Optional[int] = field(
        default=None,
        metadata={
            "name": "PrefabHash",
            "type": "Element",
            "required": True,
        },
    )
    prefab_hash_string: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrefabHashString",
            "type": "Element",
        },
    )
    paintable_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaintableText",
            "type": "Element",
        },
    )
    stack_size_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "StackSizeText",
            "type": "Element",
        },
    )
    reagents_hash: Optional[int] = field(
        default=None,
        metadata={
            "name": "ReagentsHash",
            "type": "Element",
            "required": True,
        },
    )
    reagents_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReagentsType",
            "type": "Element",
        },
    )
    unit_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitText",
            "type": "Element",
        },
    )
    reagents_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReagentsText",
            "type": "Element",
        },
    )
    specific_heat_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpecificHeatText",
            "type": "Element",
        },
    )
    max_liquid_temperature_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaxLiquidTemperatureText",
            "type": "Element",
        },
    )
    freeze_temperature_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "FreezeTemperatureText",
            "type": "Element",
        },
    )
    boiling_temperature_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "BoilingTemperatureText",
            "type": "Element",
        },
    )
    min_liquid_pressure: Optional[str] = field(
        default=None,
        metadata={
            "name": "MinLiquidPressure",
            "type": "Element",
        },
    )
    latent_heat_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "LatentHeatText",
            "type": "Element",
        },
    )
    moles_per_litre_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "MolesPerLitreText",
            "type": "Element",
        },
    )
    moles_per_litre_in_world_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "MolesPerLitreInWorldText",
            "type": "Element",
        },
    )
    flashpoint_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlashpointText",
            "type": "Element",
        },
    )
    auto_ignition_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "AutoIgnitionText",
            "type": "Element",
        },
    )
    convection_factor_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConvectionFactorText",
            "type": "Element",
        },
    )
    radiation_factor_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "RadiationFactorText",
            "type": "Element",
        },
    )
    solar_heating_factor_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "SolarHeatingFactorText",
            "type": "Element",
        },
    )
    base_power_draw: Optional[str] = field(
        default=None,
        metadata={
            "name": "BasePowerDraw",
            "type": "Element",
        },
    )
    power_storage: Optional[str] = field(
        default=None,
        metadata={
            "name": "PowerStorage",
            "type": "Element",
        },
    )
    power_generation: Optional[str] = field(
        default=None,
        metadata={
            "name": "PowerGeneration",
            "type": "Element",
        },
    )
    max_pressure: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaxPressure",
            "type": "Element",
        },
    )
    volume: Optional[str] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
        },
    )
    nutrition: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nutrition",
            "type": "Element",
        },
    )
    nutrition_quality: Optional[str] = field(
        default=None,
        metadata={
            "name": "NutritionQuality",
            "type": "Element",
        },
    )
    mood_bonus: Optional[str] = field(
        default=None,
        metadata={
            "name": "MoodBonus",
            "type": "Element",
        },
    )
    growth_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "GrowthTime",
            "type": "Element",
        },
    )
    memory_size: Optional[str] = field(
        default=None,
        metadata={
            "name": "MemorySize",
            "type": "Element",
        },
    )
    memory_access: Optional[str] = field(
        default=None,
        metadata={
            "name": "MemoryAccess",
            "type": "Element",
        },
    )
    has_memory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasMemory",
            "type": "Element",
            "required": True,
        },
    )
    placeable_in_rocket: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlaceableInRocket",
            "type": "Element",
        },
    )
    rocket_mass: Optional[str] = field(
        default=None,
        metadata={
            "name": "RocketMass",
            "type": "Element",
        },
    )
    rocket_engine_force: Optional[str] = field(
        default=None,
        metadata={
            "name": "RocketEngineForce",
            "type": "Element",
        },
    )
    rocket_engine_efficiency: Optional[str] = field(
        default=None,
        metadata={
            "name": "RocketEngineEfficiency",
            "type": "Element",
        },
    )
    rocket_engine_exhaust_velocity: Optional[str] = field(
        default=None,
        metadata={
            "name": "RocketEngineExhaustVelocity",
            "type": "Element",
        },
    )
    pressure_break_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "PressureBreakText",
            "type": "Element",
        },
    )
    cable_break_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "CableBreakText",
            "type": "Element",
        },
    )
    internal_atmos_info_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "InternalAtmosInfoText",
            "type": "Element",
        },
    )
    drill_head_properties: Optional[StationDrillHeadProperties] = field(
        default=None,
        metadata={
            "name": "DrillHeadProperties",
            "type": "Element",
        },
    )
    station_suit_info: Optional[StationSuitProperties] = field(
        default=None,
        metadata={
            "name": "StationSuitInfo",
            "type": "Element",
        },
    )
    gas_type: list[GasTypeValue] = field(
        default_factory=list,
        metadata={
            "name": "GasType",
            "type": "Element",
            "tokens": True,
        },
    )
    display_filter: Optional[SpdaentryType] = field(
        default=None,
        metadata={
            "name": "DisplayFilter",
            "type": "Element",
            "required": True,
        },
    )
    custom_sprite_to_use: Optional[Sprite] = field(
        default=None,
        metadata={
            "name": "CustomSpriteToUse",
            "type": "Element",
        },
    )
    page_custom_categories: Optional[ArrayOfString3] = field(
        default=None,
        metadata={
            "name": "PageCustomCategories",
            "type": "Element",
        },
    )
    slot_inserts: Optional[ArrayOfStationSlotsInsert] = field(
        default=None,
        metadata={
            "name": "SlotInserts",
            "type": "Element",
        },
    )
    how_to_build: Optional[ArrayOfStationBuildCostInsert] = field(
        default=None,
        metadata={
            "name": "HowToBuild",
            "type": "Element",
        },
    )
    build_states: Optional[ArrayOfStationBuildCostInsert] = field(
        default=None,
        metadata={
            "name": "BuildStates",
            "type": "Element",
        },
    )
    struct_version_insert: Optional[ArrayOfStationStructureVersionInsert] = field(
        default=None,
        metadata={
            "name": "StructVersionInsert",
            "type": "Element",
        },
    )
    logic_instructions: Optional[ArrayOfStationInstruction] = field(
        default=None,
        metadata={
            "name": "LogicInstructions",
            "type": "Element",
        },
    )
    logic_insert: Optional[ArrayOfStationLogicInsert] = field(
        default=None,
        metadata={
            "name": "LogicInsert",
            "type": "Element",
        },
    )
    logic_slot_insert: Optional[ArrayOfStationLogicInsert] = field(
        default=None,
        metadata={
            "name": "LogicSlotInsert",
            "type": "Element",
        },
    )
    mode_insert: Optional[ArrayOfStationLogicInsert] = field(
        default=None,
        metadata={
            "name": "ModeInsert",
            "type": "Element",
        },
    )
    connection_insert: Optional[ArrayOfStationLogicInsert] = field(
        default=None,
        metadata={
            "name": "ConnectionInsert",
            "type": "Element",
        },
    )
    found_in_ore: Optional[ArrayOfStationFoundInInsert] = field(
        default=None,
        metadata={
            "name": "FoundInOre",
            "type": "Element",
        },
    )
    found_in_gas: Optional[ArrayOfStationFoundInInsert] = field(
        default=None,
        metadata={
            "name": "FoundInGas",
            "type": "Element",
        },
    )
    constructed_things: Optional[ArrayOfStationCategoryInsert] = field(
        default=None,
        metadata={
            "name": "ConstructedThings",
            "type": "Element",
        },
    )
    produced_things_inserts: Optional[ArrayOfStationCategoryInsert] = field(
        default=None,
        metadata={
            "name": "ProducedThingsInserts",
            "type": "Element",
        },
    )
    constructed_by_kits: Optional[ArrayOfStationCategoryInsert] = field(
        default=None,
        metadata={
            "name": "ConstructedByKits",
            "type": "Element",
        },
    )
    resources_used: Optional[ArrayOfStationCategoryInsert] = field(
        default=None,
        metadata={
            "name": "ResourcesUsed",
            "type": "Element",
        },
    )
    used_in: Optional[ArrayOfStationCategoryInsert] = field(
        default=None,
        metadata={
            "name": "UsedIn",
            "type": "Element",
        },
    )
    life_requirements: Optional[ArrayOfStationLifeRequirement] = field(
        default=None,
        metadata={
            "name": "LifeRequirements",
            "type": "Element",
        },
    )


@dataclass
class StepUnitSaveData(StructureSaveData):
    volume: Optional[int] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class StructureExtensionSaveData(StructureSaveData):
    extendable_parent_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ExtendableParentId",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class StructureFuselageSaveData(StructureSaveData):
    rocket_network_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "RocketNetworkId",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class StructureSpawnData(ThingSpawnData):
    pass


@dataclass
class TerraFormingSaveData:
    plant_save_datas: Optional[ArrayOfGlobalPlantSaveData] = field(
        default=None,
        metadata={
            "name": "PlantSaveDatas",
            "type": "Element",
        },
    )


@dataclass
class ThingCreditCardSaveData(DynamicThingSaveData):
    currency: Optional[float] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ThingDynamicBodyBagSaveData(DynamicThingSaveData):
    body_damage_state: Optional[DamageUpdate] = field(
        default=None,
        metadata={
            "name": "BodyDamageState",
            "type": "Element",
            "required": True,
        },
    )
    body_cosmetic_data: Optional[PlayerCosmetics] = field(
        default=None,
        metadata={
            "name": "BodyCosmeticData",
            "type": "Element",
        },
    )
    player_display_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlayerDisplayName",
            "type": "Element",
        },
    )


@dataclass
class TransformerSaveData(StructureSaveData):
    output_setting: Optional[float] = field(
        default=None,
        metadata={
            "name": "OutputSetting",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class VoxelToolSaveData(DynamicThingSaveData):
    current_power: Optional[float] = field(
        default=None,
        metadata={
            "name": "CurrentPower",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class WaypointSaveData(StructureSaveData):
    target_waypoint_reference_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "TargetWaypointReferenceId",
            "type": "Element",
            "required": True,
        },
    )
    waypoint_height: Optional[int] = field(
        default=None,
        metadata={
            "name": "WaypointHeight",
            "type": "Element",
            "required": True,
        },
    )
    visualiser_on: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VisualiserOn",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class WirelessPowerSaveData(StructureSaveData):
    horizontal: Optional[float] = field(
        default=None,
        metadata={
            "name": "Horizontal",
            "type": "Element",
            "required": True,
        },
    )
    vertical: Optional[float] = field(
        default=None,
        metadata={
            "name": "Vertical",
            "type": "Element",
            "required": True,
        },
    )
    target_horizontal: Optional[float] = field(
        default=None,
        metadata={
            "name": "TargetHorizontal",
            "type": "Element",
            "required": True,
        },
    )
    target_vertical: Optional[float] = field(
        default=None,
        metadata={
            "name": "TargetVertical",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class WorldObjectiveCollection(DataCollection):
    objective: list[WorldObjective] = field(
        default_factory=list,
        metadata={
            "name": "Objective",
            "type": "Element",
        },
    )


@dataclass
class ActiveVentSaveData(DeviceAtmosphericSaveData):
    external_pressure: Optional[float] = field(
        default=None,
        metadata={
            "name": "ExternalPressure",
            "type": "Element",
            "required": True,
        },
    )
    internal_pressure: Optional[float] = field(
        default=None,
        metadata={
            "name": "InternalPressure",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class AdvancedFurnaceSaveData(DeviceAtmosphericSaveData):
    output_setting2: Optional[float] = field(
        default=None,
        metadata={
            "name": "OutputSetting2",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ArrayOfStationpediaPage:
    stationpedia_page: list[StationpediaPage] = field(
        default_factory=list,
        metadata={
            "name": "StationpediaPage",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class AtmosphericBodyReference(SphericalBodyBase):
    fresnel: Optional[FresnelReference] = field(
        default=None,
        metadata={
            "name": "Fresnel",
            "type": "Element",
        },
    )
    normal: Optional[TextureReference] = field(
        default=None,
        metadata={
            "name": "Normal",
            "type": "Element",
        },
    )
    specular: Optional[TextureReference] = field(
        default=None,
        metadata={
            "name": "Specular",
            "type": "Element",
        },
    )
    cloud: Optional[CloudTextureReference] = field(
        default=None,
        metadata={
            "name": "Cloud",
            "type": "Element",
        },
    )
    ring: Optional[RingReference] = field(
        default=None,
        metadata={
            "name": "Ring",
            "type": "Element",
        },
    )
    material: Optional[MaterialReference] = field(
        default=None,
        metadata={
            "name": "Material",
            "type": "Element",
        },
    )


@dataclass
class BuyData(TransactionData):
    required: Optional[StockData] = field(
        default=None,
        metadata={
            "name": "Required",
            "type": "Element",
        },
    )
    conditions: list[ConditionDataCollection] = field(
        default_factory=list,
        metadata={
            "name": "Conditions",
            "type": "Element",
        },
    )
    item: Optional[BuyItem] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
        },
    )
    select: Optional[SelectBuyData] = field(
        default=None,
        metadata={
            "name": "Select",
            "type": "Element",
        },
    )
    temperature: list[TemperatureComparableCondition] = field(
        default_factory=list,
        metadata={
            "name": "Temperature",
            "type": "Element",
        },
    )
    logic_type: list[LogicCondition] = field(
        default_factory=list,
        metadata={
            "name": "LogicType",
            "type": "Element",
        },
    )
    interactable: list[InteractableCondition] = field(
        default_factory=list,
        metadata={
            "name": "Interactable",
            "type": "Element",
        },
    )
    quantity: list[Quantity] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
        },
    )
    decay: list[Decay] = field(
        default_factory=list,
        metadata={
            "name": "Decay",
            "type": "Element",
        },
    )
    gas: list[GasCondition] = field(
        default_factory=list,
        metadata={
            "name": "Gas",
            "type": "Element",
        },
    )
    pressure: list[PressureCondition] = field(
        default_factory=list,
        metadata={
            "name": "Pressure",
            "type": "Element",
        },
    )
    temperature_range: list[TemperatureRangeCondition] = field(
        default_factory=list,
        metadata={
            "name": "TemperatureRange",
            "type": "Element",
        },
    )
    percent: list[Percent] = field(
        default_factory=list,
        metadata={
            "name": "Percent",
            "type": "Element",
        },
    )
    moles: list[Moles] = field(
        default_factory=list,
        metadata={
            "name": "Moles",
            "type": "Element",
        },
    )
    charge: list[Energy] = field(
        default_factory=list,
        metadata={
            "name": "Charge",
            "type": "Element",
        },
    )
    difficulty: list[Difficulty] = field(
        default_factory=list,
        metadata={
            "name": "Difficulty",
            "type": "Element",
        },
    )
    species: list[Species] = field(
        default_factory=list,
        metadata={
            "name": "Species",
            "type": "Element",
        },
    )


@dataclass
class CelestialSprite(CelestialSpriteReference):
    class Meta:
        nillable = True


@dataclass
class ChickSaveData(EntitySaveData):
    current_growth_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "CurrentGrowthTime",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ChickenSaveData(EntitySaveData):
    egg_time_default: Optional[float] = field(
        default=None,
        metadata={
            "name": "EggTimeDefault",
            "type": "Element",
            "required": True,
        },
    )
    lay_egg_timer: Optional[float] = field(
        default=None,
        metadata={
            "name": "LayEggTimer",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ChuteDigitalFlipFlopSaveData(ChuteDeviceSaveData):
    setting: Optional[int] = field(
        default=None,
        metadata={
            "name": "Setting",
            "type": "Element",
            "required": True,
        },
    )
    setting2: Optional[int] = field(
        default=None,
        metadata={
            "name": "Setting2",
            "type": "Element",
            "required": True,
        },
    )
    quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ChuteDigitalValveSaveData(ChuteDeviceSaveData):
    setting: Optional[int] = field(
        default=None,
        metadata={
            "name": "Setting",
            "type": "Element",
            "required": True,
        },
    )
    quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ChuteOverflowSaveData(ChuteSaveData):
    pass


@dataclass
class ChuteValveSaveData(ChuteSaveData):
    pass


@dataclass
class CircuitHousingSaveData(LogicBaseSaveData):
    device_ids: list[int] = field(
        default_factory=list,
        metadata={
            "name": "DeviceIDs",
            "type": "Element",
        },
    )
    device_labels: list[str] = field(
        default_factory=list,
        metadata={
            "name": "DeviceLabels",
            "type": "Element",
        },
    )


@dataclass
class CircuitboardSaveData(MotherboardSaveData):
    last_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "LastIndex",
            "type": "Element",
            "required": True,
        },
    )
    filter_string: Optional[str] = field(
        default=None,
        metadata={
            "name": "FilterString",
            "type": "Element",
        },
    )


@dataclass
class CommsMotherboardSaveData(MotherboardSaveData):
    enum_filter_int: Optional[int] = field(
        default=None,
        metadata={
            "name": "EnumFilterInt",
            "type": "Element",
            "required": True,
        },
    )
    selected_dish_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "SelectedDishIndex",
            "type": "Element",
            "required": True,
        },
    )
    selected_pad_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "SelectedPadIndex",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class CryoTubeSaveData(DeviceAtmosphericSaveData):
    pass


@dataclass
class CustomPlantData(CustomItemData):
    mesh: Optional[MeshReference] = field(
        default=None,
        metadata={
            "name": "Mesh",
            "type": "Element",
        },
    )
    texture: Optional[TextureReference] = field(
        default=None,
        metadata={
            "name": "Texture",
            "type": "Element",
        },
    )
    thumbnail: Optional[SpriteReference] = field(
        default=None,
        metadata={
            "name": "Thumbnail",
            "type": "Element",
        },
    )
    seed: Optional[PrefabReference] = field(
        default=None,
        metadata={
            "name": "Seed",
            "type": "Element",
        },
    )
    fruit: Optional[PrefabReference] = field(
        default=None,
        metadata={
            "name": "Fruit",
            "type": "Element",
        },
    )
    perennial: Optional[PerennialData] = field(
        default=None,
        metadata={
            "name": "Perennial",
            "type": "Element",
        },
    )
    stage: list[PlantStageData] = field(
        default_factory=list,
        metadata={
            "name": "Stage",
            "type": "Element",
        },
    )
    stack_quantity_max: Optional[int] = field(
        default=None,
        metadata={
            "name": "StackQuantityMax",
            "type": "Attribute",
            "required": True,
        },
    )
    harvest_quantity_max: Optional[int] = field(
        default=None,
        metadata={
            "name": "HarvestQuantityMax",
            "type": "Attribute",
            "required": True,
        },
    )
    nutrition: Optional[float] = field(
        default=None,
        metadata={
            "name": "Nutrition",
            "type": "Attribute",
            "required": True,
        },
    )
    mood_bonus: Optional[float] = field(
        default=None,
        metadata={
            "name": "MoodBonus",
            "type": "Attribute",
            "required": True,
        },
    )
    thermal_energy: Optional[float] = field(
        default=None,
        metadata={
            "name": "ThermalEnergy",
            "type": "Attribute",
            "required": True,
        },
    )
    adds_to_water: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AddsToWater",
            "type": "Attribute",
            "required": True,
        },
    )
    life_requirements_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LifeRequirementsId",
            "type": "Attribute",
        },
    )
    microwave_ingredient: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MicrowaveIngredient",
            "type": "Attribute",
            "required": True,
        },
    )
    chemistry_ingredient: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChemistryIngredient",
            "type": "Attribute",
            "required": True,
        },
    )
    animal_food: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AnimalFood",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class DeviceImportExportSaveData(DeviceImportSaveData):
    export_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "ExportCount",
            "type": "Element",
            "required": True,
        },
    )
    export_state: Optional[int] = field(
        default=None,
        metadata={
            "name": "ExportState",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DeviceInputOutputCircuitSaveData(DeviceAtmosphericSaveData):
    device_ids: list[int] = field(
        default_factory=list,
        metadata={
            "name": "DeviceIDs",
            "type": "Element",
        },
    )


@dataclass
class DeviceInputOutputImportSaveData(DeviceAtmosphericSaveData):
    import_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "ImportCount",
            "type": "Element",
            "required": True,
        },
    )
    import_state: Optional[int] = field(
        default=None,
        metadata={
            "name": "ImportState",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DiscoverSiteData(SpaceMapNodeActionData):
    site: list[SpaceMapNodeData] = field(
        default_factory=list,
        metadata={
            "name": "Site",
            "type": "Element",
        },
    )


@dataclass
class DroidSleeperSaveData(DeviceAtmosphericSaveData):
    pass


@dataclass
class EvaporationChamberSaveData(DeviceAtmosphericSaveData):
    pipe_network_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "PipeNetworkId",
            "type": "Element",
            "required": True,
        },
    )
    is_burst: list[PipeBurstValue] = field(
        default_factory=list,
        metadata={
            "name": "IsBurst",
            "type": "Element",
            "tokens": True,
        },
    )


@dataclass
class FertiliserSaveData(StackableSaveData):
    cycles: Optional[float] = field(
        default=None,
        metadata={
            "name": "Cycles",
            "type": "Element",
            "required": True,
        },
    )
    harvest_boost: Optional[float] = field(
        default=None,
        metadata={
            "name": "HarvestBoost",
            "type": "Element",
            "required": True,
        },
    )
    growth_speed: Optional[float] = field(
        default=None,
        metadata={
            "name": "GrowthSpeed",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class FoodModData(ConsumableModData):
    nutrition_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "NutritionValue",
            "type": "Element",
            "required": True,
        },
    )
    eat_speed: Optional[float] = field(
        default=None,
        metadata={
            "name": "EatSpeed",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class GasMaskSaveData(AtmosphericItemSaveData):
    pass


@dataclass
class GasRocketEngineSaveData(DeviceAtmosphericSaveData):
    pass


@dataclass
class GovernedGasEngineSaveData(DeviceAtmosphericSaveData):
    pass


@dataclass
class HeatExchangerBaseSaveData(DeviceAtmosphericSaveData):
    pass


@dataclass
class HeatExchangerSaveData(DeviceAtmosphericSaveData):
    atmos2: Optional[AtmosphereSaveData] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    atmos3: Optional[AtmosphereSaveData] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class HumanSaveData(EntitySaveData):
    currency: Optional[float] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        },
    )
    cosmetics: Optional[PlayerCosmetics] = field(
        default=None,
        metadata={
            "name": "Cosmetics",
            "type": "Element",
        },
    )
    skin_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "SkinIndex",
            "type": "Element",
            "required": True,
        },
    )
    gender_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "GenderIndex",
            "type": "Element",
            "required": True,
        },
    )
    potato_days: Optional[int] = field(
        default=None,
        metadata={
            "name": "PotatoDays",
            "type": "Element",
            "required": True,
        },
    )
    last_valid_playable_position: Optional[Vector2] = field(
        default=None,
        metadata={
            "name": "LastValidPlayablePosition",
            "type": "Element",
            "required": True,
        },
    )
    start_location: Optional[StringReference] = field(
        default=None,
        metadata={
            "name": "StartLocation",
            "type": "Element",
        },
    )


@dataclass
class JetpackSaveData(AtmosphericItemSaveData):
    output_setting: Optional[float] = field(
        default=None,
        metadata={
            "name": "OutputSetting",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LandingPadModularSaveData(PadModularSaveData):
    pass


@dataclass
class LandingPadPumpSaveData(DeviceAtmosphericSaveData):
    pad_network_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "PadNetworkId",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LfoVolumeSaveData(LogicBaseSaveData):
    intensity: Optional[int] = field(
        default=None,
        metadata={
            "name": "Intensity",
            "type": "Element",
            "required": True,
        },
    )
    output_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "OutputId",
            "type": "Element",
            "required": True,
        },
    )
    bpm: Optional[int] = field(
        default=None,
        metadata={
            "name": "Bpm",
            "type": "Element",
            "required": True,
        },
    )
    waveform: Optional[int] = field(
        default=None,
        metadata={
            "name": "Waveform",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LiquidRocketEngineSaveData(DeviceAtmosphericSaveData):
    pass


@dataclass
class LogicBatchReaderSaveData(LogicBaseSaveData):
    current_output_hash: Optional[int] = field(
        default=None,
        metadata={
            "name": "CurrentOutputHash",
            "type": "Element",
            "required": True,
        },
    )
    input_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "InputIndex",
            "type": "Element",
            "required": True,
        },
    )
    batch_method: Optional[LogicBatchMethod] = field(
        default=None,
        metadata={
            "name": "BatchMethod",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LogicBatchSlotReaderSaveData(LogicBaseSaveData):
    current_input_hash: Optional[int] = field(
        default=None,
        metadata={
            "name": "CurrentInputHash",
            "type": "Element",
            "required": True,
        },
    )
    input_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "InputIndex",
            "type": "Element",
            "required": True,
        },
    )
    slot_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "SlotIndex",
            "type": "Element",
            "required": True,
        },
    )
    batch_method: Optional[LogicBatchMethod] = field(
        default=None,
        metadata={
            "name": "BatchMethod",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LogicBatchWriterSaveData(LogicBaseSaveData):
    current_output_hash: Optional[int] = field(
        default=None,
        metadata={
            "name": "CurrentOutputHash",
            "type": "Element",
            "required": True,
        },
    )
    current_input_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "CurrentInputId",
            "type": "Element",
            "required": True,
        },
    )
    logic_type: Optional[LogicType] = field(
        default=None,
        metadata={
            "name": "LogicType",
            "type": "Element",
            "required": True,
        },
    )
    last_input_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "LastInputId",
            "type": "Element",
            "required": True,
        },
    )
    last_setting: Optional[float] = field(
        default=None,
        metadata={
            "name": "LastSetting",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LogicMathSaveData(LogicBaseSaveData):
    input1: Optional[int] = field(
        default=None,
        metadata={
            "name": "Input1",
            "type": "Element",
            "required": True,
        },
    )
    input2: Optional[int] = field(
        default=None,
        metadata={
            "name": "Input2",
            "type": "Element",
            "required": True,
        },
    )
    input3: Optional[int] = field(
        default=None,
        metadata={
            "name": "Input3",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LogicMotherboardSaveData(MotherboardSaveData):
    logic_states: Optional[ArrayOfLogicStateSave] = field(
        default=None,
        metadata={
            "name": "LogicStates",
            "type": "Element",
        },
    )
    current_logic_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "CurrentLogicIndex",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LogicReaderSaveData(LogicBaseSaveData):
    current_device_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "CurrentDeviceId",
            "type": "Element",
            "required": True,
        },
    )
    input_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "InputIndex",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LogicReagentReaderSaveData(LogicBaseSaveData):
    current_device_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "CurrentDeviceId",
            "type": "Element",
            "required": True,
        },
    )
    reagent_hash: Optional[int] = field(
        default=None,
        metadata={
            "name": "ReagentHash",
            "type": "Element",
            "required": True,
        },
    )
    mode_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "ModeIndex",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LogicSlotReaderSaveData(LogicBaseSaveData):
    current_device_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "CurrentDeviceId",
            "type": "Element",
            "required": True,
        },
    )
    input_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "InputIndex",
            "type": "Element",
            "required": True,
        },
    )
    slot_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "SlotIndex",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LogicStopWatchSaveData(LogicBaseSaveData):
    offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LogicTransmitterSaveData(LogicBaseSaveData):
    current_connected_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "CurrentConnectedId",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LogicWriterSaveData(LogicBaseSaveData):
    current_output_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "CurrentOutputId",
            "type": "Element",
            "required": True,
        },
    )
    current_input_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "CurrentInputId",
            "type": "Element",
            "required": True,
        },
    )
    logic_type: Optional[LogicType] = field(
        default=None,
        metadata={
            "name": "LogicType",
            "type": "Element",
            "required": True,
        },
    )
    last_input_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "LastInputId",
            "type": "Element",
            "required": True,
        },
    )
    last_output_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "LastOutputId",
            "type": "Element",
            "required": True,
        },
    )
    last_setting: Optional[float] = field(
        default=None,
        metadata={
            "name": "LastSetting",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LogicWriterSwitchSaveData(LogicBaseSaveData):
    current_output_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "CurrentOutputId",
            "type": "Element",
            "required": True,
        },
    )
    current_input_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "CurrentInputId",
            "type": "Element",
            "required": True,
        },
    )
    logic_type: Optional[LogicType] = field(
        default=None,
        metadata={
            "name": "LogicType",
            "type": "Element",
            "required": True,
        },
    )
    last_input_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "LastInputId",
            "type": "Element",
            "required": True,
        },
    )
    last_output_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "LastOutputId",
            "type": "Element",
            "required": True,
        },
    )
    last_setting: Optional[float] = field(
        default=None,
        metadata={
            "name": "LastSetting",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class MapMotherboardSaveData(MotherboardSaveData):
    linked_scanners: list[int] = field(
        default_factory=list,
        metadata={
            "name": "LinkedScanners",
            "type": "Element",
        },
    )
    mask_texture: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaskTexture",
            "type": "Element",
        },
    )


@dataclass
class MaterialSettings:
    macro: Optional[MacroTextureData] = field(
        default=None,
        metadata={
            "name": "Macro",
            "type": "Element",
        },
    )
    detail: Optional[DetailTextureData] = field(
        default=None,
        metadata={
            "name": "Detail",
            "type": "Element",
        },
    )


@dataclass
class MultiMotherboardSaveData(MotherboardSaveData):
    current_tab: Optional[int] = field(
        default=None,
        metadata={
            "name": "CurrentTab",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class OreSaveData(StackableSaveData):
    quantity_smelted: Optional[int] = field(
        default=None,
        metadata={
            "name": "QuantitySmelted",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class PlantSaveData(StackableSaveData):
    stage_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "StageTime",
            "type": "Element",
            "required": True,
        },
    )
    stage: Optional[int] = field(
        default=None,
        metadata={
            "name": "Stage",
            "type": "Element",
            "required": True,
        },
    )
    harvest_quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "HarvestQuantity",
            "type": "Element",
            "required": True,
        },
    )
    seed_quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "SeedQuantity",
            "type": "Element",
            "required": True,
        },
    )
    fertilizer_boost: Optional[float] = field(
        default=None,
        metadata={
            "name": "FertilizerBoost",
            "type": "Element",
            "required": True,
        },
    )
    is_fertilized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsFertilized",
            "type": "Element",
            "required": True,
        },
    )
    planter_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlanterName",
            "type": "Element",
        },
    )
    stacked_gene_collections: Optional[ArrayOfGeneCollectionWrapper] = field(
        default=None,
        metadata={
            "name": "StackedGeneCollections",
            "type": "Element",
        },
    )
    plant_record: Optional[PlantRecord] = field(
        default=None,
        metadata={
            "name": "PlantRecord",
            "type": "Element",
        },
    )
    aggregate_states: Optional[ArrayOfStateWrapper] = field(
        default=None,
        metadata={
            "name": "AggregateStates",
            "type": "Element",
        },
    )
    current_states: Optional[ArrayOfBooleanStateWrapper] = field(
        default=None,
        metadata={
            "name": "CurrentStates",
            "type": "Element",
        },
    )


@dataclass
class PowerReceiverSaveData(WirelessPowerSaveData):
    pass


@dataclass
class PowerTransmitterSaveData(WirelessPowerSaveData):
    output_network_reference_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "OutputNetworkReferenceId",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class PoweredVentSaveData(DeviceAtmosphericSaveData):
    external_pressure: Optional[float] = field(
        default=None,
        metadata={
            "name": "ExternalPressure",
            "type": "Element",
            "required": True,
        },
    )
    internal_pressure: Optional[float] = field(
        default=None,
        metadata={
            "name": "InternalPressure",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class PressureFedGasEngineSaveData(DeviceAtmosphericSaveData):
    pass


@dataclass
class PressureFedLiquidEngineSaveData(DeviceAtmosphericSaveData):
    pass


@dataclass
class ProgrammableChipMotherboardSaveData(MotherboardSaveData):
    source_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourceCode",
            "type": "Element",
        },
    )
    device_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "DeviceIndex",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class PumpedLiquidEngineSaveData(DeviceAtmosphericSaveData):
    pass


@dataclass
class RadiatorRotatableSaveData(DeviceAtmosphericSaveData):
    horizontal: Optional[float] = field(
        default=None,
        metadata={
            "name": "Horizontal",
            "type": "Element",
            "required": True,
        },
    )
    vertical: Optional[float] = field(
        default=None,
        metadata={
            "name": "Vertical",
            "type": "Element",
            "required": True,
        },
    )
    target_horizontal: Optional[float] = field(
        default=None,
        metadata={
            "name": "TargetHorizontal",
            "type": "Element",
            "required": True,
        },
    )
    target_vertical: Optional[float] = field(
        default=None,
        metadata={
            "name": "TargetVertical",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RoadflareSaveData(StackableSaveData):
    lifetime: Optional[float] = field(
        default=None,
        metadata={
            "name": "Lifetime",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RoboticArmBypassSaveData(RoboticArmRailDeviceBaseSaveData):
    pass


@dataclass
class RoboticArmDockSaveData(RoboticArmRailDeviceBaseSaveData):
    current_index: Optional[float] = field(
        default=None,
        metadata={
            "name": "CurrentIndex",
            "type": "Element",
            "required": True,
        },
    )
    target_junction_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "TargetJunctionIndex",
            "type": "Element",
            "required": True,
        },
    )
    is_starting_dock: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsStartingDock",
            "type": "Element",
            "required": True,
        },
    )
    arm_state: Optional[ArmState] = field(
        default=None,
        metadata={
            "name": "ArmState",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RoboticArmJunctionSaveData(RoboticArmRailBaseSaveData):
    pass


@dataclass
class RoboticArmRailSaveData(RoboticArmRailBaseSaveData):
    pass


@dataclass
class RocketGasUmbilicalFemaleSaveData(DeviceAtmosphericSaveData):
    partner_distance: Optional[int] = field(
        default=None,
        metadata={
            "name": "PartnerDistance",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RocketMotherboardSaveData(MotherboardSaveData):
    pinned_devices: list[int] = field(
        default_factory=list,
        metadata={
            "name": "PinnedDevices",
            "type": "Element",
        },
    )
    pinned_logic_value_device: list[int] = field(
        default_factory=list,
        metadata={
            "name": "PinnedLogicValueDevice",
            "type": "Element",
        },
    )
    pinned_logic_value_type: list[int] = field(
        default_factory=list,
        metadata={
            "name": "PinnedLogicValueType",
            "type": "Element",
        },
    )


@dataclass
class RockyBodyReference(SphericalBodyBase):
    normal: Optional[TextureReference] = field(
        default=None,
        metadata={
            "name": "Normal",
            "type": "Element",
        },
    )
    mesh: Optional[MeshReference] = field(
        default=None,
        metadata={
            "name": "Mesh",
            "type": "Element",
        },
    )
    emissive: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "Emissive",
            "type": "Element",
        },
    )


@dataclass
class SatelliteDishSaveData(RotatableSaveData):
    setting: Optional[int] = field(
        default=None,
        metadata={
            "name": "Setting",
            "type": "Element",
            "required": True,
        },
    )
    target_pad_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "TargetPadIndex",
            "type": "Element",
            "required": True,
        },
    )
    best_signal_idfilter: Optional[int] = field(
        default=None,
        metadata={
            "name": "BestSignalIDFilter",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SellData(TransactionData):
    stock: Optional[StockData] = field(
        default=None,
        metadata={
            "name": "Stock",
            "type": "Element",
        },
    )
    interaction: list[InteractionAction] = field(
        default_factory=list,
        metadata={
            "name": "Interaction",
            "type": "Element",
        },
    )
    move_player: list[MovePlayerAction] = field(
        default_factory=list,
        metadata={
            "name": "MovePlayer",
            "type": "Element",
        },
    )
    gene: list[GeneAction] = field(
        default_factory=list,
        metadata={
            "name": "Gene",
            "type": "Element",
        },
    )
    quantity: list[QuantityAction] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
        },
    )
    percent: list[PercentAction] = field(
        default_factory=list,
        metadata={
            "name": "Percent",
            "type": "Element",
        },
    )
    reagents: list[SetReagents] = field(
        default_factory=list,
        metadata={
            "name": "Reagents",
            "type": "Element",
        },
    )
    charge: list[ChargeAction] = field(
        default_factory=list,
        metadata={
            "name": "Charge",
            "type": "Element",
        },
    )
    gas: list[GasAction] = field(
        default_factory=list,
        metadata={
            "name": "Gas",
            "type": "Element",
        },
    )
    source_code: list[SourceCodeAction] = field(
        default_factory=list,
        metadata={
            "name": "SourceCode",
            "type": "Element",
        },
    )
    select: Optional[SelectSellData] = field(
        default=None,
        metadata={
            "name": "Select",
            "type": "Element",
        },
    )
    item: Optional[SellItem] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
        },
    )


@dataclass
class SlagSaveData(StackableSaveData):
    created_reagents: Optional[ArrayOfReagentSaveData] = field(
        default=None,
        metadata={
            "name": "CreatedReagents",
            "type": "Element",
        },
    )


@dataclass
class SolarControlSaveData(MotherboardSaveData):
    target_horizontal: Optional[float] = field(
        default=None,
        metadata={
            "name": "TargetHorizontal",
            "type": "Element",
            "required": True,
        },
    )
    target_vertical: Optional[float] = field(
        default=None,
        metadata={
            "name": "TargetVertical",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SpaceMapData(DataCollection):
    entry: Optional[SpaceMapNodeData] = field(
        default=None,
        metadata={
            "name": "Entry",
            "type": "Element",
        },
    )
    low_orbit_hub: Optional[SpaceMapNodeData] = field(
        default=None,
        metadata={
            "name": "LowOrbitHub",
            "type": "Element",
        },
    )
    node: list[SpaceMapNodeData] = field(
        default_factory=list,
        metadata={
            "name": "Node",
            "type": "Element",
        },
    )
    sprite: list[SpaceMapSpriteData] = field(
        default_factory=list,
        metadata={
            "name": "Sprite",
            "type": "Element",
        },
    )
    orbit_distance: Optional[float] = field(
        default=None,
        metadata={
            "name": "OrbitDistance",
            "type": "Attribute",
            "required": True,
        },
    )
    fall_back: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FallBack",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class StepSequencerSaveData(LogicBaseSaveData):
    input_ids: list[int] = field(
        default_factory=list,
        metadata={
            "name": "InputIds",
            "type": "Element",
        },
    )
    attack: Optional[int] = field(
        default=None,
        metadata={
            "name": "Attack",
            "type": "Element",
            "required": True,
        },
    )
    release: Optional[int] = field(
        default=None,
        metadata={
            "name": "Release",
            "type": "Element",
            "required": True,
        },
    )
    output_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "OutputId",
            "type": "Element",
            "required": True,
        },
    )
    bpm: Optional[int] = field(
        default=None,
        metadata={
            "name": "Bpm",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class StirlingEngineSaveData(DeviceAtmosphericSaveData):
    hot_input_atmosphere: Optional[AtmosphereSaveData] = field(
        default=None,
        metadata={
            "name": "HotInputAtmosphere",
            "type": "Element",
        },
    )
    hot_side_atmosphere: Optional[AtmosphereSaveData] = field(
        default=None,
        metadata={
            "name": "HotSideAtmosphere",
            "type": "Element",
        },
    )
    cold_side_atmosphere: Optional[AtmosphereSaveData] = field(
        default=None,
        metadata={
            "name": "ColdSideAtmosphere",
            "type": "Element",
        },
    )


@dataclass
class StoredThings:
    dynamic_thing: Optional[DynamicThingSaveData] = field(
        default=None,
        metadata={
            "name": "DynamicThing",
            "type": "Element",
        },
    )
    stored_children: Optional[ArrayOfDynamicThingSaveData] = field(
        default=None,
        metadata={
            "name": "StoredChildren",
            "type": "Element",
        },
    )


@dataclass
class SuitBaseSaveData(AtmosphericItemSaveData):
    output_setting: Optional[float] = field(
        default=None,
        metadata={
            "name": "OutputSetting",
            "type": "Element",
            "required": True,
        },
    )
    output_temperature_setting: Optional[float] = field(
        default=None,
        metadata={
            "name": "OutputTemperatureSetting",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SuitSaveData(AtmosphericItemSaveData):
    output_setting: Optional[float] = field(
        default=None,
        metadata={
            "name": "OutputSetting",
            "type": "Element",
            "required": True,
        },
    )
    output_temperature_setting: Optional[float] = field(
        default=None,
        metadata={
            "name": "OutputTemperatureSetting",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class WaterPurifierSaveData(DeviceAtmosphericSaveData):
    pass


@dataclass
class WorldData:
    game: Optional[str] = field(
        default=None,
        metadata={
            "name": "Game",
            "type": "Element",
        },
    )
    game_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "GameVersion",
            "type": "Element",
        },
    )
    date_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "DateTime",
            "type": "Element",
            "required": True,
        },
    )
    days_past: Optional[int] = field(
        default=None,
        metadata={
            "name": "DaysPast",
            "type": "Element",
            "required": True,
        },
    )
    world_setting: Optional[SerializedId] = field(
        default=None,
        metadata={
            "name": "WorldSetting",
            "type": "Element",
        },
    )
    world_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "WorldName",
            "type": "Element",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    difficulty_setting: Optional[SerializedId] = field(
        default=None,
        metadata={
            "name": "DifficultySetting",
            "type": "Element",
        },
    )
    start_condition: Optional[SerializedId] = field(
        default=None,
        metadata={
            "name": "StartCondition",
            "type": "Element",
        },
    )
    start_location: Optional[SerializedId] = field(
        default=None,
        metadata={
            "name": "StartLocation",
            "type": "Element",
        },
    )
    client_info: list[SerializedClientInfo] = field(
        default_factory=list,
        metadata={
            "name": "ClientInfo",
            "type": "Element",
        },
    )
    celestial: Optional[OrbitSimulationSaveData] = field(
        default=None,
        metadata={
            "name": "Celestial",
            "type": "Element",
        },
    )
    terra_forming: Optional[TerraFormingSaveData] = field(
        default=None,
        metadata={
            "name": "TerraForming",
            "type": "Element",
        },
    )
    station_contacts: Optional[ArrayOfStationContactData] = field(
        default=None,
        metadata={
            "name": "StationContacts",
            "type": "Element",
        },
    )
    contact_slot_save_datas: Optional[ArrayOfContactSlotSaveData] = field(
        default=None,
        metadata={
            "name": "ContactSlotSaveDatas",
            "type": "Element",
        },
    )
    overall_index_of_contacts: Optional[int] = field(
        default=None,
        metadata={
            "name": "OverallIndexOfContacts",
            "type": "Element",
            "required": True,
        },
    )
    world_seed: Optional[int] = field(
        default=None,
        metadata={
            "name": "WorldSeed",
            "type": "Element",
            "required": True,
        },
    )
    rooms: Optional[ArrayOfRoomData] = field(
        default=None,
        metadata={
            "name": "Rooms",
            "type": "Element",
        },
    )
    pipe_networks: Optional[ArrayOfLong1] = field(
        default=None,
        metadata={
            "name": "PipeNetworks",
            "type": "Element",
        },
    )
    cable_networks: Optional[ArrayOfLong1] = field(
        default=None,
        metadata={
            "name": "CableNetworks",
            "type": "Element",
        },
    )
    chute_networks: Optional[ArrayOfLong1] = field(
        default=None,
        metadata={
            "name": "ChuteNetworks",
            "type": "Element",
        },
    )
    landing_pad_networks: Optional[ArrayOfLong1] = field(
        default=None,
        metadata={
            "name": "LandingPadNetworks",
            "type": "Element",
        },
    )
    rocket_networks: Optional[ArrayOfLong1] = field(
        default=None,
        metadata={
            "name": "RocketNetworks",
            "type": "Element",
        },
    )
    robotic_arm_networks: Optional[ArrayOfLong1] = field(
        default=None,
        metadata={
            "name": "RoboticArmNetworks",
            "type": "Element",
        },
    )
    rocket_shuttle_networks: Optional[ArrayOfLong1] = field(
        default=None,
        metadata={
            "name": "RocketShuttleNetworks",
            "type": "Element",
        },
    )
    all_things: Optional[ArrayOfThingSaveData] = field(
        default=None,
        metadata={
            "name": "AllThings",
            "type": "Element",
        },
    )
    things: Optional[ArrayOfThingSaveData] = field(
        default=None,
        metadata={
            "name": "Things",
            "type": "Element",
        },
    )
    pending_spawn_actions: Optional[ArrayOfPendingSpawnAction] = field(
        default=None,
        metadata={
            "name": "PendingSpawnActions",
            "type": "Element",
        },
    )
    atmospheres: Optional[ArrayOfAtmosphereSaveData] = field(
        default=None,
        metadata={
            "name": "Atmospheres",
            "type": "Element",
        },
    )
    space_map: Optional[SpaceMapSaveData] = field(
        default=None,
        metadata={
            "name": "SpaceMap",
            "type": "Element",
        },
    )
    world_objectives: Optional[ArrayOfWorldObjectiveSaveData] = field(
        default=None,
        metadata={
            "name": "WorldObjectives",
            "type": "Element",
        },
    )
    rockets: Optional[ArrayOfRocketSaveData] = field(
        default=None,
        metadata={
            "name": "Rockets",
            "type": "Element",
        },
    )
    rocket_name_history: Optional[ArrayOfString3] = field(
        default=None,
        metadata={
            "name": "RocketNameHistory",
            "type": "Element",
        },
    )
    user_interface: Optional[UserInterfaceSaveData] = field(
        default=None,
        metadata={
            "name": "UserInterface",
            "type": "Element",
        },
    )
    weather_manager_data: Optional[WeatherManagerSavedData] = field(
        default=None,
        metadata={
            "name": "WeatherManagerData",
            "type": "Element",
        },
    )
    origin_position: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "OriginPosition",
            "type": "Element",
            "required": True,
        },
    )
    world_log: Optional[ArrayOfChoice1] = field(
        default=None,
        metadata={
            "name": "WorldLog",
            "type": "Element",
        },
    )
    planetary_atmosphere: Optional[PlanetaryAtmosphereSaveData] = field(
        default=None,
        metadata={
            "name": "PlanetaryAtmosphere",
            "type": "Element",
        },
    )
    terrain_chunk_checksums: Optional[ArrayOfInt1] = field(
        default=None,
        metadata={
            "name": "TerrainChunkChecksums",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass
class WreckageSaveData(StackableSaveData):
    wrecked_parent_prefab_hash: Optional[int] = field(
        default=None,
        metadata={
            "name": "WreckedParentPrefabHash",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class AdvAirlockControldSaveData(CircuitboardSaveData):
    pressure_internal: Optional[float] = field(
        default=None,
        metadata={
            "name": "PressureInternal",
            "type": "Element",
            "required": True,
        },
    )
    pressure_external: Optional[float] = field(
        default=None,
        metadata={
            "name": "PressureExternal",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class AirConditionerSaveData(DeviceInputOutputCircuitSaveData):
    pass


@dataclass
class AirContolCircuitboardSaveData(CircuitboardSaveData):
    air_control_vents: Optional[ArrayOfAirControlVent] = field(
        default=None,
        metadata={
            "name": "AirControlVents",
            "type": "Element",
        },
    )


@dataclass
class AtmosphericBody(AtmosphericBodyReference):
    class Meta:
        nillable = True


@dataclass
class CelestialCollection:
    body: list[CelestialBodyReference] = field(
        default_factory=list,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )
    sprite: list[CelestialSpriteReference] = field(
        default_factory=list,
        metadata={
            "name": "Sprite",
            "type": "Element",
        },
    )
    rocky_body: list[RockyBodyReference] = field(
        default_factory=list,
        metadata={
            "name": "RockyBody",
            "type": "Element",
        },
    )
    atmospheric_body: list[AtmosphericBodyReference] = field(
        default_factory=list,
        metadata={
            "name": "AtmosphericBody",
            "type": "Element",
        },
    )


@dataclass
class CentrifugeSaveData(DeviceImportExportSaveData):
    rpm: Optional[float] = field(
        default=None,
        metadata={
            "name": "Rpm",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DeviceImportExport2SaveData(DeviceImportExportSaveData):
    export2_state: Optional[int] = field(
        default=None,
        metadata={
            "name": "Export2State",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DeviceInputOutputImportExportSaveData(DeviceInputOutputImportSaveData):
    export_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "ExportCount",
            "type": "Element",
            "required": True,
        },
    )
    export_state: Optional[int] = field(
        default=None,
        metadata={
            "name": "ExportState",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DirectHeatExchangerSaveData(HeatExchangerBaseSaveData):
    pass


@dataclass
class HorizontalQuarrySaveData(DeviceImportExportSaveData):
    drill_car_position: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "DrillCarPosition",
            "type": "Element",
            "required": True,
        },
    )
    collected_ore: list[QuarryCollectedOre] = field(
        default_factory=list,
        metadata={
            "name": "CollectedOre",
            "type": "Element",
        },
    )


@dataclass
class IndustrialCombustorSaveData(DeviceInputOutputCircuitSaveData):
    stressed_to_failure: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StressedToFailure",
            "type": "Element",
            "required": True,
        },
    )
    machine_temperature: Optional[float] = field(
        default=None,
        metadata={
            "name": "MachineTemperature",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class IndustrialFiltrationSaveData(DeviceInputOutputCircuitSaveData):
    pass


@dataclass
class LandingPadCenterSaveData(LandingPadModularSaveData):
    trader_reference_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "TraderReferenceID",
            "type": "Element",
            "required": True,
        },
    )
    parent_motherboard_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParentMotherboardID",
            "type": "Element",
            "required": True,
        },
    )
    next_waypoint_reference_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "NextWaypointReferenceId",
            "type": "Element",
            "required": True,
        },
    )
    virtual_waypoint_height: Optional[float] = field(
        default=None,
        metadata={
            "name": "VirtualWaypointHeight",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Language:
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    code: Optional[LanguageCode] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "required": True,
        },
    )
    font: Optional[str] = field(
        default=None,
        metadata={
            "name": "Font",
            "type": "Element",
        },
    )
    reagents: Optional[ArrayOfRecordReagent] = field(
        default=None,
        metadata={
            "name": "Reagents",
            "type": "Element",
        },
    )
    gases: Optional[ArrayOfRecord] = field(
        default=None,
        metadata={
            "name": "Gases",
            "type": "Element",
        },
    )
    actions: Optional[ArrayOfRecord] = field(
        default=None,
        metadata={
            "name": "Actions",
            "type": "Element",
        },
    )
    things: Optional[ArrayOfRecordThing] = field(
        default=None,
        metadata={
            "name": "Things",
            "type": "Element",
        },
    )
    slots: Optional[ArrayOfRecord] = field(
        default=None,
        metadata={
            "name": "Slots",
            "type": "Element",
        },
    )
    interactables: Optional[ArrayOfRecord] = field(
        default=None,
        metadata={
            "name": "Interactables",
            "type": "Element",
        },
    )
    interface: Optional[ArrayOfRecord] = field(
        default=None,
        metadata={
            "name": "Interface",
            "type": "Element",
        },
    )
    colors: Optional[ArrayOfRecord] = field(
        default=None,
        metadata={
            "name": "Colors",
            "type": "Element",
        },
    )
    keys: Optional[ArrayOfRecord] = field(
        default=None,
        metadata={
            "name": "Keys",
            "type": "Element",
        },
    )
    mineables: Optional[ArrayOfRecord] = field(
        default=None,
        metadata={
            "name": "Mineables",
            "type": "Element",
        },
    )
    screen_space_tool_tips: Optional[ArrayOfRecord] = field(
        default=None,
        metadata={
            "name": "ScreenSpaceToolTips",
            "type": "Element",
        },
    )
    help_page: Optional[ArrayOfStationpediaPage] = field(
        default=None,
        metadata={
            "name": "HelpPage",
            "type": "Element",
        },
    )
    thing_page_override: Optional[ArrayOfSpdathingOverideData] = field(
        default=None,
        metadata={
            "name": "ThingPageOverride",
            "type": "Element",
        },
    )
    home_page_buttons_override: Optional[ArrayOfSpdahomePageButtonOverride] = field(
        default=None,
        metadata={
            "name": "HomePageButtonsOverride",
            "type": "Element",
        },
    )
    game_strings: Optional[ArrayOfRecord] = field(
        default=None,
        metadata={
            "name": "GameStrings",
            "type": "Element",
        },
    )
    game_tip: Optional[ArrayOfString6] = field(
        default=None,
        metadata={
            "name": "GameTip",
            "type": "Element",
        },
    )


@dataclass
class LogicPidControllerSaveData(LogicReaderSaveData):
    set_point: Optional[float] = field(
        default=None,
        metadata={
            "name": "SetPoint",
            "type": "Element",
            "required": True,
        },
    )
    proportional_gain: Optional[float] = field(
        default=None,
        metadata={
            "name": "ProportionalGain",
            "type": "Element",
            "required": True,
        },
    )
    derivative_gain: Optional[float] = field(
        default=None,
        metadata={
            "name": "DerivativeGain",
            "type": "Element",
            "required": True,
        },
    )
    integral_gain: Optional[float] = field(
        default=None,
        metadata={
            "name": "IntegralGain",
            "type": "Element",
            "required": True,
        },
    )
    process_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "ProcessValue",
            "type": "Element",
            "required": True,
        },
    )
    output_maximum: Optional[float] = field(
        default=None,
        metadata={
            "name": "OutputMaximum",
            "type": "Element",
            "required": True,
        },
    )
    output_minimum: Optional[float] = field(
        default=None,
        metadata={
            "name": "OutputMinimum",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class MachineSaveData(DeviceInputOutputCircuitSaveData):
    pass


@dataclass
class NitrolyzerSaveData(DeviceInputOutputCircuitSaveData):
    pass


@dataclass
class PassthroughHeatExchangerSaveData(HeatExchangerBaseSaveData):
    pass


@dataclass
class PureIceSaveData(OreSaveData):
    spawn_gas: list[SpawnContentsData] = field(
        default_factory=list,
        metadata={
            "name": "SpawnGas",
            "type": "Element",
        },
    )
    temperature: Optional[float] = field(
        default=None,
        metadata={
            "name": "Temperature",
            "type": "Element",
            "required": True,
        },
    )
    melt_temperature: Optional[float] = field(
        default=None,
        metadata={
            "name": "MeltTemperature",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class QuarrySaveData(DeviceImportExportSaveData):
    drill_end_sgement_x: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "DrillEndSgementX",
            "type": "Element",
            "required": True,
        },
    )
    drill_end_sgement_y: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "DrillEndSgementY",
            "type": "Element",
            "required": True,
        },
    )
    drill_end_sgement_z: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "DrillEndSgementZ",
            "type": "Element",
            "required": True,
        },
    )
    saved_drill_end_segment_x: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "SavedDrillEndSegmentX",
            "type": "Element",
            "required": True,
        },
    )
    saved_drill_end_segment_y: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "SavedDrillEndSegmentY",
            "type": "Element",
            "required": True,
        },
    )
    saved_drill_end_segment_z: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "SavedDrillEndSegmentZ",
            "type": "Element",
            "required": True,
        },
    )
    head_position: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "HeadPosition",
            "type": "Element",
            "required": True,
        },
    )
    carriage_position: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "CarriagePosition",
            "type": "Element",
            "required": True,
        },
    )
    railing_position: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "RailingPosition",
            "type": "Element",
            "required": True,
        },
    )
    movement_amount: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "MovementAmount",
            "type": "Element",
            "required": True,
        },
    )
    forward_direction: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ForwardDirection",
            "type": "Element",
            "required": True,
        },
    )
    drill_finished: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DrillFinished",
            "type": "Element",
            "required": True,
        },
    )
    is_finishing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsFinishing",
            "type": "Element",
            "required": True,
        },
    )
    transporting_ore: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TransportingOre",
            "type": "Element",
            "required": True,
        },
    )
    collected_ore: list[QuarryCollectedOre] = field(
        default_factory=list,
        metadata={
            "name": "CollectedOre",
            "type": "Element",
        },
    )


@dataclass
class RoboticArmDockAtmosSaveData(RoboticArmDockSaveData):
    external_pressure: Optional[float] = field(
        default=None,
        metadata={
            "name": "ExternalPressure",
            "type": "Attribute",
            "required": True,
        },
    )
    internal_pressure: Optional[float] = field(
        default=None,
        metadata={
            "name": "InternalPressure",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class RoboticArmDockCargoSaveData(RoboticArmDockSaveData):
    current_slot_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "CurrentSlotIndex",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RoboticArmDockCollectorSaveData(RoboticArmDockSaveData):
    pass


@dataclass
class RoboticArmDockHydroponicsSaveData(RoboticArmDockSaveData):
    pass


@dataclass
class RocketChuteStorageSaveData(DeviceImportExportSaveData):
    current_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "CurrentIndex",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RocketGasCollectorSaveData(DeviceImportExportSaveData):
    mining_progress: Optional[float] = field(
        default=None,
        metadata={
            "name": "MiningProgress",
            "type": "Element",
            "required": True,
        },
    )
    quantity_mined: Optional[int] = field(
        default=None,
        metadata={
            "name": "QuantityMined",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RocketMinerSaveData(DeviceImportExportSaveData):
    mining_progress: Optional[float] = field(
        default=None,
        metadata={
            "name": "MiningProgress",
            "type": "Element",
            "required": True,
        },
    )
    last_mined_prefab: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastMinedPrefab",
            "type": "Element",
        },
    )
    quantity_mined: Optional[int] = field(
        default=None,
        metadata={
            "name": "QuantityMined",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class RockyBody(RockyBodyReference):
    class Meta:
        nillable = True


@dataclass
class SiloSaveData(DeviceImportExportSaveData):
    stored_items: list[DynamicThingSaveData] = field(
        default_factory=list,
        metadata={
            "name": "StoredItems",
            "type": "Element",
        },
    )
    all_stored_items: list[StoredThings] = field(
        default_factory=list,
        metadata={
            "name": "AllStoredItems",
            "type": "Element",
        },
    )


@dataclass
class SimpleFabricatorSaveData(DeviceImportExportSaveData):
    fabricator_job: Optional[FabricatorJob] = field(
        default=None,
        metadata={
            "name": "FabricatorJob",
            "type": "Element",
        },
    )
    current_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "CurrentIndex",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SlotHandlerBaseSaveData(DeviceImportExportSaveData):
    current_output: Optional[int] = field(
        default=None,
        metadata={
            "name": "CurrentOutput",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SorterMotherboardSaveData(MultiMotherboardSaveData):
    pass


@dataclass
class SorterSaveData(DeviceImportExportSaveData):
    current_output: Optional[int] = field(
        default=None,
        metadata={
            "name": "CurrentOutput",
            "type": "Element",
            "required": True,
        },
    )
    filters: Optional[ArrayOfFilterReference] = field(
        default=None,
        metadata={
            "name": "Filters",
            "type": "Element",
        },
    )


@dataclass
class TerrainSettings(DataCollection):
    curvature: Optional[FloatReference] = field(
        default=None,
        metadata={
            "name": "Curvature",
            "type": "Element",
        },
    )
    mini_map: Optional[TextureReference] = field(
        default=None,
        metadata={
            "name": "MiniMap",
            "type": "Element",
        },
    )
    lava: Optional[LavaData] = field(
        default=None,
        metadata={
            "name": "Lava",
            "type": "Element",
        },
    )
    terrain_props: Optional[TerrainProps] = field(
        default=None,
        metadata={
            "name": "TerrainProps",
            "type": "Element",
        },
    )
    material_settings: Optional[MaterialSettings] = field(
        default=None,
        metadata={
            "name": "MaterialSettings",
            "type": "Element",
        },
    )
    path: Optional[str] = field(
        default=None,
        metadata={
            "name": "Path",
            "type": "Attribute",
        },
    )
    world_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "WorldSize",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TraderData:
    type_value: list[SlotIdReference] = field(
        default_factory=list,
        metadata={
            "name": "Type",
            "type": "Element",
        },
    )
    name: list[LocalizedStringReference] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    buy: list[BuyData] = field(
        default_factory=list,
        metadata={
            "name": "Buy",
            "type": "Element",
        },
    )
    sell: list[SellData] = field(
        default_factory=list,
        metadata={
            "name": "Sell",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    shuttle_variant: Optional[ShuttleVariant] = field(
        default=None,
        metadata={
            "name": "ShuttleVariant",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class VendingMachineSaveData(DeviceImportExportSaveData):
    current_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "CurrentIndex",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class AdvancedComposterSaveData(DeviceInputOutputImportExportSaveData):
    unprocessed_items: Optional[int] = field(
        default=None,
        metadata={
            "name": "UnprocessedItems",
            "type": "Element",
            "required": True,
        },
    )
    saved_decay_food_quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "SavedDecayFoodQuantity",
            "type": "Element",
            "required": True,
        },
    )
    saved_normal_food_quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "SavedNormalFoodQuantity",
            "type": "Element",
            "required": True,
        },
    )
    saved_biomass_quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "SavedBiomassQuantity",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class CarbonSequesterSaveData(DeviceInputOutputImportExportSaveData):
    pass


@dataclass
class CelestialBodies(CelestialCollection):
    class Meta:
        nillable = True


@dataclass
class DeepMinerSaveData(DeviceInputOutputImportExportSaveData):
    is_reached_bed_rock: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsReachedBedRock",
            "type": "Element",
            "required": True,
        },
    )
    drill_position: Optional[Vector3] = field(
        default=None,
        metadata={
            "name": "DrillPosition",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DeviceInputOutputImportExportCircuitSaveData(
    DeviceInputOutputImportExportSaveData
):
    device_ids: list[int] = field(
        default_factory=list,
        metadata={
            "name": "DeviceIDs",
            "type": "Element",
        },
    )


@dataclass
class DispersalTowerSaveData(DeviceInputOutputImportExportSaveData):
    pass


@dataclass
class FiltrationMachineSaveData(MachineSaveData):
    pass


@dataclass
class FurnaceSaveData(DeviceInputOutputImportExportSaveData):
    pass


@dataclass
class ResearchMachineSaveData(DeviceInputOutputImportExportSaveData):
    pod_type_to_find_saved: Optional[int] = field(
        default=None,
        metadata={
            "name": "PodTypeToFindSaved",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class StackerSaveData(SlotHandlerBaseSaveData):
    setting: Optional[float] = field(
        default=None,
        metadata={
            "name": "Setting",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class VendingMachineRefrigeratedSaveData(VendingMachineSaveData):
    setting: Optional[float] = field(
        default=None,
        metadata={
            "name": "Setting",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class WorldSettingData(DataCollection):
    is_tutorial: Optional[BoolReference] = field(
        default=None,
        metadata={
            "name": "IsTutorial",
            "type": "Element",
        },
    )
    display_badge: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DisplayBadge",
            "type": "Element",
            "nillable": True,
        },
    )
    description: Optional[LocalizedStringReference] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
        },
    )
    short_description: Optional[LocalizedStringReference] = field(
        default=None,
        metadata={
            "name": "ShortDescription",
            "type": "Element",
        },
    )
    rating: Optional[LocalizedStringReference] = field(
        default=None,
        metadata={
            "name": "Rating",
            "type": "Element",
        },
    )
    summary_text: Optional[LocalizedStringReference] = field(
        default=None,
        metadata={
            "name": "SummaryText",
            "type": "Element",
        },
    )
    sky_box_material_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SkyBoxMaterialName",
            "type": "Element",
        },
    )
    sun_prefab_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SunPrefabName",
            "type": "Element",
        },
    )
    max_sun_intensity: Optional[float] = field(
        default=None,
        metadata={
            "name": "MaxSunIntensity",
            "type": "Element",
            "required": True,
        },
    )
    spawn: list[SpawnData] = field(
        default_factory=list,
        metadata={
            "name": "Spawn",
            "type": "Element",
        },
    )
    start_condition: list[StartConditionData] = field(
        default_factory=list,
        metadata={
            "name": "StartCondition",
            "type": "Element",
        },
    )
    start_location: list[StartLocationData] = field(
        default_factory=list,
        metadata={
            "name": "StartLocation",
            "type": "Element",
        },
    )
    random_start_location: list[RoundRobinStartLocationData] = field(
        default_factory=list,
        metadata={
            "name": "RandomStartLocation",
            "type": "Element",
        },
    )
    playable_area: list[PlayableAreaData] = field(
        default_factory=list,
        metadata={
            "name": "PlayableArea",
            "type": "Element",
        },
    )
    skybox: Optional[ArrayOfPlanetPrefab1] = field(
        default=None,
        metadata={
            "name": "Skybox",
            "type": "Element",
        },
    )
    celestial_bodies: Optional[CelestialCollection] = field(
        default=None,
        metadata={
            "name": "CelestialBodies",
            "type": "Element",
        },
    )
    celestial_constants: Optional[CelestialConstantsReference] = field(
        default=None,
        metadata={
            "name": "CelestialConstants",
            "type": "Element",
        },
    )
    playable_body: Optional[PlayableBodyReference] = field(
        default=None,
        metadata={
            "name": "PlayableBody",
            "type": "Element",
        },
    )
    primary_body: Optional[PrimaryBodyReference] = field(
        default=None,
        metadata={
            "name": "PrimaryBody",
            "type": "Element",
        },
    )
    ambient_lighting: Optional[AmbientLightingReference] = field(
        default=None,
        metadata={
            "name": "AmbientLighting",
            "type": "Element",
        },
    )
    global_atmosphere: Optional[GlobalAtmosphereData] = field(
        default=None,
        metadata={
            "name": "GlobalAtmosphere",
            "type": "Element",
        },
    )
    preview_scene: Optional[PreviewScene] = field(
        default=None,
        metadata={
            "name": "PreviewScene",
            "type": "Element",
        },
    )
    gravity: Optional[float] = field(
        default=None,
        metadata={
            "name": "Gravity",
            "type": "Element",
            "required": True,
        },
    )
    lava_level: Optional[float] = field(
        default=None,
        metadata={
            "name": "LavaLevel",
            "type": "Element",
            "required": True,
        },
    )
    has_lava: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasLava",
            "type": "Element",
            "required": True,
        },
    )
    seed: Optional[int] = field(
        default=None,
        metadata={
            "name": "Seed",
            "type": "Element",
            "required": True,
        },
    )
    atmospheric_scattering: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AtmosphericScattering",
            "type": "Element",
            "required": True,
        },
    )
    atmospheric_scattering_data: Optional[AtmosphericScatteringData] = field(
        default=None,
        metadata={
            "name": "AtmosphericScatteringData",
            "type": "Element",
        },
    )
    ambient_light_min: Optional[float] = field(
        default=None,
        metadata={
            "name": "AmbientLightMin",
            "type": "Element",
            "required": True,
        },
    )
    ambient_light_max: Optional[float] = field(
        default=None,
        metadata={
            "name": "AmbientLightMax",
            "type": "Element",
            "required": True,
        },
    )
    ambient_sky_color: Optional[Color1] = field(
        default=None,
        metadata={
            "name": "AmbientSkyColor",
            "type": "Element",
            "required": True,
        },
    )
    ambient_equator_color: Optional[Color1] = field(
        default=None,
        metadata={
            "name": "AmbientEquatorColor",
            "type": "Element",
            "required": True,
        },
    )
    ambient_ground_color: Optional[Color1] = field(
        default=None,
        metadata={
            "name": "AmbientGroundColor",
            "type": "Element",
            "required": True,
        },
    )
    set_sun_in_skybox: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SetSunInSkybox",
            "type": "Element",
            "required": True,
        },
    )
    stars: Optional[ArrayOfStarData] = field(
        default=None,
        metadata={
            "name": "Stars",
            "type": "Element",
        },
    )
    preview_button: Optional[TextureReference] = field(
        default=None,
        metadata={
            "name": "PreviewButton",
            "type": "Element",
        },
    )
    lava_color: Optional[Color1] = field(
        default=None,
        metadata={
            "name": "LavaColor",
            "type": "Element",
            "required": True,
        },
    )
    has_custom_lava_color: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasCustomLavaColor",
            "type": "Element",
            "required": True,
        },
    )
    ambience_sound: Optional[str] = field(
        default=None,
        metadata={
            "name": "AmbienceSound",
            "type": "Element",
        },
    )
    weather_event: list[WeatherEvent] = field(
        default_factory=list,
        metadata={
            "name": "WeatherEvent",
            "type": "Element",
        },
    )
    space_map: Optional[SpaceMapData] = field(
        default=None,
        metadata={
            "name": "SpaceMap",
            "type": "Element",
        },
    )
    world_objective: list[WorldObjectiveCollection] = field(
        default_factory=list,
        metadata={
            "name": "WorldObjective",
            "type": "Element",
        },
    )
    terrain_settings: Optional[TerrainSettings] = field(
        default=None,
        metadata={
            "name": "TerrainSettings",
            "type": "Element",
        },
    )
    region_set: list[RegionSet] = field(
        default_factory=list,
        metadata={
            "name": "RegionSet",
            "type": "Element",
        },
    )
    geographic_region_data: Optional[GeographicRegionData] = field(
        default=None,
        metadata={
            "name": "GeographicRegionData",
            "type": "Element",
        },
    )
    deep_minables_region_data: Optional[DeepMinablesRegionData] = field(
        default=None,
        metadata={
            "name": "DeepMinablesRegionData",
            "type": "Element",
        },
    )
    minables: list[MinablesGenerationData] = field(
        default_factory=list,
        metadata={
            "name": "Minables",
            "type": "Element",
        },
    )
    deep_minables: list[DeepMinablesGenerationData] = field(
        default_factory=list,
        metadata={
            "name": "DeepMinables",
            "type": "Element",
        },
    )
    point_of_interest: list[PointOfInterest] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterest",
            "type": "Element",
        },
    )
    achievement_chain: list[AchievementChainData] = field(
        default_factory=list,
        metadata={
            "name": "AchievementChain",
            "type": "Element",
        },
    )
    achievement_survival: list[AchievementSurvivalData] = field(
        default_factory=list,
        metadata={
            "name": "AchievementSurvival",
            "type": "Element",
        },
    )
    hidden: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Hidden",
            "type": "Attribute",
            "required": True,
        },
    )
    priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "Priority",
            "type": "Attribute",
            "required": True,
        },
    )
    deprecated: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Deprecated",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ArrayOfWorldSettingData:
    world: list[WorldSettingData] = field(
        default_factory=list,
        metadata={
            "name": "World",
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class CombustionCentrifugeSaveData(DeviceInputOutputImportExportCircuitSaveData):
    throttle: Optional[float] = field(
        default=None,
        metadata={
            "name": "Throttle",
            "type": "Element",
            "required": True,
        },
    )
    combustion_limiter: Optional[float] = field(
        default=None,
        metadata={
            "name": "CombustionLimiter",
            "type": "Element",
            "required": True,
        },
    )
    rpm: Optional[float] = field(
        default=None,
        metadata={
            "name": "Rpm",
            "type": "Element",
            "required": True,
        },
    )
    stress: Optional[float] = field(
        default=None,
        metadata={
            "name": "Stress",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class IndustrialBurnerSaveData(FurnaceSaveData):
    stress: Optional[float] = field(
        default=None,
        metadata={
            "name": "Stress",
            "type": "Element",
            "required": True,
        },
    )
    stressed_to_failure: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StressedToFailure",
            "type": "Element",
            "required": True,
        },
    )
    machine_temperature: Optional[float] = field(
        default=None,
        metadata={
            "name": "MachineTemperature",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class GameData:
    centrifuge_recipes: Optional[ArrayOfRecipeData] = field(
        default=None,
        metadata={
            "name": "CentrifugeRecipes",
            "type": "Element",
        },
    )
    furnace_recipes: Optional[ArrayOfRecipeData] = field(
        default=None,
        metadata={
            "name": "FurnaceRecipes",
            "type": "Element",
        },
    )
    advanced_furnace_recipes: Optional[ArrayOfRecipeData] = field(
        default=None,
        metadata={
            "name": "AdvancedFurnaceRecipes",
            "type": "Element",
        },
    )
    arc_furnace_recipes: Optional[ArrayOfRecipeData] = field(
        default=None,
        metadata={
            "name": "ArcFurnaceRecipes",
            "type": "Element",
        },
    )
    microwave_recipes: Optional[ArrayOfRecipeData] = field(
        default=None,
        metadata={
            "name": "MicrowaveRecipes",
            "type": "Element",
        },
    )
    packaging_machine_recipes: Optional[ArrayOfRecipeData] = field(
        default=None,
        metadata={
            "name": "PackagingMachineRecipes",
            "type": "Element",
        },
    )
    autolathe_recipes: Optional[ArrayOfRecipeData] = field(
        default=None,
        metadata={
            "name": "AutolatheRecipes",
            "type": "Element",
        },
    )
    automated_oven_recipes: Optional[ArrayOfRecipeData] = field(
        default=None,
        metadata={
            "name": "AutomatedOvenRecipes",
            "type": "Element",
        },
    )
    electronics_printer_recipes: Optional[ArrayOfRecipeData] = field(
        default=None,
        metadata={
            "name": "ElectronicsPrinterRecipes",
            "type": "Element",
        },
    )
    security_printer_recipes: Optional[ArrayOfRecipeData] = field(
        default=None,
        metadata={
            "name": "SecurityPrinterRecipes",
            "type": "Element",
        },
    )
    rocket_manufactory_recipes: Optional[ArrayOfRecipeData] = field(
        default=None,
        metadata={
            "name": "RocketManufactoryRecipes",
            "type": "Element",
        },
    )
    hydraulic_pipe_bender_recipes: Optional[ArrayOfRecipeData] = field(
        default=None,
        metadata={
            "name": "HydraulicPipeBenderRecipes",
            "type": "Element",
        },
    )
    tool_manufactory_recipes: Optional[ArrayOfRecipeData] = field(
        default=None,
        metadata={
            "name": "ToolManufactoryRecipes",
            "type": "Element",
        },
    )
    chemistry_recipes: Optional[ArrayOfRecipeData] = field(
        default=None,
        metadata={
            "name": "ChemistryRecipes",
            "type": "Element",
        },
    )
    ingot_recipes: Optional[ArrayOfRecipeData] = field(
        default=None,
        metadata={
            "name": "IngotRecipes",
            "type": "Element",
        },
    )
    recycle_recipes: Optional[ArrayOfRecipeData] = field(
        default=None,
        metadata={
            "name": "RecycleRecipes",
            "type": "Element",
        },
    )
    terraforming_manufactory_recipes: Optional[ArrayOfRecipeData] = field(
        default=None,
        metadata={
            "name": "TerraformingManufactoryRecipes",
            "type": "Element",
        },
    )
    minable_visualiser: list[MinableVisualiserData] = field(
        default_factory=list,
        metadata={
            "name": "MinableVisualiser",
            "type": "Element",
        },
    )
    reagent_grinder_recipes: Optional[ArrayOfProcessingData] = field(
        default=None,
        metadata={
            "name": "ReagentGrinderRecipes",
            "type": "Element",
        },
    )
    world_settings: Optional[ArrayOfWorldSettingData] = field(
        default=None,
        metadata={
            "name": "WorldSettings",
            "type": "Element",
        },
    )
    trader: list[TraderData] = field(
        default_factory=list,
        metadata={
            "name": "Trader",
            "type": "Element",
        },
    )
    room_type_rule: list[RoomTypeRuleData] = field(
        default_factory=list,
        metadata={
            "name": "RoomTypeRule",
            "type": "Element",
        },
    )
    contact_slot: list[ContactSlotData] = field(
        default_factory=list,
        metadata={
            "name": "ContactSlot",
            "type": "Element",
        },
    )
    space_map: list[SpaceMapData] = field(
        default_factory=list,
        metadata={
            "name": "SpaceMap",
            "type": "Element",
        },
    )
    celestial_bodies: Optional[ArrayOfCelestialBodyTemplate] = field(
        default=None,
        metadata={
            "name": "CelestialBodies",
            "type": "Element",
        },
    )
    icon: list[NodeIcon] = field(
        default_factory=list,
        metadata={
            "name": "Icon",
            "type": "Element",
        },
    )
    spawn: list[SpawnData] = field(
        default_factory=list,
        metadata={
            "name": "Spawn",
            "type": "Element",
        },
    )
    start_condition: list[StartConditionData] = field(
        default_factory=list,
        metadata={
            "name": "StartCondition",
            "type": "Element",
        },
    )
    start_location: list[StartLocationData] = field(
        default_factory=list,
        metadata={
            "name": "StartLocation",
            "type": "Element",
        },
    )
    random_start_location: list[RoundRobinStartLocationData] = field(
        default_factory=list,
        metadata={
            "name": "RandomStartLocation",
            "type": "Element",
        },
    )
    world_objective: list[WorldObjectiveCollection] = field(
        default_factory=list,
        metadata={
            "name": "WorldObjective",
            "type": "Element",
        },
    )
    objective: list[WorldObjective] = field(
        default_factory=list,
        metadata={
            "name": "Objective",
            "type": "Element",
        },
    )
    buy: list[BuyData] = field(
        default_factory=list,
        metadata={
            "name": "Buy",
            "type": "Element",
        },
    )
    sell: list[SellData] = field(
        default_factory=list,
        metadata={
            "name": "Sell",
            "type": "Element",
        },
    )
    paint_mix_recipes: Optional[ArrayOfRecipeData] = field(
        default=None,
        metadata={
            "name": "PaintMixRecipes",
            "type": "Element",
        },
    )
    thing_mods: Optional[ArrayOfThingModData] = field(
        default=None,
        metadata={
            "name": "ThingMods",
            "type": "Element",
        },
    )
    reagent_trade_values: Optional[ArrayOfReagentTradeData] = field(
        default=None,
        metadata={
            "name": "ReagentTradeValues",
            "type": "Element",
        },
    )
    gas_mole_trade_values: Optional[ArrayOfGasTradeData] = field(
        default=None,
        metadata={
            "name": "GasMoleTradeValues",
            "type": "Element",
        },
    )
    difficulty_settings: Optional[ArrayOfDifficultySetting] = field(
        default=None,
        metadata={
            "name": "DifficultySettings",
            "type": "Element",
        },
    )
    default_rocket_names: Optional[ArrayOfRocketName] = field(
        default=None,
        metadata={
            "name": "DefaultRocketNames",
            "type": "Element",
        },
    )
    ghgindex: list[TerraformingGasCurveData] = field(
        default_factory=list,
        metadata={
            "name": "GHGIndex",
            "type": "Element",
        },
    )
    atmospheric_scattering_blend: list[AtmosphericScatteringBlendData] = field(
        default_factory=list,
        metadata={
            "name": "AtmosphericScatteringBlend",
            "type": "Element",
        },
    )
    life_requirements: list[LifeRequirementsData] = field(
        default_factory=list,
        metadata={
            "name": "LifeRequirements",
            "type": "Element",
        },
    )
    custom_plant: list[CustomPlantData] = field(
        default_factory=list,
        metadata={
            "name": "CustomPlant",
            "type": "Element",
        },
    )
    custom_seed: list[CustomSeedData] = field(
        default_factory=list,
        metadata={
            "name": "CustomSeed",
            "type": "Element",
        },
    )
    blueprint: list[BlueprintData] = field(
        default_factory=list,
        metadata={
            "name": "Blueprint",
            "type": "Element",
        },
    )
    weather_event: list[WeatherEvent] = field(
        default_factory=list,
        metadata={
            "name": "WeatherEvent",
            "type": "Element",
        },
    )
    server_provider_data: list[ServerProvider] = field(
        default_factory=list,
        metadata={
            "name": "ServerProviderData",
            "type": "Element",
        },
    )
    minables: list[MinablesGenerationData] = field(
        default_factory=list,
        metadata={
            "name": "Minables",
            "type": "Element",
        },
    )
    deep_minables: list[DeepMinablesGenerationData] = field(
        default_factory=list,
        metadata={
            "name": "DeepMinables",
            "type": "Element",
        },
    )
    ore_vein: list[VeinGenerationData] = field(
        default_factory=list,
        metadata={
            "name": "OreVein",
            "type": "Element",
        },
    )
    expression: list[FacialExpressionData] = field(
        default_factory=list,
        metadata={
            "name": "Expression",
            "type": "Element",
        },
    )
