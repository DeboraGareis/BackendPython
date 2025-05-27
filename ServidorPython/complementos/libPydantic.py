from typing import Optional
from pydantic import BaseModel, ValidationError, validator

#los atributos seran obligatorios, no podran omitirse en la creacion
#queremos atributo no requerido -> usar Optional 
class User(BaseModel):
    username: str
    password: str
    email: str
    age: Optional[int] = None

    @validator('username')
    def username_validation_lenght(cls, username):
        if len(username) < 3:
            raise ValueError('La longitud minima es de 3 caracteres')
        if len(username) > 30:
            raise ValueError('La longitud maxima es de 30 caracteres')
        return username

try:
    user1= User(
        username= "us",
        password= "123224",
        email= "user@gmail.com",
        #age= 12
    )
    print(user1) 
except ValidationError as e:
    print(e.json())