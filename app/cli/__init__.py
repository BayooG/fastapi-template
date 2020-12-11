import typer

from fastapi_migrations.cli import MigrationsCli
import app.cli.action as action

# main cli app
app: typer.Typer = typer.Typer()

# these are our cli actions
app.add_typer(action.app, name='action', help='Common actions the app do')

# this line adds the fastapi-migrations cli commands to our app
app.add_typer(MigrationsCli())