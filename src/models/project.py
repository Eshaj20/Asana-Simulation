from dataclasses import dataclass
from datetime import datetime

@dataclass
class Project:
    id: str
    team_id: str
    name: str
    project_type: str
    created_at: datetime
