
import requests

def client():
    #credentials = {"username": "admin", "password": "admin"}
    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/",
    #                         data=credentials)
    token_h = "Token 1ba2df12ef8dbee6ff2304b78e6ac3625d382469"
    headers = {"Authorization":token_h}
    response = requests.get("http://127.0.0.1:8000/api/profiles",
                            headers=headers)
    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()