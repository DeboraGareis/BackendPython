#Indicar explícitamente el tipo de dato que se podrá almacenar

from typing import Dict, List, Tuple, Union

### variables ###
a: str = "variable a"
b: int = 30
c: float = 3.14
d: bool = True
print (" a:", a , " b:", b , " c:", c , " d:", d)

### funciones ###
def suma(n1: int, n2:int)-> int:
    return n1+n2

valor1: int = 10
valor2: int = 20
valor3: int #no se define valor inicial pero se la usara posteriormente

resultado: int = suma(valor1, valor2)
print("resultado funcion: ",resultado)

### clases ###
class User():
    def __init__(self, username:str, password:str) ->None:
        self.username = username
        self.password = password
    
    def saluda(self) -> str:
        return f'Hola {self.username}'
    
usuario = User("debo", "1234")
print(usuario.saluda())

### Colecciones ### -> list
calificaciones: List[int] = [10,9,6,4,8,8,9,9]
def promedio(calificaciones: List[int]) ->float:
    return sum(calificaciones)/len(calificaciones)
print(promedio(calificaciones))  

### Colecciones ### -> tuple
configuracion2: Tuple[str] = ('localhost', '3306', 'root')
print(configuracion2)

#definir explicitamente el tipo de cada elemento de la tupla
configuracion3: Tuple[Union[str,str,bool,int]] = ('root','localhost',True,34)
print(configuracion3)

### Colecciones ### -> diccionarios
usuarios: Dict[str,int] = {'usuario1':10, 'usuario2': 10}
print(usuarios)

# FASTAPI USA PYDANTIC
#validar datos de entrada y salida usando anotaciones


