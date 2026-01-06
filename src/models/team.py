from dataclasses import dataclass
from datetime import datetime

# Data class representing a Team
@dataclass
class Team:
    id: str
    organization_id: str
    name: str
    created_at: datetime

