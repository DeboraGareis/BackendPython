import requests

URL = "http://127.0.0.1:8000/reviews"
REVIEW={
  "user_id": 10,
  "movie": {
    "id": 2,
    "title": "pelicula 1"
  },
  "review": "reseña 2 creada con request",
  "score": 5
}

response = requests.post(URL, json=REVIEW)

if response.status_code==200:
    print("reseña creada exitosamente con id: ", response.json()['id'])
else:
    print(response.content)
