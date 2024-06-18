import requests
#from math import radians, sin, cos, sqrt, asin
from bs4 import BeautifulSoup
import math
import json
import time ,textwrap
import threading
from datetime import datetime,timedelta
 
#telegram bot
bot_token = '5880937101:AAEaJH8sO1coKephJjf4Bq1d4WI1Q3FwJpY' 
chat_id = '6142127925'
#requests.get(bot_url)

def astronomy():
    import datetime
    
    events = [
        ("Penumbral lunar eclipse", datetime.date(2023, 5, 5), "Visible from Africa, Oceania, Asia, Eastern Europe and Greece."),
        ("Full Moon", datetime.date(2023, 5, 5), ""),
        ("Eta Aquariids Meteor Shower", datetime.date(2023, 5, 6), "Moon phase: 99.8%."),
        ("New Moon", datetime.date(2023, 5, 19), ""),
        ("Mercury at Greatest West Elongation", datetime.date(2023, 5, 29), "The best time to photograph Mercury is just before Sunrise."),
        ("Manhattanhenge (Sunset)", datetime.date(2023, 5, 30), "Best locations: 14th Street, 34th Street, 42nd Street, 57th Street y 79th Street."),
        ("Full Moon", datetime.date(2023, 6, 4), ""),
        ("Venus at Greatest Eastern Elongation", datetime.date(2023, 6, 4), "This is the best time to view Venus since it's so bright that it becomes the third brightest object in the sky after the Sun and the Moon."),
        ("New Moon", datetime.date(2023, 6, 18), ""),
        ("Summer or winter solstice", datetime.date(2023, 6, 21), "It marks the longest or shortest day of the year."),
        ("Full Moon", datetime.date(2023, 7, 3), ""),
        ("Manhattanhenge (Sunset)", datetime.date(2023, 7, 12), "Best locations: 14th Street, 34th Street, 42nd Street, 57th Street y 79th Street."),
        ("New Moon", datetime.date(2023, 7, 17), ""),
        ("Delta Aquariids Meteor Shower", datetime.date(2023, 7, 30), "Moon phase: 95.6%."),
        ("Full Moon (Supermoon)", datetime.date(2023, 8, 1), ""),
        ("Mercury at Greatest Eastern Elongation", datetime.date(2023, 8, 9), "The best time to photograph Mercury is shortly after Sunset."),
        ("Perseids Meteor Shower", datetime.date(2023, 8, 12), "Moon phase: 10.0%."),
        ("New Moon", datetime.date(2023, 8, 16), ""),
        ("Saturn at opposition", datetime.date(2023, 8, 27), "It's brighter than at any other time of the year and is visible throughout the night. This is the best time to view and photograph Saturn and its rings."),
        ("Full Moon (Supermoon)", datetime.date(2023, 8, 31), ""),
        ("New Moon", datetime.date(2023, 9, 15), ""),
        ("Neptune at opposition", datetime.date(2023, 9, 19), "It's brighter than at any other time of the year and is visible throughout the night."),
        ("Mercury at Greatest Western Elongation", datetime.date(2023, 9, 22), "The best time to photograph Mercury is shortly before Sunrise."),
        ("Fall or spring equinox", datetime.date(2023, 9, 23), "This is the best time to photograph the zodiacal light."),
        ("Full Moon", datetime.date(2023, 9, 29), ""),
        ("Milky Way season ends (Northern Hemisphere)", datetime.date(2023, 10, 14), ""),
        ("Annular solar eclipse", datetime.date(2023, 10, 14), "The eclipse path will begin in the Pacific Ocean off the coast of southern Canada and move across the southwestern United States and Central America, Columbia, and Brazil. A partial eclipse will be visible throughout much of North and South America."),
        ("Orionids Meteor Shower", datetime.date(2023, 10, 21), "Moon phase: 51.2%."),
        ("Venus at Greatest Western Elongation", datetime.date(2023, 10, 23), "This is the best time to view Venus since it's so bright that it becomes the third brightest object in the sky after the Sun and the Moon."),
        ("Partial lunar eclipse", datetime.date(2023, 10, 28), "Visible in Africa, Oceania, the Americas, Asia, and Europe."),
        ("Full Moon", datetime.date(2023, 10, 28), ""),
        ("Jupiter at opposition", datetime.date(2023, 11, 3), "It's brighter than at any other time of the year and is visible throughout the night. This is the best time to view and photograph Jupiter and its moons."),
        ("New Moon", datetime.date(2023, 11, 13), ""),
        ("Uranus at opposition", datetime.date(2023, 11, 13), "It's brighter than at any other time of the year. You need a telescope."),
        ("Leonids Meteor Shower", datetime.date(2023, 11, 17), "Moon phase: 26.5%."),
        ("Full Moon", datetime.date(2023, 11, 27), ""),
        ("Manhattanhenge (Sunrise)", datetime.date(2023, 11, 30), "Best locations: 14th Street, 34th Street, 42nd Street, 57th Street y 79th Street."),
        ("Mercury at Greatest Eastern Elongation", datetime.date(2023, 12, 4), "The best time to photograph Mercury is shortly after Sunset."),
        ("New Moon", datetime.date(2023, 12, 13), ""),
        ("Geminids Meteor Shower", datetime.date(2023, 12, 14), "Moon phase: 5.6%."),
        ("Winter or summer solstice", datetime.date(2023, 12, 22), "It marks the shortest or longest day of the year."),
        ("Ursids Meteor Shower", datetime.date(2023, 12, 22), "Moon phase: 85.3%."),
        ("Full Moon", datetime.date(2023, 12, 27), "")]
        
    today = datetime.date.today()

    next_event = None
    for event in events:
        if event[1] >= today:
            next_event = event
            break

    if next_event is not None:
        name, date, info = next_event
        message = f"The {name} will happen on {date}. {info}"
        requests.get(f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}')
    else:
        message = "There are no upcoming events."
        requests.get(f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}')
        

def get_philippine_time():
    # Get the current time in UTC
    now_utc = datetime.utcnow()
    # Convert to Philippine time (UTC +8)
    now_ph = now_utc + timedelta(hours=8)
    return now_ph

def Weather():
    city_name='Tagbilaran City, PH'
    api_key = '30d4741c779ba94c470ca1f63045390a'
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&APPID={api_key}") 
    if weather_data.json()['cod'] == '404':
        message = "App: error on request from weather function!"
        requests.get(f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}')
    else:
        # Retrieve temperature data
        weather = weather_data.json()['weather'][0]['main']
        
        temp_f = weather_data.json()['main']['temp']
        temp_c = round((temp_f - 32) * 5/9)

        feels_like_f = weather_data.json()['main']['feels_like']
        feels_like_c = round((feels_like_f - 32) * 5/9)
        
        temp_min_f = weather_data.json()['main']['temp_min']
        temp_min_c = round((temp_min_f - 32) * 5/9)
        
        temp_max_f = weather_data.json()['main']['temp_max']
        temp_max_c = round((temp_max_f - 32) * 5/9)

        humidity = weather_data.json()['main']['humidity']  # Retrieve humidity data
        precipitation = weather_data.json()['weather'][0]['description']  # Retrieve precipitation data
        
        dew_point_f = temp_f - ((100 - humidity)/5)  # Retrieve dew_point data
        dew_point_c = round((dew_point_f - 32) * 5/9)

        pressure = weather_data.json()['main']['pressure']  # Retrieve pressure data
        
        visibility_meters = weather_data.json()['visibility']  # Retrieve visibility data
        visibility_km = visibility_meters / 1000
        
        wind_speed_mph = weather_data.json()['wind']['speed']  # Retrieve wind_speed data
        wind_speed_ms = wind_speed_mph * 0.44704
        wind_speed_rounded = round(wind_speed_ms, 1)
        
        wind_direction = weather_data.json()['wind']['deg']  # Retrieve wind_direction data

        # Convert the wind direction angle to a cardinal direction
        if 348.75 <= wind_direction < 11.25:
            direction = "N"
        elif 11.25 <= wind_direction < 33.75:
            direction = "NNE"
        elif 33.75 <= wind_direction < 56.25:
            direction = "NE"
        elif 56.25 <= wind_direction < 78.75:
            direction = "ENE"
        elif 78.75 <= wind_direction < 101.25:
            direction = "E"
        elif 101.25 <= wind_direction < 123.75:
            direction = "ESE"
        elif 123.75 <= wind_direction < 146.25:
            direction = "SE"
        elif 146.25 <= wind_direction < 168.75:          
            direction = "SSE"
        elif 168.75 <= wind_direction < 191.25:
            direction = "S"
        elif 191.25 <= wind_direction < 213.75:
            direction = "SSW"
        elif 213.75 <= wind_direction < 236.25:
            direction = "SW"
        elif 236.25 <= wind_direction < 258.75:
            direction = "WSW"
        elif 258.75 <= wind_direction < 281.25:
            direction = "W"
        elif 281.25 <= wind_direction < 303.75:
            direction = "WNW"
        elif 303.75 <= wind_direction < 326.25:
            direction = "NW"
        elif 326.25 <= wind_direction < 348.75:
            direction = "NNW"
        else:
            direction = "Unknown"

        message = f"The ☁️ in {city_name}\n"
        message += f"{precipitation} {temp_min_c} °C\n"
        message += f"Feels Like: {feels_like_c} °C \n"
        message += f"Wind Speed: {wind_speed_rounded} m/s {direction}\n"
        message += f"Humidity: {humidity}%\n"
        message += f"Dew Point: {dew_point_c} °C\n"
        message += f"Visibility: {visibility_km} km"
        
        bot_url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}'
        requests.get(bot_url)

def schedule_weather_message():
    print('weather 2nd function is now running')
    while True:
        now_ph = get_philippine_time()# Get the current time in Philippine time
        if now_ph.hour == 7 and now_ph.minute == 0:# Check if it's 7 AM in Philippine time
            message = "Good Morning👋"  
            bot_url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"
            requests.get(bot_url)
            astronomy()
            time.sleep(10)
            Weather()
            time.sleep(60)

class My_ISS_Track_App:
    N2YO_API_KEY = 'C8JULN-R755FA-KCYTK3-507U'
    THRESHOLD_DISTANCE = 900  # Threshold distance in km for ISS passing over location
    MY_LATITUDE = 9.8500
    MY_LONGITUDE = 124.1435

    def calculate_distance(self, lat1, lon1, lat2, lon2):
        # Convert degrees to radians
        lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
        # Apply haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a))
        km = 6371 * c
        return km

    def get_iss_location(self):
        print("iss function is now running")
        while True:
            try:
                response = requests.get('https://api.n2yo.com/rest/v1/satellite/positions/25544/0/0/0/1/&apiKey={}'.format(self.N2YO_API_KEY))
                data = json.loads(response.text)
                iss_latitude = float(data['positions'][0]['satlatitude'])
                iss_longitude = float(data['positions'][0]['satlongitude'])
            except:
                print("App: Error on request function or Might exceed the maximum request per hour on the API")
                time.sleep(60) # Sleep for 60 seconds and try again

            iss_longitude_rounded = round(iss_longitude, 2)
            iss_latitude_rounded = round(iss_latitude, 2)

            distance = self.calculate_distance(self.MY_LATITUDE, self.MY_LONGITUDE, iss_latitude, iss_longitude)

            if distance <= self.THRESHOLD_DISTANCE:
                message = f"The Space station will be passing within {self.THRESHOLD_DISTANCE} km of your location❗️"
                bot_url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}'
                requests.get(bot_url)
                time.sleep(250) # 4 mins and 10 secs sleep
            else:
                #message = f"The ISS is not visible"
                #bot_url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}'
                #requests.get(bot_url)
                time.sleep(40) # 40 sec sleep

    def run(self):
        self.get_iss_location()

def iss_track_app():
    app = My_ISS_Track_App()
    app.run()

def bohol_news(): 
    url = 'https://www.boholchronicle.com.ph/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    titles = soup.find_all(class_='title')
    bot_url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text=top 4 latest news on bohol chronicle' 
    requests.get(bot_url)
    for title in titles[1:5]:
        message = title.text
        bot_url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}'
        requests.get(bot_url)
        
def ph_news():
    api_key = 'f397b1478a234090a6135a008a119a1e'

    endpoint = 'https://newsapi.org/v2/top-headlines'
    params = {'country': 'ph', 'pageSize': 5, 'apiKey': api_key}
    
    response = requests.get(endpoint, params=params)# Make a request to the API and get the response
    data = json.loads(response.text)# Parse the JSON data from the response

    # Loop through the articles and format the output
    for i, article in enumerate(data['articles']):
        # Wrap the article title to a certain width
        wrapped_title = textwrap.fill(article['title'], width=80)
        message = article['url']
        requests.get(f'https://api.telegram.org/bot5880937101:AAEaJH8sO1coKephJjf4Bq1d4WI1Q3FwJpY/sendMessage?chat_id=6142127925&text={message}')
        time.sleep(60)#sends news every 1 minute

def schedule_for_news():
    print("news function is now running")
    while True:
        now_ph = get_philippine_time()# Get the current time in Philippine time
        if now_ph.hour == 8 and now_ph.minute == 0:
            bohol_news()
            time.sleep(60)
        elif now_ph.hour == 8 and now_ph.minute == 4:
            ph_news()
            
if __name__ == '__main__':
    print("weather 1st function is now running")
    Weather()
    thread1 = threading.Thread(target=schedule_weather_message)#send weather message at specific time
    thread2 = threading.Thread(target=iss_track_app)
    thread3 = threading.Thread(target=schedule_for_news)
        
    thread1.start()# Start the threads
    thread2.start()
    thread3.start()
    
    thread1.join()# Wait for the threads to finish
    thread2.join()
    thread3.join()

    

    
