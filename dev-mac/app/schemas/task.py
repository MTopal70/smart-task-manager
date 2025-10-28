from pydantic import BaseModel
from typing import Optional
from datetime import datetime
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    completed: Optional[bool] = False
class TaskCreate(TaskBase):
    pass
class TaskUpdate(TaskBase):
    pass
class TaskOut(TaskBase):
    id: int
    created_at: datetime
    owner_id: int
    project_id: Optional[int]
    class Config:
        orm_mode = True