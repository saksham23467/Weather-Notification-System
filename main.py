API_KEY = "Your-API-KEY"
MY_LAT = 28.701870
MY_LONG = 77.098358
account_sid = 'YOUR-ACCOUNT-SID'
auth_token = "YOUR-AUTH-TOCKEN"
import requests
from twilio.rest import Client



parameter = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "cnt": 4,
    "appid": API_KEY
}
OMW_ENDPOINT = " https://api.openweathermap.org/data/2.5/forecast"
response = requests.get(OMW_ENDPOINT, params=parameter)

# print(response.json()["list"][0]['weather'][0]['id'])
will_rain=False
for i in range(4):
    weather_id = response.json()["list"][i]['weather'][0]['id']
    if weather_id < 700:
        will_rain = True
        # my_label = Label(window, text="It will rain today, You're advised to carry an umbrella",
        #                  font=("Helvetica", 20, "bold"))
        # my_label.pack()
        # window.mainloop()
    # if response.json()['list'][i]["main"]["temp"]>315:
    #     print(response.json()['list'][i]["dt_txt"])
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+12087470851',
        body="hello",
        to='YOUR-PHONE-NUMBER'
    )

print(message.status)
print(message.sid)

