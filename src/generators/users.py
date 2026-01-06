import uuid
from datetime import datetime
import random

# Available roles for generated users
ROLES = ["Engineer", "Manager", "Designer", "Marketer", "QA"]

# Generate and insert users for a given organization
def generate_users(cursor, organization_id, count=10):
    user_ids = []

    # Create the specified number of users
    for i in range(count):
        # Generate a unique user ID
        user_id = str(uuid.uuid4())

        # Assign a placeholder full name
        full_name = f"User {i+1}"

        # Generate a simple unique email address
        email = f"user{i+1}@example.com"

        # Randomly assign a role from the predefined list
        role = random.choice(ROLES)

        # Set user creation time
        created_at = datetime.now()

        # Insert the user record into the database
        cursor.execute(
            "INSERT INTO users (id, organization_id, full_name, email, role, created_at) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (user_id, organization_id, full_name, email, role, created_at)
        )

        user_ids.append(user_id)

    return user_ids
