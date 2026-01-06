import uuid
import random

# Default tags to be created
DEFAULT_TAGS = [
    "Urgent", "Bug", "Feature", "Improvement", "High Priority", "Low Priority"
]

# Generate tags
def generate_tags(cursor):
    tag_ids = [] # List to hold generated tag IDs
    # Create each default tag
    for name in DEFAULT_TAGS:
        tag_id = str(uuid.uuid4()) # Generate unique ID for the tag
        # Insert the tag into the database
        cursor.execute(
            "INSERT INTO tags (id, name) VALUES (?, ?)",
            (tag_id, name)
        )
        # Append the generated tag ID to the list
        tag_ids.append(tag_id)
    return tag_ids # Return the list of generated tag IDs
