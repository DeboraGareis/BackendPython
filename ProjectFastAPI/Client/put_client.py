import requests
REVIEW_ID = 8
URL = f"http://127.0.0.1:8000/reviews/{REVIEW_ID}"

REVIEW={
  "review": "actualizamos contenido con put",
  "score": 1
}


response = requests.put(URL, json=REVIEW)

if response.status_code == 200:
    print("reseña actualizada desde put_client.py")
    print(response.json())
else:
    print("error en actualizacion", response.status_code)
