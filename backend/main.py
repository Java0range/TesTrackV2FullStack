from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Users import users
from TaskBase import task_base
from Tests import tests
from Results import results
import uvicorn

app = FastAPI()


app.include_router(users)
app.include_router(task_base)
app.include_router(tests)
app.include_router(results)


origins = ["http://localhost:5173", "http://82.148.30.194:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)