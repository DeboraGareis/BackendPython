import requests

URL = f"http://127.0.0.1:8000/"

USER={
  "username": "user10",
  "password": "12345"
}


response = requests.post(URL+"login", json=USER)

if response.status_code == 200:
    print("autenticacion exitosa")
    print(response.json())
    print(response.cookies) #RequestCookieJar
    print(response.cookies.get_dict())
    user_id = response.cookies.get_dict().get("user_id")
    print(user_id)
else:
    print("error en autenticacion", response.status_code)