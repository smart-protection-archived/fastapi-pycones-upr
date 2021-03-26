# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import uvicorn
from fastapi import FastAPI

from sales.infrastructure.routes.fastAPI.routes import router

app = FastAPI()

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app)
