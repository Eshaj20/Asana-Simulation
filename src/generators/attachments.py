import uuid
from datetime import datetime
import random

# Possible attachment file names
FILE_NAMES = ["report.pdf", "design.png", "specs.docx", "screenshot.jpg"]

# Generate attachments for tasks
def generate_attachments(cursor, task_ids, user_ids):
    # Approximately 30% of tasks get attachments
    for task_id in task_ids:
        # Randomly decide if this task gets an attachment
        if random.random() < 0.3:  # ~30% of tasks get attachments
            # Generate attachment details
            attachment_id = str(uuid.uuid4())
            # Select a user to upload the attachment
            uploaded_by = random.choice(user_ids)
            # Select a random file
            file_name = random.choice(FILE_NAMES)
            # Construct file URL and other attributes
            file_url = f"https://example.com/files/{file_name}"
            # Determine file type and size
            file_type = file_name.split('.')[-1]
            # Determine file size randomly between 10KB to 2MB
            file_size = random.randint(10_000, 2_000_000)  # Bytes
            # Set creation time
            created_at = datetime.now()
            # Insert the attachment record into the database
            cursor.execute(
                "INSERT INTO attachments (id, task_id, uploaded_by, file_name, file_url, file_type, file_size, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (attachment_id, task_id, uploaded_by, file_name, file_url, file_type, file_size, created_at)
            )
