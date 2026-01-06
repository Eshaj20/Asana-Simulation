from dataclasses import dataclass
from datetime import datetime

@dataclass
class Comment:
    id: str
    task_id: str
    author_id: str
    body: str
    created_at: datetime
