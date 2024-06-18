import requests ,datetime , time , math ,json
from bs4 import BeautifulSoup


BOT_TOKEN = ''
CHAT_ID = ''

def bot(text):
    URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}"
    requests.get(URL)

def astronomy():
    from datetime import date

    events = [
        ("Penumbral lunar eclipse", date(2023, 5, 5), "Visible from Africa, Oceania, Asia, Eastern Europe and Greece."),
        ("Full Moon", date(2023, 5, 5), ""),
        ("Eta Aquariids Meteor Shower", date(2023, 5, 6), "Moon phase: 99.8%."),
        ("New Moon", date(2023, 5, 19), ""),
        ("Mercury at Greatest West Elongation", date(2023, 5, 29), "The best time to photograph Mercury is just before Sunrise."),
        ("Manhattanhenge (Sunset)", date(2023, 5, 30), "Best locations: 14th Street, 34th Street, 42nd Street, 57th Street y 79th Street."),
        ("Full Moon", date(2023, 6, 4), ""),
        ("Venus at Greatest Eastern Elongation", date(2023, 6, 4), "This is the best time to view Venus since it's so bright that it becomes the third brightest object in the sky after the Sun and the Moon."),
        ("New Moon", date(2023, 6, 18), ""),
        ("Summer or winter solstice", date(2023, 6, 21), "It marks the longest or shortest day of the year."),
        ("Full Moon", date(2023, 7, 3), ""),
        ("Manhattanhenge (Sunset)", date(2023, 7, 12), "Best locations: 14th Street, 34th Street, 42nd Street, 57th Street y 79th Street."),
        ("New Moon", date(2023, 7, 17), ""),
        ("Delta Aquariids Meteor Shower", date(2023, 7, 30), "Moon phase: 95.6%."),
        ("Full Moon (Supermoon)", date(2023, 8, 1), ""),
        ("Mercury at Greatest Eastern Elongation", date(2023, 8, 9), "The best time to photograph Mercury is shortly after Sunset."),
        ("Perseids Meteor Shower", date(2023, 8, 12), "Moon phase: 10.0%."),
        ("New Moon", date(2023, 8, 16), ""),
        ("Saturn at opposition", date(2023, 8, 27), "It's brighter than at any other time of the year and is visible throughout the night. This is the best time to view and photograph Saturn and its rings."),
        ("Full Moon (Supermoon)", date(2023, 8, 31), ""),
        ("New Moon", date(2023, 9, 15), ""),
        ("Neptune at opposition", date(2023, 9, 19), "It's brighter than at any other time of the year and is visible throughout the night."),
        ("Mercury at Greatest Western Elongation", date(2023, 9, 22), "The best time to photograph Mercury is shortly before Sunrise."),
        ("Fall or spring equinox", date(2023, 9, 23), "This is the best time to photograph the zodiacal light."),
        ("Full Moon", date(2023, 9, 29), ""),
        ("Milky Way season ends (Northern Hemisphere)", date(2023, 10, 14), ""),
        ("Annular solar eclipse", date(2023, 10, 14), "The eclipse path will begin in the Pacific Ocean off the coast of southern Canada and move across the southwestern United States and Central America, Columbia, and Brazil. A partial eclipse will be visible throughout much of North and South America."),
        ("Orionids Meteor Shower", date(2023, 10, 21), "Moon phase: 51.2%."),
        ("Venus at Greatest Western Elongation", date(2023, 10, 23), "This is the best time to view Venus since it's so bright that it becomes the third brightest object in the sky after the Sun and the Moon."),
        ("Partial lunar eclipse", date(2023, 10, 28), "Visible in Africa, Oceania, the Americas, Asia, and Europe."),
        ("Full Moon", date(2023, 10, 28), ""),
        ("Jupiter at opposition", date(2023, 11, 3), "It's brighter than at any other time of the year and is visible throughout the night. This is the best time to view and photograph Jupiter and its moons."),
        ("New Moon", date(2023, 11, 13), ""),
        ("Uranus at opposition", date(2023, 11, 13), "It's brighter than at any other time of the year. You need a telescope."),
        ("Leonids Meteor Shower", date(2023, 11, 17), "Moon phase: 26.5%."),
        ("Full Moon", date(2023, 11, 27), ""),
        ("Manhattanhenge (Sunrise)", date(2023, 11, 30), "Best locations: 14th Street, 34th Street, 42nd Street, 57th Street y 79th Street."),
        ("Mercury at Greatest Eastern Elongation", date(2023, 12, 4), "The best time to photograph Mercury is shortly after Sunset."),
        ("New Moon", date(2023, 12, 13), ""),
        ("Geminids Meteor Shower", date(2023, 12, 14), "Moon phase: 5.6%."),
        ("Winter or summer solstice", date(2023, 12, 22), "It marks the shortest or longest day of the year."),
        ("Ursids Meteor Shower", date(2023, 12, 22), "Moon phase: 85.3%."),
        ("Full Moon", date(2023, 12, 27), "")]

    today = datetime.date.today()

    next_event = None
    for event in events:
        if event[1] >= today:
            next_event = event
            break

    if next_event is not None:
        name, date, info = next_event
        message = f"The {name} will happen on {date}. {info}"
        bot(message)

    else:
        message = "There are no upcoming events."
        bot(message)


def weather():
    CITY_NAME='Tagbilaran City, PH'
    API_KEY = '30d4741c779ba94c470ca1f63045390a'

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&units=imperial&APPID={API_KEY}")

    if weather_data.json()['cod'] == '404':
        message = "⚠️ An error occurred in weather function: failed to request , code 404"
        bot(message)

    else:
        # Retrieve temperature data
        #weather = weather_data.json()['weather'][0]['main']

        temp_f = weather_data.json()['main']['temp']
        #temp_c = round((temp_f - 32) * 5/9)

        feels_like_f = weather_data.json()['main']['feels_like']
        feels_like_c = round((feels_like_f - 32) * 5/9)

        temp_min_f = weather_data.json()['main']['temp_min']
        temp_min_c = round((temp_min_f - 32) * 5/9)

        #temp_max_f = weather_data.json()['main']['temp_max']
        #temp_max_c = round((temp_max_f - 32) * 5/9)

        humidity = weather_data.json()['main']['humidity']  # Retrieve humidity data
        precipitation = weather_data.json()['weather'][0]['description']  # Retrieve precipitation data

        dew_point_f = temp_f - ((100 - humidity)/5)  # Retrieve dew_point data
        dew_point_c = round((dew_point_f - 32) * 5/9)

        #pressure = weather_data.json()['main']['pressure']  # Retrieve pressure data

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

        message = f"The ☁️ in {CITY_NAME}\n"
        message += f"{precipitation} {temp_min_c} °C\n"
        message += f"Feels Like: {feels_like_c} °C \n"
        message += f"Wind Speed: {wind_speed_rounded} m/s {direction}\n"
        message += f"Humidity: {humidity}%\n"
        message += f"Dew Point: {dew_point_c} °C\n"
        message += f"Visibility: {visibility_km} km"

        bot(message)

class Iss_App:

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
        print("ISS locator is running!")
        while True:
            try:
                response = requests.get('https://api.n2yo.com/rest/v1/satellite/positions/25544/0/0/0/1/&apiKey={}'.format(self.N2YO_API_KEY))
                data = json.loads(response.text)
                iss_latitude = float(data['positions'][0]['satlatitude'])
                iss_longitude = float(data['positions'][0]['satlongitude'])

            except:
                message = "⚠️ An error occurred in Iss tracker function: Might exceed the maximum request per hour on the API"
                bot(message)
                time.sleep(3600)

            #iss_longitude_rounded = round(iss_longitude, 2)
            #iss_latitude_rounded = round(iss_latitude, 2)

            distance = self.calculate_distance(self.MY_LATITUDE, self.MY_LONGITUDE, iss_latitude, iss_longitude)

            if distance <= self.THRESHOLD_DISTANCE:
                message = f"🚀 Alert: Space Station will be passing within {self.THRESHOLD_DISTANCE} km of your location❗️"
                bot(message)
                time.sleep(250) # 4 mins and 10 secs sleep
            else:
                #else for an iss not visible
                time.sleep(40) # 40 sec sleep

    def run(self):
        self.get_iss_location()

def iss_alert():
    app = Iss_App()
    app.run()


def main_news():

    API_KEY = 'f397b1478a234090a6135a008a119a1e'
    ENDPOINT = 'https://newsapi.org/v2/top-headlines'
    params = {'country': 'ph', 'pageSize': 6, 'apiKey': API_KEY}

    response = requests.get(ENDPOINT, params=params)
    data = json.loads(response.text)

    try:
        for i, article in enumerate(data['articles']):
            message = article['url']
            bot(message)
            time.sleep(3)
    except:
        message = "⚠️ An error occurred in PH News function"
        bot(message)
        time.sleep(60)

def pag_asa():
    print('pag-asa report have sent!')
    url = "https://www.pagasa.dost.gov.ph/weather#:~:text=SYNOPSIS%3A%20At%203%3A00%20AM,the%20rest%20of%20the%20country"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    heading = soup.find("div", class_="panel-heading").get_text().strip()
    body = soup.find("div", class_="panel-body").get_text().strip()

    bot(heading)
    bot(body)

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
        
        
def get_philippine_time():

    from datetime import datetime, timedelta

    now_utc = datetime.utcnow()# Get the current time in UTC
    now_ph = now_utc + timedelta(hours=8)# Convert to Philippine time (UTC +8)
    return now_ph


def schedule():
    print("schedule is running!")

    while True:
        now_ph = get_philippine_time()# Get the current time in Philippine time
        if now_ph.hour == 6 and now_ph.minute == 0 :# Check if it's 7 AM in Philippine time
            bot("Good Morning👋")
            astronomy()
            time.sleep(10)
            weather()
            time.sleep(50)
        elif now_ph.hour == 8 and now_ph.minute == 0:
            pag_asa()

