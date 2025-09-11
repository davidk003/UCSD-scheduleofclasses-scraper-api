from dataclasses import dataclass
from typing import TypeAlias

DeptCode: TypeAlias = str
DeptName: TypeAlias = str

SubjectCode: TypeAlias = str
SubjectName: TypeAlias = str

@dataclass
class ClassSchedulePage:
    """Container for a page of schedule results."""
    courses: list[dict]
    current_page: int
    max_page: int
    term: str
    departments: list[str]
