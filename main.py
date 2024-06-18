from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from config.database import  engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router
from schemas.movieDto import get_movies

app = FastAPI()
app.title = "MI APLICACION CON FAST API"
app.version = "0.0.1"
app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)


Base.metadata.create_all(bind = engine)

# data
movies = get_movies()


# endPoints
@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1> hello world</h1>')



