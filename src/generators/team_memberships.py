import random

# Generate team memberships (many-to-many)
def generate_team_memberships(cursor, team_ids, user_ids):
    # Each user can belong to 1–3 teams
    for user_id in user_ids:
        # Randomly select teams for the user
        teams_for_user = random.sample(team_ids, k=random.randint(1, min(3, len(team_ids))))
        # Assign user to selected teams
        for team_id in teams_for_user:
            # Insert membership record into the database
            cursor.execute(
                "INSERT INTO team_memberships (team_id, user_id) VALUES (?, ?)",
                (team_id, user_id)
            )
