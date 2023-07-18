project_management_tables = [
    {
        "table_name": "project",
        "table_columns": {
            'project_id': 'int primary key',
            'project_name': 'text',
            'project_description': 'text',
            'project_feature_ids': 'uuidv4()',
            'project_web_copy_id': 'uuidv4()',
            'project_user_story_ids': 'uuidv4()',
            'project_tech_stack_id': 'uuidv4()',
            'project_overview': 'uuidv4()',

        }
    },
    {
        "table_name": "project_feature",
        "table_columns": {
            'id': '',
            'project_id': '',
            'project_feature_description': '',
            'project_feature_category_id': '',
        }
    }
]