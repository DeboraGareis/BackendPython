from typing import List
from fastapi import Cookie, FastAPI, HTTPException, Response
from fastapi.security import HTTPBasicCredentials
from database import Movie, User, UserReview, database as connection
from schemas import MovieRequestModel, MovieResponseModel, ReviewRequestModel, ReviewRequestPutModel, ReviewResponseModel, UserRequestModel, UserResponseModel
app = FastAPI(title='Proyecto para reseñar peliculas',
              description='este proyecto sera capaz de....',
              version='1'
              )

#EVENTOS
@app.on_event('startup')
def startup():
    if connection.is_closed():
        #antes que inicie la conexion realizamos conexion
        connection.connect()
        print('conecting...')
    connection.create_tables([User, Movie, UserReview])

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        # cerramos conexion
        connection.close()
        print('desconectando... ')

#primera ruta
#estructura: @aplicacion.metodoHTTP
@app.get('/')
async def index():
    return "mensaje enviado desde el servidor en FastAPI"

@app.get('/about/')
async def about():
    return "about"

## VA EN USERS
@app.post('/users/', response_model=UserResponseModel)
async def create_user(user: UserRequestModel):
    
    #validar que el usuario enviado no exista
    if User.select().where(User.username == user.username).exists():
        return HTTPException(409,"ese username ya se ha usado")
    #llamamos al metodo de clase para hashear contraseña
    hash_password = User.create_password(user.password)
    
    new_user = User.create(
        username = user.username,
        password = hash_password
    ) 
    return new_user

@app.post("/login", response_model=UserResponseModel)
async def login(credentials: HTTPBasicCredentials, response:Response):
    user = User.select().where(User.username == credentials.username).first()
    if user is None:
        return HTTPException(404,"user not found")
   
    if user.password != User.create_password(credentials.password):
        return HTTPException(404,"Passeord error")
    response.set_cookie(key="user_id",value=user.id)
    return user

@app.get("/reviews_por_user", response_model=List[ReviewResponseModel])
async def get_reviews(user_id: int = Cookie(None)):
    user = User.select().where(User.id == user_id).first()
    if user is None:
        raise HTTPException(404,"user not found")
    return [user_review for user_review in user.reviews]





## VA EN MOVIES
@app.post('/movies', response_model=MovieResponseModel)
async def create_movie(movie: MovieRequestModel):
    new_movie= Movie.create(
        title = movie.title
    )
    return new_movie

## VA EN REVIEWS
@app.post('/reviews', response_model=ReviewResponseModel)
async def create_review(user_review: ReviewRequestModel):
    #comprobar que exista la pelicula y el usuario
    if User.select().where(User.id == user_review.user_id).first() is None:
        raise HTTPException(status_code=404, detail="user not found")
    if Movie.select().where(Movie.id == user_review.movie.id).first() is None:
        raise HTTPException(status_code=404, detail="movie not found")

    new_user_review= UserReview.create(
        user_id = user_review.user_id,
        movie_id = user_review.movie.id,
        review =user_review.review,
        score = user_review.score
    )
    return new_user_review

@app.get('/reviews', response_model=List[ReviewRequestModel])
async def get_reviews(page : int = 1, limit : int = 10):
    reviews = UserReview.select().paginate(page, limit)
    return [user_review for user_review in reviews]

@app.get('/reviews/{review_id}', response_model=ReviewResponseModel)
async def get_review(review_id:int):
    user_review = UserReview.select().where(UserReview.id == review_id).first()
    if user_review is None:
        raise HTTPException(status_code=404, detail="review not found")
    return user_review


@app.put('/reviews/{review_id}', response_model=ReviewResponseModel)
async def update_review(review_id:int, review_request: ReviewRequestPutModel):
    user_review = UserReview.select().where(UserReview.id == review_id).first()
    
    if user_review is None:
        raise HTTPException(status_code=404, detail='review not found')
    
    user_review.review = review_request.review
    user_review.score = review_request.score
    user_review.save()

    return user_review



@app.delete('/reviews/{review_id}')
async def delete_review(review_id: int):
    user_review= UserReview.select().where(UserReview.id == review_id).first()
    
    if user_review is None:
        raise HTTPException(status_code=404, detail='review not found')    
   
    user_review.delete_instance()

    return user_review