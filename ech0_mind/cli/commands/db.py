# ech0_mind/cli/commands/db.py
from typer import Typer, Option
from nexus_db.core.api.db_direct_access_point import DbDirectAccessPoint
app = Typer()

@app.command()
def create_db():
    db_interface = DbDirectAccessPoint()
    db_interface.create_db("ech0_mind")


