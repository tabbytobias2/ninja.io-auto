import http.client
import json
import getpass
import time

def gold(id):
    conn2 = http.client.HTTPSConnection("api2.ninja.io")

    payload2 = '{\n  "id":"' + id + '"\n}'

    headers2 = {'Content-Type': "application/json",'User-Agent': "Insomnia/2023.5.2"}

    conn2.request("POST", "/user/reward-shop", payload2, headers2)

    res2 = conn2.getresponse()
    data2 = res2.read()
    goldres = json.loads(data2.decode("utf-8"))
    
    print("Recieved " + str(goldres["reward"]) +" gold.")
    
    if "error" in goldres:
        print(goldres["error"]);

conn = http.client.HTTPSConnection("api2.ninja.io")

username = input("Enter your username: ")

password = getpass.getpass("Enter your password: ")

try:
    iterations = int(input("Enter iterations: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")

payload = {"name": username, "password": password}

payload_json = json.dumps(payload)

headers = {'Content-Type': "application/json",'User-Agent': "Insomnia/2023.5.2"}

conn.request("POST", "/user/login", payload_json, headers)

res = conn.getresponse()
data = res.read()

if res.status == 200:
    
    response_json = json.loads(data.decode("utf-8"))
    
    if "id" in response_json:
        authentication_token = response_json["id"]
        i = 0
        while (i < iterations):
            gold(authentication_token)
            i += 1
            if (i < iterations):
                print("Next gold availible in 60 seconds...")
                time.sleep(61)
            else:
                print("Finished all iteration.")     
    else:
        print("Incorrect username or password")
else:
    print(f"HTTP Error: {res.status} - {res.reason}, please report to dev")

conn.close()
