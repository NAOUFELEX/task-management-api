from pydantic import BaseModel, Field, model_validator
from typing import Optional
from enum import Enum
from datetime import datetime


# Enum defined here to avoid circular import issues
class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"
    cancelled = "cancelled"


# Shared base properties
class TaskBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: TaskStatus = TaskStatus.pending
    cancelled_reason: Optional[str] = Field(None, max_length=500)


# Used when creating a task
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)


# Used when updating a task
class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: Optional[TaskStatus] = None
    cancelled_reason: Optional[str] = Field(None, max_length=500)

    @model_validator(mode="after")
    def validate_cancel_logic(self):
        # If status is being updated to cancelled,
        # cancelled_reason must be provided
        if self.status == TaskStatus.cancelled and not self.cancelled_reason:
            raise ValueError(
                "cancelled_reason is required when status is 'cancelled'"
            )
        return self


# Used when returning data to client
class TaskResponse(TaskBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True