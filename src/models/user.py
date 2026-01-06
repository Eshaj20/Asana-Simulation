from dataclasses import dataclass
from datetime import datetime

# Data class representing a user record
@dataclass
class User:
    id: str
    organization_id: str
    full_name: str
    email: str
    role: str
    created_at: datetime
