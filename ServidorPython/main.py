from wsgiref.simple_server import make_server

def application(env, start_response):
    headers = [('Content-Type', 'text/plain')]
    start_response('200 OK', headers)
    return ['respuesta en texto plano de servidor python'.encode("utf-8")]

#creacion de un serivdor de prueba con make_server
server = make_server('localhost', 8000, application)
#indicar al servidor que se enceuntre a la escucha siempre hasta que lo detengamos
server.serve_forever()








