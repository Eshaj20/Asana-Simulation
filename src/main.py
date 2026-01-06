import os
from utils.db import get_connection
from utils.logger import logger
from utils.config import DB_PATH, ORG_COUNT, USER_COUNT, TASK_COUNT

# Generators
from generators.organizations import generate_organizations
from generators.teams import generate_teams
from generators.users import generate_users
from generators.team_memberships import generate_team_memberships
from generators.projects import generate_projects
from generators.sections import generate_sections
from generators.tasks import generate_tasks
from generators.comments import generate_comments
from generators.tags import generate_tags
from generators.task_tags import generate_task_tags
from generators.custom_fields_defintions import generate_custom_fields_defintions
from generators.custom_field_values import generate_custom_field_values
from generators.attachments import generate_attachments

# Path to the SQL schema file
SCHEMA_PATH = "schema.sql"


def initialize_database(conn):
    """Initialize database tables using the schema file."""
    logger.info("Initializing database schema...")
    if not os.path.exists(SCHEMA_PATH):
        raise FileNotFoundError(f"Schema file not found at {SCHEMA_PATH}")
    with open(SCHEMA_PATH, "r") as f:
        conn.executescript(f.read())
    conn.commit()


def main():
    # Ensure output directory exists
    os.makedirs("output", exist_ok=True)

    # Connect to the database
    logger.info("Connecting to SQLite database...")
    conn = get_connection(DB_PATH)

    # Initialize database schema and generate data
    try:
        initialize_database(conn)
        cursor = conn.cursor()

        # 1. Organizations
        logger.info("Generating organizations...")
        org_ids = generate_organizations(cursor, count=ORG_COUNT)

        # 2. Teams
        logger.info("Generating teams...")
        team_ids = []
        for org_id in org_ids:
            team_ids.extend(generate_teams(cursor, org_id))

        # 3. Users
        logger.info("Generating users...")
        user_ids = []
        for org_id in org_ids:
            user_ids.extend(generate_users(cursor, org_id, USER_COUNT))

        # 4. Team memberships
        logger.info("Assigning users to teams...")
        generate_team_memberships(cursor, team_ids, user_ids)

        # 5. Projects
        logger.info("Generating projects...")
        project_ids = generate_projects(cursor, team_ids)

        # 6. Sections
        logger.info("Generating sections...")
        section_map = generate_sections(cursor, project_ids)

        # 7. Tasks
        logger.info("Generating tasks...")
        generate_tasks(cursor, project_ids, section_map, user_ids, TASK_COUNT)

        # Fetch task IDs for dependent tables
        cursor.execute("SELECT id FROM tasks")
        task_ids = [row[0] for row in cursor.fetchall()]

        # 8. Comments
        logger.info("Generating comments for tasks...")
        generate_comments(cursor, task_ids, user_ids)

        # 9. Tags
        logger.info("Generating tags...")
        tag_ids = generate_tags(cursor)

        # 10. Task-Tag mapping
        logger.info("Assigning tags to tasks...")
        generate_task_tags(cursor, task_ids, tag_ids)

        # 11. Custom fields
        logger.info("Generating custom fields...")
        field_ids = generate_custom_fields_defintions(cursor, project_ids)

        # 12. Custom field values
        logger.info("Assigning custom field values to tasks...")
        generate_custom_field_values(cursor, task_ids, field_ids)

        # 13. Attachments
        logger.info("Generating attachments...")
        generate_attachments(cursor, task_ids, user_ids)

        # Commit all changes
        conn.commit()
        # Final log summary
        logger.info("Asana simulation database successfully generated 🎉")
        logger.info(f"Database location: {DB_PATH}")
        logger.info(
            f"Summary: {len(org_ids)} orgs, {len(team_ids)} teams, "
            f"{len(user_ids)} users, {TASK_COUNT} tasks"
        )

    # Handle exceptions
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        conn.rollback()
        
    # Ensure the database connection is closed
    finally:
        conn.close()
        logger.info("Database connection closed.")


if __name__ == "__main__":
    main()
