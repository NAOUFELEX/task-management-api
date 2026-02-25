from pydantic import BaseModel, Field
from pydantic import model_validator
from typing import Optional
from enum import Enum
from datetime import datetime
from .models import TaskStatus



class TaskBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: TaskStatus = TaskStatus.pending
    cancelled_reason: Optional[str] = Field(None, max_length=500)



class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)



class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: Optional[TaskStatus]
    cancelled_reason: Optional[str] = Field(None, max_length=500)

    @model_validator(mode="after")
    def check_cancel_reason(self):
        if self.status == TaskStatus.cancelled and not self.cancelled_reason:
            raise ValueError("cancelled_reason is required when status is cancelled")
        return self



class TaskResponse(TaskBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
   
    class Config:
        from_attributes = True