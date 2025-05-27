from urllib import request

#direccion a la que realizo peticion
URL = "http://localhost:8000/"

#realizamos peticion
response = request.urlopen(URL)
print(response)

#acceder a los atributos de la rta
print(response.__dict__)


print(response.read())