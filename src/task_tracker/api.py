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

class TaskCreate(BaseModel):
  title : str

class TaskUpdate(BaseModel):
    title: str

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

@app.get("/tasks/{task_id}", response_model=Task)
def get_task_by_id(task_id:int):
   exiting_task = get_task(task_id)
   if exiting_task :
      result = {
         'id' : exiting_task[0],
         'title' : exiting_task[1]
      }
      return result
   else:
      raise HTTPException(status_code=404, detail="Taks not found")

@app.post("/tasks", status_code=201)
def create_task(task:TaskCreate):
    add_task(task.title)
    return {
       "message" : "Task Created successfully"
    }

@app.put("/tasks/{task_id}" , status_code=200)
def update_task_by_id(task_id:int, task:TaskUpdate):
   exiting_task = get_task(task_id)
   if exiting_task :
      update_task(task_id,task.title)
      return {"message": "Task updated succesfully"}
   else:
      raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}",status_code=200)
def delete_task_by_id(task_id:int):
   existing_task = get_task(task_id)
   if not existing_task:
      raise HTTPException(
         status_code=404,
         detail="Task not found")
   delete_task(task_id)
   return {
       "message" : "Task deleted successfully"
    }