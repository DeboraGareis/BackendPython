import requests

REVIEW_ID = 9
URL = f"http://127.0.0.1:8000/reviews/{REVIEW_ID}"

response = requests.delete(URL)

if response.status_code == 200:
    print("reseña eliminada desde delete_client.py")
    print(response.json())
else: 
    print("falla al eliminar desde delete_client.py")
