from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Movie(Base):
    __tablename__ = "movies"

    # We keep the Python attribute names matching the schema (camelCase)
    # but store columns in snake_case where desired:
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    director = Column(String, nullable=True)
    releaseYear = Column("release_year", Integer, nullable=True)  # attr releaseYear, column release_year
    genre = Column(String, nullable=True)
    rating = Column(Float, nullable=True)  # 1.0 to 10.0 (validated in schema/service)
