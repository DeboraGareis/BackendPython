from jinja2 import Environment, FileSystemLoader
from wsgiref.simple_server import make_server

def application(env, start_response):
    headers = [('Content-Type', 'text/html')]
    start_response('200 OK', headers)
    env = Environment(loader = FileSystemLoader('templates'))
    template=env.get_template('index.html')
    
    #pasamos como argumento en diccionario los valores de las variables
    pagina=template.render(
        {
            "title":"servidor python",
            "name":"debora"
        }
    )
    return [bytes(pagina,'utf-8')]

#creacion de un serivdor de prueba con make_server
server = make_server('localhost', 8000, application)
#indicar al servidor que se enceuntre a la escucha siempre hasta que lo detengamos
server.serve_forever()








