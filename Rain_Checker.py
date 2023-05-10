import requests
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from API_KEYS import *

lat = 48.775845
lon = 9.182932
response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={openweather_apiKey}")

rainy = False
data = response.json()["hourly"][7:16]
for i in data:
    if i["weather"][0]["id"] == 502 or i["weather"][0]["id"] == 503 or i["weather"][0]["id"] == 504:
        rainy = True
if rainy:
    message = Mail(
        from_email='sherifookhamis@gmail.com',
        to_emails='Sherif.K@outlook.de',
        subject='Rain Checker',
        plain_text_content="Es regnet heute!")

    sg = SendGridAPIClient(sendgrid_apiKey)
    response = sg.send(message)

