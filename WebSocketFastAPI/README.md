Pasos:
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn websockets
uvicorn ejWebSocketFastAPI:app --reload
