import requests

class TestAPI:
    #BASE_URL="https://reqres.in/api"
    def test_get_users(self):
        respose=requests.get("https://reqres.in/api/users?page=2")
        assert respose.status_code==200
        assert "data" in respose.json()

    def test_create_user(self):
        payload={
        "name": "morpheus",
        "job": "leader1"
        }
        response=requests.post("https://reqres.in/api/users",json=payload)
        print(response)
        # assert response.status_code==401
        # assert response.json()['name'] == "manish"







