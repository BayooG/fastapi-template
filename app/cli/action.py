import typer
from fastapi_migrations import MigrationsConfig, Migrations

app: typer.Typer = typer.Typer()

@app.command()
def show() -> None:
    config = MigrationsConfig()

    migrations = Migrations(config)

    migrations.show()