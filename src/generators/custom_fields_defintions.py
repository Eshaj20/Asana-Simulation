import uuid
import random

# Possible custom field names and types
FIELD_NAMES = ["Priority", "Effort", "Status"]
FIELD_TYPES = ["text", "number", "enum"]

# Generate custom fields for each project
def generate_custom_fields_defintions(cursor, project_ids):
    field_ids = [] # List to hold generated field IDs
    # Create random number of custom fields for each project
    for project_id in project_ids:
        # Create between 1 to 3 custom fields per project
        for i in range(random.randint(1, 3)):
            # Generate unique ID for the custom field
            field_id = str(uuid.uuid4())
            # Randomly select field name and type
            name = random.choice(FIELD_NAMES)
            field_type = random.choice(FIELD_TYPES)
            # Insert the custom field definition into the database
            cursor.execute(
                "INSERT INTO custom_field_definitions (id, project_id, name, field_type) VALUES (?, ?, ?, ?)",
                (field_id, project_id, name, field_type)
            )
            field_ids.append(field_id) # Append to the list of field IDs
    return field_ids # Return the list of generated custom field IDs
