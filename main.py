import requests
import argparse
from datetime import datetime

def get_current_date():
    current_date = datetime.now().date()
    formatted_date = current_date.strftime("%Y-%m-%d")
    return formatted_date

def check_city_location():
    response = requests.get('http://ip-api.com/json')
    if response.status_code == 200:
        data = response.json()
        return data['city']
    else:
        return None
def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('option', choices=['rain', 'shine'], help='Choose between rain and shine')
    args = parser.parse_args()
    return args.option

def CheckWeatherStatus():
    shine_or_rain = arguments()
    city = check_city_location()
    date = get_current_date()
    parameters =  {
        'access_key': '349b8eb07c0a88e50f6fb572d84290e4',
        'query': city,
        'forecast_days': 1,
        'hourly': 1,
        'interval': 1
    }
    request = requests.get('http://api.weatherstack.com/forecast', parameters)
    api_response = request.json()
    if shine_or_rain == 'shine':
        if api_response['current']['uv_index'] > 3:
#            print('UV index is greater then 3 you should take the sunscreen')
            return True

    elif shine_or_rain == 'rain':
        if api_response['forecast'][date]['hourly']['chanceofrain'] > 5:
#            print('I suggest to take umbrella with you maybe it will rain')
            return True
    else:
        return False

if __name__ == '__main__':
    CheckWeatherStatus()
