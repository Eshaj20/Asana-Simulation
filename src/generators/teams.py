import uuid  
from datetime import datetime  
import random  

def generate_teams(cursor, organization_id, count=3):
    
    team_ids = []  # List to store the IDs of the teams we create

    for i in range(count):
        # Generate a unique ID for the team
        team_id = str(uuid.uuid4())

        # Create a team name. Example: "Team 1 of Org"
        name = f"Team {i+1} of Org"

        # Get the current timestamp for the created_at column
        created_at = datetime.now()

        # Insert the new team record into the database
        cursor.execute(
            "INSERT INTO teams (id, organization_id, name, created_at) VALUES (?, ?, ?, ?)",
            (team_id, organization_id, name, created_at)
        )

        # Add the generated team_id to our list
        team_ids.append(team_id)

    # Return the list of generated team IDs
    return team_ids
