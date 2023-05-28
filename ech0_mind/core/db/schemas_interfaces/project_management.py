from nexus_db.core.api.nexus_db_interface import NexusDbInterface
from util_scripts.logs.log_handler import LogHandler
from ech0_mind.core.project_management.tables import project_management_tables

class ProjectManagementDbInterface:
    def __init__(self): 
        self.logger = LogHandler()
        self.db_interface = NexusDbInterface()
        self.schema_name = "project_management"
    
    def create_schema(self):
        self.db_interface.create_schema(schema_name=self.schema_name)

    def create_tables(self):
        for project_management_table in project_management_tables:
            table_name = project_management_table["table_name"]
            table_columns = project_management_table["table_columns"]
            print(table_columns)
            self.add_new_table(table_name=table_name, table_columns=table_columns)


        self.logger.print_success(f"{self.schema_name} tables created successfully.")
    
    def add_new_table(self, table_name, table_columns):
        response = self.db_interface.create_table(
            schema_name=self.schema_name,
            table_name=table_name,
            table_columns=table_columns
        )
        self.logger.print_info(f"{table_name} in {self.schema_name}: {response.json()}")
        

