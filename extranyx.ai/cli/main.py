# ech0_mind/cli/main.py
import typer

from ech0_mind.cli.commands import db, project_management


def create_app():
    app = typer.Typer()
    app.add_typer(db.app, name="db")
    app.add_typer(project_management.app, name="project_management")
    return app

app = create_app()

if __name__ == "__main__":
    app()
