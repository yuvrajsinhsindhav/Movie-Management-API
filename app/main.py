from fastapi import FastAPI
from .database import Base, engine
from .handlers.movies import router as movies_router
from . import models

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="🎬 Movie Management API",
    version="1.0.0",
    description="A basic CRUD API for movies with layered architecture (Handler/Service/DAO)."
)

# Register routers
app.include_router(movies_router)
