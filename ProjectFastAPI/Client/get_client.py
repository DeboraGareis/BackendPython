import requests
#URL = "http://127.0.0.1:8000/reviews"
URL = "http://127.0.0.1:8000/reviews?page=2&limit=2"
HEADERS = {"accept" : "application/json"}

#podemos usar un queryset
#QUERYSET = {"page" : 1, "limit" : 2}
#response = requests.get(URL, headers=HEADERS, params=QUERYSET)
response = requests.get(URL, headers=HEADERS)
if response.status_code == 200:
    print("Peticion realizada de forma exitosa")
    print(response.content)
    print("\n")
    print(response.headers)

if response.headers.get("content-type") =="application/json":
    reviews = response.json()
    for review in reviews:
        print(f"> score: {review["score"]} - {review["review"]}") 

