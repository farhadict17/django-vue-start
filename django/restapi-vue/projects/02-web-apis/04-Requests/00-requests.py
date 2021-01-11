import requests

def main():
    response = requests.get("http://www.google.com") #Status Code: 200 OK
    # response = requests.get("http://www.google.com/random-address/")  #Status Code: 404 not found
    print("Status Code:", response.status_code)
    #print("Status Code:", response.headers)
    #print("Content-Type:", response.headers["Content-Type"])
    print("Content:", response.text)



if __name__ == "__main__":
    main()