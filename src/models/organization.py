from dataclasses import dataclass
from datetime import datetime

@dataclass
class Organization:
    id: str
    name: str
    created_at: datetime
