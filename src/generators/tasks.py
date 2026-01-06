import uuid
from datetime import datetime, timedelta
import random

# Generate tasks for each project
def generate_tasks(cursor, project_ids, section_map, user_ids, count=50):
    # Iterate over each project to create tasks
    for project_id in project_ids:
        # Get sections for the current project
        sections = section_map[project_id]
        # Create specified number of tasks per project
        for i in range(count // len(project_ids)):
            # Generate unique ID for the task
            task_id = str(uuid.uuid4())
            # Randomly assign section and assignee
            section_id = random.choice(sections)
            assignee_id = random.choice(user_ids + [None])  # Some tasks unassigned are also there
            # Create task name and description
            name = f"Task {i+1} of Project"
            description = f"This is the description for {name}."
            # Set creation time and other attributes
            created_at = datetime.now() - timedelta(days=random.randint(0, 30))
            # Set completion status and timestamps
            completed = random.choice([True, False])
            completed_at = created_at + timedelta(days=random.randint(1, 14)) if completed else None
            # Set due date
            due_date = created_at + timedelta(days=random.randint(1, 20))
            # Insert the task record into the database
            cursor.execute(
                "INSERT INTO tasks (id, project_id, section_id, assignee_id, parent_task_id, name, description, due_date, completed, created_at, completed_at) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (task_id, project_id, section_id, assignee_id, None, name, description, due_date, completed, created_at, completed_at)
            )
