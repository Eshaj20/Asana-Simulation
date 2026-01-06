import uuid
from datetime import datetime

# Generate organizations
def generate_organizations(cursor, count=1):
    # List to hold generated organization IDs
    org_ids = []
    # Create specified number of organizations
    for i in range(count):
        # Generate unique ID for the organization
        org_id = str(uuid.uuid4())
        # Create organization name
        name = f"Organization {i+1}"
        # Get current timestamp for created_at
        created_at = datetime.now()
        # Insert the organization record into the database
        cursor.execute(
            "INSERT INTO organizations (id, name, created_at) VALUES (?, ?, ?)",
            (org_id, name, created_at)
        )
        org_ids.append(org_id) # Append to the list of organization IDs
    return org_ids # Return the list of generated organization IDs
