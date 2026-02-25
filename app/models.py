from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.sql import func
from .database import Base
import enum


class TaskStatus(enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"
    cancelled = "cancelled"


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)

    status = Column(
        Enum(TaskStatus),
        nullable=False,
        default=TaskStatus.pending
    )
    cancelled_reason = Column(String(500), nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    updated_at = Column(
        DateTime(timezone=True),
        onupdate=func.now(),
        nullable=True
    )