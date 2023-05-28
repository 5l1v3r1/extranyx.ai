# ech0_mind/cli/commands/db.py
from typer import Typer, Option
from ech0_mind.core.db.schemas_interfaces.project_management import ProjectManagementDbInterface

app = Typer()
db_interface = ProjectManagementDbInterface()

@app.command()
def create_schema():
    db_interface.create_schema()

@app.command()
def init_db():
    print('creating...')
    db_interface.create_schema()
    print('finished')
    print('attempting to create tables...')
    db_interface.create_tables()
    print("finished")


