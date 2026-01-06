from dataclasses import dataclass

@dataclass
class Section:
    id: str
    project_id: str
    name: str
    position: int
