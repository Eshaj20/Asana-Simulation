import random

# Generate custom field values for tasks
def generate_custom_field_values(cursor, task_ids, field_ids):
    # Each task can have 0–3 custom field values
    for task_id in task_ids:
        # Randomly select fields for this task
        fields_for_task = random.sample(field_ids, k=random.randint(0, min(3, len(field_ids))))
        # Assign values to the selected fields
        for field_id in fields_for_task:
            # Generate a random value based on field type (simplified here)
            value = random.choice(["High", "Medium", "Low", "5", "3", "Done", "In Progress"])
            # Insert the custom field value record into the database
            cursor.execute(
                "INSERT INTO custom_field_values (task_id, field_id, value) VALUES (?, ?, ?)",
                (task_id, field_id, value)
            )
