from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
import json


#history = []
#with open('history.json') as f:
#    data = json.load(f)
#    history.extend(data)
#f.close()
#print(str(history))\

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

class User(BaseModel):
    id: UUID = None
    name: str
    email: Optional[str]
    history: Optional[List]

class Task(BaseModel):
    id: Optional[UUID] = None
    title: str
    description: Optional[str] = None
    completed: bool = False

tasks = []

@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    task.id = uuid4()
    tasks.append(task)
    return task
    
@app.get("/tasks/", response_model=List[Task])
def read_tasks():
    return tasks



@app.get("/")
async def root():
    return {"message": "Hello World 333 !!!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)