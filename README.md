# ASANA_SIMULATION

## Overview

`ASANA_SIMULATION` is a Python project that simulates an Asana-like project management system.
It generates realistic data for organizations, teams, projects, sections, tasks, tags, comments, attachments, and users, and stores it in a **SQLite database**.

---

## Features

* Modular design with separation of concerns
* Populates a SQLite database (`asana_simulation.sqlite`) with realistic data
* Supports configurable parameters: number of users, projects, tasks, date ranges
* Error handling and logging included
* Optional AI prompt generation (LLM)

---

## Folder Structure

```
ASANA_SIMULATION/
├── output/                   # Generated SQLite DB
├── prompts/                  # Text prompts for tasks/comments
├── src/                      # Source code
│   ├── generators/           # Data generators
│   ├── models/               # DB models
│   ├── scrapers/             # Data scrapers
│   ├── utils/                # Helper functions (config, logger, db)
│   └── main.py               # Entry point
├── .env                      # Environment variables
├── README.md                 # Documentation
├── requirements.txt          # Python dependencies
└── schema.sql                # Database schema
```

---

## Setup Instructions

1. **Clone the repository**

```bash
git clone <repo_url>
cd ASANA_SIMULATION
```

2. **Create virtual environment (optional)**

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure environment variables**

```bash
.env.example
```

Edit `.env` if using optional LLM/API keys.

5. **Run the simulation**

```bash
python src/main.py
```

This will generate `output/asana_simulation.sqlite` with sample data.

---

## Configuration

All configurable options are in `src/utils/config.py`:

* `NUM_USERS`, `NUM_TEAMS`, `NUM_PROJECTS`, `NUM_TASKS`
* Date ranges for tasks and comments

You can adjust these values without changing the main code.

---

## Database Overview

* **DB File:** `output/asana_simulation.sqlite`
* **Tables:** `users`, `teams`, `projects`, `sections`, `tasks`, `tags`, `task_tags`, `comments`, `attachments`, `custom_fields_definitions`, `custom_field_values`, `organizations`, `team_memberships`

**Sample Queries:**

```sql
-- First 10 tasks
SELECT id, name, section_id, assignee_id, completed
FROM tasks
LIMIT 10;

-- Comments per task
SELECT task_id, COUNT(*) AS comment_count
FROM comments
GROUP BY task_id
LIMIT 10;
```

---

## Logging & Error Handling

* Logs handled via `src/utils/logger.py`
* Database and generator operations use **try/except** for safety

---

## Notes

* LLM integration is **optional** 
* Some tasks may be unassigned; you can auto-assign them if needed
* Database schema is in `schema.sql` for reference

---

## Dependencies

* Python 3.10+
* `sqlite3` (built-in)
* Other dependencies listed in `requirements.txt`

---

## Verification

1. Open SQLite DB:

```bash
sqlite3 output/asana_simulation.sqlite
```

2. Run queries to verify tasks, comments, and users are populated


