from dataclasses import dataclass
from datetime import datetime, date
from typing import Optional

# Data class representing a Task
@dataclass
class Task:
    id: str
    project_id: str
    section_id: str
    assignee_id: Optional[str]
    parent_task_id: Optional[str]
    name: str
    description: str
    due_date: Optional[date]
    completed: bool
    created_at: datetime
    completed_at: Optional[datetime]
