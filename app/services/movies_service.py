from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..schemas import MovieCreate, MovieUpdate
from ..models import Movie
from ..dao.movies_dao import MoviesDAO

class MoviesService:
    def __init__(self, dao: MoviesDAO = MoviesDAO()):
        self.dao = dao

    def list_movies(self, db: Session) -> List[Movie]:
        return self.dao.list_all(db)

    def get_movie(self, db: Session, movie_id: int) -> Movie:
        movie = self.dao.find_by_id(db, movie_id)
        if not movie:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
        return movie

    def create_movie(self, db: Session, payload: MovieCreate) -> Movie:
        # Example business rule: unique title (optional but useful)
        existing = self.dao.find_by_title(db, payload.title)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="A movie with this title already exists"
            )
        return self.dao.create(db, payload.model_dump())

    def update_movie(self, db: Session, movie_id: int, payload: MovieUpdate) -> Movie:
        movie = self.dao.find_by_id(db, movie_id)
        if not movie:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")

        data = payload.model_dump(exclude_unset=True)

        # If title is being changed, enforce uniqueness
        new_title = data.get("title")
        if new_title:
            other = self.dao.find_by_title(db, new_title)
            if other and other.id != movie.id:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Another movie with this title already exists"
                )

        return self.dao.update(db, movie, data)

    def delete_movie(self, db: Session, movie_id: int) -> None:
        movie = self.dao.find_by_id(db, movie_id)
        if not movie:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
        self.dao.delete(db, movie)
