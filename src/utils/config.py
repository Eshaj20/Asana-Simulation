import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Path for the SQLite database file
DB_PATH = os.getenv("DB_PATH", "output/asana_simulation.sqlite")

# Number of organizations to generate
ORG_COUNT = int(os.getenv("ORG_COUNT", 1))

# Total number of users to create
USER_COUNT = int(os.getenv("USER_COUNT", 20))

# Total number of tasks to generate
TASK_COUNT = int(os.getenv("TASK_COUNT", 100))
