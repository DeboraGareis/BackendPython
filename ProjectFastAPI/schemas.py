from typing import Any, ClassVar
from pydantic import BaseModel, validator
from pydantic.v1.utils import GetterDict
from peewee import ModelSelect

#funciona unicamente trabajando con ORM peewee
class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, ModelSelect):
            return list(res)
        return res

#convertir model en ResponseModel, todas las rtas heredan de esta clase
class ResponseModel(BaseModel):
    model_config = {
        "from_attributes": True
    } 
    getter_dict: ClassVar = PeeweeGetterDict

#### USUARIO ####
class UserRequestModel(BaseModel):
    username: str
    password: str

    @validator('username')
    def username_validator(cls, username):
        if len(username) < 3 or len(username) > 50:
            raise ValueError('la longitud debe ser entre 3 y 50')
        return username

class UserResponseModel(ResponseModel):
    id: int
    username: str

#### MOVIE ####
class MovieRequestModel(BaseModel):
    title: str

class MovieResponseModel(ResponseModel):
    id: int
    title: str 

#### REVIEW ####

class ReviewValidator():
    #todas las validaciones para las reseñas
    @validator('score')
    def score_validator(cls, score):
        if score > 5 or score < 1:
            raise ValueError('la puntuacion debe ser entre 1 y 5')
        return score

class ReviewRequestModel(BaseModel, ReviewValidator):
    user_id: int
    #si solo queremos dar el id de la pelicula:
    #movie_id: int
    #si queremos dar un objeto movie para relacionar objetos:
    movie: MovieResponseModel
    review: str
    score: int
   
    
class ReviewResponseModel(ResponseModel):
    id: int
    movie_id: int
    review: str
    score: int

class ReviewRequestPutModel(BaseModel, ReviewValidator):
    review: str
    score: int







