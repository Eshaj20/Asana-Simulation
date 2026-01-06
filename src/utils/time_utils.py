from datetime import datetime, timedelta
import random

# Return a random datetime within the past given number of days
def random_past_datetime(days=180):
    return datetime.utcnow() - timedelta(days=random.randint(0, days))

# Generate a completion time after the given creation date
def completion_time(created_at):
    return created_at + timedelta(days=random.randint(1, 14))
