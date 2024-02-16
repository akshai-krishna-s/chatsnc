__import__("pysqlite3")
import sys

sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")
from fastapi import FastAPI
from .routers import user, auth, chatsnc
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .config import settings


# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://chatsnc.vercel.app",
    "https://chatsnc.vercel.app",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(chatsnc.router)


@app.get("/")
def root():
    return {"message": "Hello World"}
