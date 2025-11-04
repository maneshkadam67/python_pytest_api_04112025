import requests

def get_users():
    respose=requests.get("https://reqres.in/api/users?page=2")
    print(respose.status_code)

get_users()