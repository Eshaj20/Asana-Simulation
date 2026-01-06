import uuid

# Default sections to be created for each project
DEFAULT_SECTIONS = ["To Do", "In Progress", "Done"]

# Generate sections for each project
def generate_sections(cursor, project_ids):
    section_map = {} # Map of project_id to its section IDs
    # Create default sections for each project
    for project_id in project_ids:
        section_ids = [] # List to hold section IDs for this project
        # Create each default section
        for pos, name in enumerate(DEFAULT_SECTIONS):
            section_id = str(uuid.uuid4()) # Generate unique ID for the section
            # Insert the section into the database
            cursor.execute(
                "INSERT INTO sections (id, project_id, name, position) VALUES (?, ?, ?, ?)",
                (section_id, project_id, name, pos)
            )
            # Append the generated section ID to the list
            section_ids.append(section_id)
        section_map[project_id] = section_ids # Map project_id to its section IDs
    return section_map # Return the map of project IDs to their section IDs
