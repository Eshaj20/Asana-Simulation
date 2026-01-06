import random

# Generate task-tag associations (many-to-many)
def generate_task_tags(cursor, task_ids, tag_ids):
    # Each task can have 0–3 tags
    for task_id in task_ids:
        # Each task can have 0–3 tags
        tags_for_task = random.sample(tag_ids, k=random.randint(0, min(3, len(tag_ids))))
        # Assign tags to the task
        for tag_id in tags_for_task:
            # Insert association record into the database
            cursor.execute(
                "INSERT INTO task_tags (task_id, tag_id) VALUES (?, ?)",
                (task_id, tag_id)
            )
