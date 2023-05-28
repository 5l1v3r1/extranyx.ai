# ech0_mind/cli/commands/db.py
from typer import Typer, Option
from nexus_db.core.api.nexus_db_interface import NexusDbInterface
app = Typer()

@app.command()
def create_db():
    db_interface = NexusDbInterface()
    db_interface.create_db("ech0_mind")


