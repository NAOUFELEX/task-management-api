from sqlalchemy.orm import Session
from typing import Optional, List

from . import models, schemas


# Create a new task
def create_task(db: Session, task_data: schemas.TaskCreate) -> models.Task:
    task = models.Task(
        title=task_data.title,
        description=task_data.description,
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


# Get all tasks (with pagination and optional status filtering)
def get_tasks(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    status: Optional[schemas.TaskStatus] = None,
) -> List[models.Task]:

    query = db.query(models.Task)

    if status is not None:
        query = query.filter(models.Task.status == status)

    return query.offset(skip).limit(limit).all()


# Get single task by ID
def get_task(db: Session, task_id: int) -> Optional[models.Task]:
    return db.query(models.Task).filter(models.Task.id == task_id).first()


# Update task
def update_task(
    db: Session,
    task_id: int,
    task_update: schemas.TaskUpdate,
) -> Optional[models.Task]:

    task = get_task(db, task_id)

    if task is None:
        return None

    update_data = task_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)

    return task


# Delete task
def delete_task(db: Session, task_id: int) -> Optional[models.Task]:

    task = get_task(db, task_id)

    if task is None:
        return None

    db.delete(task)
    db.commit()

    return task