from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
from task_tracker.database import (
    add_task,
    update_task,
    get_task,
    get_all_tasks,
    delete_task
)

app = FastAPI()

class TaskCreate(BaseModel):
    title : str

class TaskUpdate(BaseModel):
    task_id : int
    title : str

class TaskDelete(BaseModel):
    task_id : int

class TaskGetAll(BaseModel):
    task_id:int
    title:str

class TaskGet(BaseModel):
    task_id:int


@app.get("/")
def root():
    return {"message": "Task Tracker is live"}

@app.get("/tasks",status_code=200)
def list_tasks(task:TaskGetAll):
    tasks = get_all_tasks()
    return tasks

@app.post("/tasks", status_code=200)
def create_task(task:TaskCreate):
    add_task(task.title)
    return  {"message" : "Task created successfully"}

@app.get("/tasks/{task_id}" ,status_code=200)
def get_task_by_id(task:TaskGet):
    task = get_task(task.task_id)
    if task:
        return task
    else:
        raise HTTPException(status_code=404, detail="Invalid task id")

@app.put("/tasks/{task_id}", status_code=201)
def update_task_by_id(task:TaskUpdate):
    task = get_task(task.task_id)
    if task:
        update_task(task.task_id, task.title)
        return {"message" : "Task updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task_by_id(task:TaskDelete):
    task = get_task(task.task_id)
    if task:
        delete_task(task.task_id)
        return {"message" : "Task deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Task not found")


