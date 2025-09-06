from typing import List, Optional
from sqlalchemy.orm import Session
from ..models import Movie

class MoviesDAO:
    @staticmethod
    def list_all(db: Session) -> List[Movie]:
        return db.query(Movie).order_by(Movie.id.asc()).all()

    @staticmethod
    def find_by_id(db: Session, movie_id: int) -> Optional[Movie]:
        return db.query(Movie).filter(Movie.id == movie_id).first()

    @staticmethod
    def find_by_title(db: Session, title: str) -> Optional[Movie]:
        return db.query(Movie).filter(Movie.title == title).first()

    @staticmethod
    def create(db: Session, data: dict) -> Movie:
        obj = Movie(**data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def update(db: Session, movie: Movie, data: dict) -> Movie:
        for k, v in data.items():
            setattr(movie, k, v)
        db.commit()
        db.refresh(movie)
        return movie

    @staticmethod
    def delete(db: Session, movie: Movie) -> None:
        db.delete(movie)
        db.commit()
