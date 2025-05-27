from fastapi import FastAPI, WebSocket, WebSocketDisconnect, UploadFile, File
from fastapi.responses import HTMLResponse
from typing import List

app = FastAPI()

# Lista de conexiones WebSocket activas
active_connections: List[WebSocket] = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    print("Cliente conectado")
    try:
        while True:
            await websocket.receive_text()  # Mantener la conexión viva
    except WebSocketDisconnect:
        active_connections.remove(websocket)
        print("Cliente desconectado")

@app.post("/upload/")
async def upload(files: List[UploadFile] = File(...)):
    resultados = []
    for file in files:
        resultado = {
            "filename": file.filename,
            "resultado": f"Simulado OK para {file.filename}"
        }
        resultados.append(resultado)

        # Enviar resultado parcial a todos los clientes WebSocket conectados
        for connection in active_connections:
            try:
                await connection.send_json(resultado)
            except Exception as e:
                print(f"Error enviando WebSocket: {e}")

    return {"status": "Procesamiento simulado", "resultados": resultados}