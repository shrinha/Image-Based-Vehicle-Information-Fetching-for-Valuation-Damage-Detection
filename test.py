import requests
import json

def fetchInfo(plate="dl7cn5617"):
    url = "https://rto-vehicle-details.p.rapidapi.com/?rapidapi-key=9c1adb8cf1msh0da252e07b8e18dp1d266cjsn50ec78c66839/"

        # Make sure payload is properly formatted as JSON
    payload = { "vehicleId": "dl7cn5617" }

    headers = {
            "content-type": "application/json",
            "Content-Type": "application/json",
            "X-RapidAPI-Key": "9c1adb8cf1msh0da252e07b8e18dp1d266cjsn50ec78c66839",
            "X-RapidAPI-Host": "rto-vehicle-details.p.rapidapi.com"
        }

    try:
            response = requests.post(url, json=payload, headers=headers)

            # Check if the response status code is 200 (OK)
            if response.status_code == 200:
                res = ((response.json()))
                ans = [res['brand_name'],res['brand_model'],res['registration_date'],res['fuel_type'],res['cubic_capacity'],res['is_financed'],res['seating_capacity']]
                return ans
            else:
                print("Request failed with status code:", response.status_code)

    except requests.exceptions.RequestException as e:
            print("Request error:", e)
