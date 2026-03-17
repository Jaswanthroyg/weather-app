import requests
api_key="YOUR_API_KEY"
city=input("Enter city:")
url="https://api.openweathermap.org/data/2.5/weather"
params={
    "q":city,
    "appid":api_key,
    "units":"metric"
    }
try:
    response=requests.get(url,params=params)
    if response.status_code==200:
        data=response.json()
        print("City:",data["name"])
        print("Temparature:",data["main"]["temp"],"°C")
        print("Weather:",data["weather"][0]["description"])
        print("Humidity:",data["main"]["Humidity"]
    else:
        print("city not found or error:",response.status_code)
except requests.exceptions.RequestException as e:
    print("Request failed:",e)
