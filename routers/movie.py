from fastapi import APIRouter, Path, Query,  Depends
from fastapi.responses import  JSONResponse
from typing import List
from fastapi.encoders import jsonable_encoder

from config.database import Session
from middlewares.jwt_bearer import JWTBearer
from models.movie import Movie as MovieModel
from schemas.movieDto import Movie
from services.movie import MovieService

movie_router = APIRouter()


@movie_router.get('/movies', tags=['movies'], response_model= List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    # db = Session();
    # result = MovieService(db).get_movies()
    result = MovieService().get_movies()
    return JSONResponse(status_code=200, content= jsonable_encoder(result))


@movie_router.get('/movies/{id}', tags=['movies'], response_model= Movie, status_code=200)
def get_movie(id: int = Path(ge =1, le=2000)) -> Movie:
    # return next( (movie for movie in movies if movie["id"] == id ), [])
    # for item in movies:
    #     if item["id"] == id:
    #         return JSONResponse(status_code=200,content= item)
    # return JSONResponse(status_code=404, content= [])
    
    # db = Session()
    # result= MovieService(db).get_movie(id)
    result= MovieService().get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content= {"message": "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@movie_router.get('/movies/', tags=['movies'], response_model= List[Movie], status_code=200)
def get_movies_by_category(category: str = Query(min_length= 5, max_length= 15))-> List[Movie]:
    # filters = [movie for movie in movies if movie["category"] == category]
    # return JSONResponse(status_code=200, content= filters)
    # db= Session()
    # result= MovieService(db).get_movies_by_category(category)
    result= MovieService().get_movies_by_category(category)
    print(result)
    if not result:
        return JSONResponse(status_code=404, content= {"message": "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# @app.post('/movies', tags=['movies'])
# def create_movies(id: int  = Body(), title: str = Body(), overview: str = Body(), year: int  = Body(), rating: float = Body(), category: str = Body()):
#     movies.append({
#         "id": id,
#         "title": title,
#         "overview": overview,
#         "year": year,
#         "rating": rating,
#         "category": category
#         })
#     return movies

@movie_router.post('/movies', tags=['movies'], response_model= dict, status_code=201)
def create_movie(movie: Movie)->dict:
    # db = Session()
    # new_movie = MovieModel(**movie.dict())
    # db.add(new_movie)
    # db.commit()
    # movies.append(movie.model_dump())
    MovieService().create_movie(movie)
    return JSONResponse(status_code= 201, content = {"message": "Se regisro la pelicula"})

@movie_router.put('/movies/{id}', tags=['movies'], response_model= dict, status_code=200)
def update_movie(id: int, movie: Movie)->dict:
    # for item in movies:
    #     if item["id"] == id:
    #         item["title"] = movie.title
    #         item["overview"] = movie.overview
    #         item["year"] = movie.year
    #         item["rating"] = movie.rating
    #         item["category"] = movie.category
    #         return JSONResponse(status_code=200, content = {"message": "Se modifico la pelicula"})
    # return JSONResponse(status_code=200, content = {"message": "No se modifico la pelicula"})
    # db = Session()
    # result =db.query(MovieModel).filter(MovieModel.id == id).first()
    # if not result:
    #     return JSONResponse(status_code=404, content= {"message": "No encontrado"})
    # result.title = movie.title
    # result.overview = movie.overview
    # result.year = movie.year
    # result.rating = movie.rating
    # result.category = movie.category
    # db.commit()  
    result =MovieService().get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content= {"message": "No encontrado"})
    MovieService().update_movie(id, movie)
    return JSONResponse(status_code=200, content = {"message": "Se modifico la pelicula "})
 
@movie_router.delete('/movies/{id}', tags=['movies'], response_model= dict, status_code=200)
def delete_movie(id: int)->dict:
    # 1
    # movie = [movie for movie in movies if movie["id"] == id]
    # movies.remove(movie[0])
    
    # 2
    # movies.remove([movie for movie in movies if movie["id"] == id][0])
    
    # 3
    # for item in movies:
    #     if item['id'] == id:
    #         movies.remove(item)
    # db = Session()
    result = MovieService().get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content= {"message": "No encontrado"})
    MovieService().delete_movie(id)
    return JSONResponse(status_code=200, content = {"message": "Se elimino la pelicula"})