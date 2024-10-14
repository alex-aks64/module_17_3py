from fastapi import FastAPI
from app.models import user
from app.models import task

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}



app.include_router(user.router)
app.include_router(task.router)






