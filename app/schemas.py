from pydantic import BaseModel, Field, field_validator , ConfigDict
from typing import Optional

class MovieBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="Movie title (required)")
    director: Optional[str] = Field(default=None, max_length=200)
    releaseYear: Optional[int] = Field(
        default=None,
        ge=1888,  # first known films era
        le=2100,
        description="Year the movie was released"
    )
    genre: Optional[str] = Field(default=None, max_length=100)
    rating: Optional[float] = Field(
        default=None,
        ge=1.0,
        le=10.0,
        description="Rating between 1 and 10"
    )

    @field_validator("title")
    @classmethod
    def strip_title(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("title cannot be empty")
        return v

class MovieCreate(MovieBase):
    pass

class MovieUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    director: Optional[str] = Field(default=None, max_length=200)
    releaseYear: Optional[int] = Field(default=None, ge=1888, le=2100)
    genre: Optional[str] = Field(default=None, max_length=100)
    rating: Optional[float] = Field(default=None, ge=1.0, le=10.0)

    @field_validator("title")
    @classmethod
    def strip_title_update(cls, v: Optional[str]) -> Optional[str]:
        return v.strip() if isinstance(v, str) else v

class MovieOut(MovieBase):
    id: int

    class Config:
        model_config = ConfigDict(from_attributes=True)

        #from_attributes = True  # (pydantic v2 equivalent of orm_mode)
