
from fastapi import FastAPI
import models
from database import engine, sessionLocal
from routers import auth, todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# app.include_router(auth.router, tags=["auuth"],)
app.include_router(todos.router, tags=["todos"])


