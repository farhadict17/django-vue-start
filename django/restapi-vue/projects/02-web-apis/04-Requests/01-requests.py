import requests

def main():
    response = requests.get("https://api.exchangeratesapi.io/latest")
    print("Status code",response.status_code)
    #print("'Content-Type'",response.headers)
    #print("'Content-Type'",response.headers['Content-Type'])
    
    if response.status_code != 200:
        print("Status Code: ",response.status_code)
        raise Exception("There was an error")
    data = response.json()
    print ("json data:",data)


if __name__ == "__main__":
    main()