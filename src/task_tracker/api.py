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

class Task(BaseModel):
  id : int
  title : str

@app.get("/tasks", response_model=list[Task])
def get_task_list():
    tasks = get_all_tasks()
    result = []
    for task in tasks:
        result.append(
           {
            "id" : task[0],
            "title" : task[1]
           }
        )
    return result