from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

from .database import SessionLocal, engine
from . import models, schemas, crud

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management API")


# Dependency injection for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create Task
@app.post(
    "/tasks",
    response_model=schemas.TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db),
):
    return crud.create_task(db, task)


# Get All Tasks (with pagination + filtering)
@app.get(
    "/tasks",
    response_model=List[schemas.TaskResponse],
)
def read_tasks(
    skip: int = 0,
    limit: int = 10,
    status: Optional[schemas.TaskStatus] = None,
    db: Session = Depends(get_db),
):
    return crud.get_tasks(db, skip=skip, limit=limit, status=status)


# Get Single Task
@app.get(
    "/tasks/{task_id}",
    response_model=schemas.TaskResponse,
)
def read_task(
    task_id: int,
    db: Session = Depends(get_db),
):
    task = crud.get_task(db, task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    return task


# Update Task
@app.put(
    "/tasks/{task_id}",
    response_model=schemas.TaskResponse,
)
def update_task(
    task_id: int,
    task_update: schemas.TaskUpdate,
    db: Session = Depends(get_db),
):
    task = crud.update_task(db, task_id, task_update)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    return task


# Delete Task
@app.delete(
    "/tasks/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
):
    task = crud.delete_task(db, task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    return None