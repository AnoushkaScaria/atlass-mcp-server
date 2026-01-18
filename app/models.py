from pydantic import BaseModel
from typing import List, Optional


class JiraSubtask(BaseModel):
    key: str
    summary: str
    status: str


class JiraTicket(BaseModel):
    key: str
    summary: str
    description: Optional[str]
    status: str
    assignee: Optional[str]
    subtasks: List[JiraSubtask]
