import requests 
import os
import json



root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
api_settings_path = os.path.join(root_dir,"api","api_settings.json")

try:
    with open(api_settings_path) as f:
        api_file = json.load(f)
except:
    print(f"api_settings.json file not found at path: {api_settings_path}")

header = api_file["headers"]
# resp = request(method="get",url="https://www.nseindia.com/get-quotes/equity?symbol=INFY")

# print(resp.json())

def get_market_status():
    url = "https://www.nseindia.com/api/marketStatus"
    headers = header
    resp = requests.get(url=url,headers=headers)
    if resp.status_code == 200:
        data = resp.json()
        if data["marketState"][0]["marketStatus"] == "Close":
            print("market is closed")
            return False
        elif data["marketState"][0]["marketStatus"] == "Open":
            print("market is open")
            return True
        else:
            print("something went wrong!")
    else:
        print("api is not working")


def get_live_data():

    url = "https://www.nseindia.com/api/quote-equity?symbol=INFY"
    headers = header
    resp = requests.get(url=url,headers=headers)
    if resp.status_code == 200:
        data = resp.json()
        price = data["priceInfo"]
        print(price)
    else:
        print(resp.status_code)
        error =  resp.json()
        print(error)

get_live_data()
