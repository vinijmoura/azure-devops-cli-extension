# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from ._format import transform_project_table_output, transform_projects_table_output

from .credentials import credential_set, credential_clear
from .feedback import feedback
from .configure import configure
from .project import create_project, show_project, list_projects

def load_team_commands(self, _):
    with self.command_group('dev') as g:
        g.custom_command('login', 'dev.team.credentials.credential_set')
        g.custom_command('logout', 'dev.team.credentials.credential_clear')
        g.custom_command('feedback', 'dev.team.feedback.feedback')
        g.custom_command('configure', 'dev.team.configure.configure')
        g.custom_command('project create', 'dev.team.project.create_project', table_transformer=transform_project_table_output)
        g.custom_command('project show', 'dev.team.project.show_project', table_transformer=transform_project_table_output)
        g.custom_command('project list', 'dev.team.project.list_projects', table_transformer=transform_projects_table_output)
