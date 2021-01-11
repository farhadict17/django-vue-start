
import requests

def client():
    # data = {
    #     "username": "test1", 
    #     "email":"test1@gmail.com",
    #     "password1": "changegame1234",
    #     "password2": "changegame1234"
    #     }
    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/",
    #                         data=data)




    token_h = "Token e4b6c9bf224683460f9e81cb1e6ba18c4e3d1871"
    headers = {"Authorization":token_h}
    response = requests.get("http://127.0.0.1:8000/api/profiles",
                            headers=headers)
    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()