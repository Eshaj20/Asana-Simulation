import uuid
from datetime import datetime, timedelta
import random

# Generate comments for tasks
def generate_comments(cursor, task_ids, user_ids):
    # Approximately 50% of tasks get comments
    for task_id in task_ids:
        if random.random() < 0.5:  # ~50% of tasks get comments
            # Each selected task gets 1–3 comments
            for _ in range(random.randint(1, 3)):
                # Generate comment details
                comment_id = str(uuid.uuid4())
                author_id = random.choice(user_ids)
                body = f"This is a comment by {author_id}."
                # Generate a random timestamp for the comment
                created_at = datetime.now() - timedelta(days=random.randint(0, 30))
                # Insert the comment record into the database
                cursor.execute(
                    "INSERT INTO comments (id, task_id, author_id, body, created_at) VALUES (?, ?, ?, ?, ?)",
                    (comment_id, task_id, author_id, body, created_at)
                )
