from wsgiref.simple_server import make_server
pagina = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Pagina de prueba</title>
    </head>
    <body>
        <label for="css-textarea">Do you have any questions:</label>
        <div class="answer">
            <textarea id="css-textarea" name="css-questions" rows="5" cols="24" placeholder="Who is flexbox..."></textarea>
        </div>
        <button type="submit">Send</button>
    </body>
</html>
"""
def application(env, start_response):
    headers = [('Content-Type', 'text/html')]
    start_response('200 OK', headers)
    return [bytes(pagina,'utf-8')]

#creacion de un serivdor de prueba con make_server
server = make_server('localhost', 8000, application)
#indicar al servidor que se enceuntre a la escucha siempre hasta que lo detengamos
server.serve_forever()








