import typer
from pathlib import Path

from .save_data import SaveData

app = typer.Typer()


def validate_filename(filename: Path):
    if not filename.exists():
        typer.echo(f"Error: File '{filename}' does not exist.", err=True)
        raise typer.Exit(code=1)
    if not filename.suffix in [".xml", ".save"]:
        typer.echo("Error: filename must end with '.xml' or '.save'", err=True)
        raise typer.Exit(code=1)


def load_file(filename: Path) -> SaveData:
    try:
        validate_filename(filename)
        data = SaveData(str(filename))
        return data
    except Exception as e:
        print("Error loading file:", e)
        raise typer.Exit(code=1)


@app.command("i")
@app.command("info")
def info(filename: Path):
    data = load_file(filename)
    data.print_info()


@app.command("m")
@app.command("move")
def move(filename: Path, x: float, y: float, z: float):
    data = load_file(filename)

    data.move_player(x, y, z)
    data.save(data.filename.replace(".save", "_moved.save"))


if __name__ == "__main__":
    app()
