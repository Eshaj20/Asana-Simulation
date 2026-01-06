import uuid
from datetime import datetime
import random

# Default project types
PROJECT_TYPES = ["Engineering", "Marketing", "Operations"]

# Generate projects for each team
def generate_projects(cursor, team_ids, count_per_team=2):
    project_ids = [] # List to hold generated project IDs
    # Create projects for each team
    for team_id in team_ids:
        # Create specified number of projects per team
        for i in range(count_per_team):
            project_id = str(uuid.uuid4()) # Generate unique ID for the project
            # Create project name and type
            name = f"Project {i+1} of Team"
            project_type = random.choice(PROJECT_TYPES)
            # Get current timestamp for created_at
            created_at = datetime.now()
            # Insert the new project record into the database
            cursor.execute(
                "INSERT INTO projects (id, team_id, name, project_type, created_at) VALUES (?, ?, ?, ?, ?)",
                (project_id, team_id, name, project_type, created_at)
            )
            project_ids.append(project_id) # Append to the list of project IDs
    return project_ids # Return the list of generated project IDs
