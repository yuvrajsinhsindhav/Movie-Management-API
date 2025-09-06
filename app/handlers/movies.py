from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..schemas import MovieCreate, MovieUpdate, MovieOut
from ..services.movies_service import MoviesService

router = APIRouter(prefix="/movies", tags=["Movies"])

service = MoviesService()

@router.get("", response_model=List[MovieOut], summary="List all movies")
def list_movies(db: Session = Depends(get_db)):
    return service.list_movies(db)

@router.get("/{movie_id}", response_model=MovieOut, summary="Get movie by ID")
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    return service.get_movie(db, movie_id)

@router.post("", response_model=MovieOut, status_code=status.HTTP_201_CREATED, summary="Create a new movie")
def create_movie(payload: MovieCreate, db: Session = Depends(get_db)):
    # If you want to log/print the SQL queries, enable SQLAlchemy echo=True in engine OR print payload here
    # print("Incoming payload:", payload.model_dump())
    return service.create_movie(db, payload)

@router.put("/{movie_id}", response_model=MovieOut, summary="Update existing movie")
def update_movie(movie_id: int, payload: MovieUpdate, db: Session = Depends(get_db)):
    return service.update_movie(db, movie_id, payload)

@router.delete("/{movie_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete movie by ID")
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    service.delete_movie(db, movie_id)
    return None
