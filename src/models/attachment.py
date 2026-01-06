from dataclasses import dataclass
from datetime import datetime

@dataclass
class Attachment:
    id: str
    task_id: str
    uploaded_by: str
    file_name: str
    file_url: str
    file_type: str
    file_size: int
    created_at: datetime
