from dataclasses import dataclass

@dataclass
class CustomFieldDefinition:
    id: str
    project_id: str
    name: str
    field_type: str
