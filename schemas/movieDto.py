from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id : Optional[int] = None
    title: str = Field(min_length=5, max_length= 15)
    overview : str = Field(min_length=15, max_length= 50)
    year: int = Field(le = 2022)
    rating: float = Field(ge = 0.1, le = 10)
    category: str = Field(min_length=5, max_length= 15)
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi pelicula",
                "overview": "Descripcion de mi pelicula",
                "year": "2009",
                "rating": 9.8,
                "category": "Acción"
            }
        }
  
def get_movies():
    return [
                {
                    "id": 1,
                    "title": "Avatar",
                    "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
                    "year": "2009",
                    "rating": 7.8,
                    "category": "Acción"
                },
                    {
                    "id": 2,
                    "title": "Avatar",
                    "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
                    "year": "2009",
                    "rating": 7.8,
                    "category": "Acción"
                }
            ]  