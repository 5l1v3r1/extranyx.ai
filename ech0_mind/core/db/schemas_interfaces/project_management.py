from nexus_db.core.api.cross_app_db_interface import CrossAppDbInterface

class ProjectManagementDbInterface(CrossAppDbInterface):
    def __init__(self): 
        super().__init__(schema_name="project_management")