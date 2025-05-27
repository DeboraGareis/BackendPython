from datetime import datetime
import hashlib
from peewee import *

database = MySQLDatabase('fastapi_project',
                         user='root',
                         password='',
                         host='localhost',
                         port=3306)

class User(Model):
    username = CharField(max_length=50, unique= True)
    password = CharField(max_length=50)
    created_at = DateTimeField(default=datetime.now)

    #sobreescribo str: cada vez que se imprima un objeto user retorno username
    def __str__(self):
        return self.username
    
    #indicar BD y nombre que damos a la tabla
    class Meta:
        database = database
        table_name = 'users'

    #metodo para hashear contraseña
    @classmethod
    def create_password(cls,password):
        h= hashlib.md5()
        h.update(password.encode('utf-8'))
        return h.hexdigest()

class Movie(Model):
    title = CharField(max_length=50)
    created_at = DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
    
    class Meta:
        database = database
        table_name = 'movies'

#relacionar una pelicula - reseña - usuario
class UserReview(Model):
    #usando el atributo reviews un objeto de tipo user o movie puede acceder a sus reseñas
    user = ForeignKeyField(User, backref='reviews')
    movie = ForeignKeyField(Movie, backref='reviews')
    review = TextField()
    score = IntegerField()
    created_at = DateTimeField(default = datetime.now)

    def __str__(self):
        return f'{self.user.username}-{self.user.title}'
    
    class Meta:
        database = database
        table_name = 'user_reviews'

