import requests
from win10toast import ToastNotifier
import json
import time


def covid_update():
    response = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    covid_data = response.json()
    results = f'Total Confirmed Cases : {covid_data["cases"]} \n Total Deaths : {covid_data["deaths"]} \n Total Recovered : {covid_data["recovered"]}'


    while True:
        covid_toast = ToastNotifier.show("Covid-19 Updates", results, duration = 20)
        time.sleep(60)


covid_update()

