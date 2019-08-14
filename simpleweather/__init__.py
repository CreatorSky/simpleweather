import requests as re
from bs4 import BeautifulSoup


class Weather(object):
    def __init__(self, unit='F', cords=None):
        """
        :param unit: F for Fahrenheit, C for Celsius
        :param cords: Weather of the passed Geocordinates is fetched,
        If none,automatic Coordinates are fetched by ip.
        """
        if not cords:
            data = re.get('https://ipinfo.io/')
            cords = data.json()['loc']

        w_url = 'https://weather.com/weather/today/l/' + cords

        weather_data = re.get(w_url).text
        soup = BeautifulSoup(weather_data, features="html.parser")

        # City
        self.city = soup.find('h1', {'class': 'today_nowcard-location'}).text

        # Current Temp
        temp = soup.find('div', {'class': 'today_nowcard-temp'}).find('span').text

        # Phrase
        self.phrase = soup.find('div', {'class': 'today_nowcard-phrase'}).text

        # Feels Like
        feels = soup.find('span', {'class': 'deg-feels'}).text

        # High Low & UV Index
        hilo = list(soup.find('div', {'class': 'today_nowcard-hilo'}).children)

        self.uv_index = ' '.join(hilo[5].text.split(' ')[2::])

        # Precipitation
        precip = soup.find('span', {'class': 'precip-val'}).text
        self.precip = precip

        # Wind Humidity DewPoint Pressure Visibility
        tbody = soup.find('div', {'class': 'today_nowcard-sidecar'}).find('table').find('tbody').find_all('td')

        self.humidity = tbody[1].text

        if unit.lower() == 'f':
            self.current_temp = temp + ' F'
            self.feels_like = feels + ' F'
            self.hi = hilo[1].text + ' F' if hilo[1].text != '--' else hilo[1].text
            self.low = hilo[4].text + ' F'
            self.wind = tbody[0].text
            self.pressure = tbody[3].text
            self.dew_point = tbody[2].text + ' F'
            self.visibility = tbody[4].text
        else:
            self.current_temp = self.__f_to_c(temp)
            self.feels_like = self.__f_to_c(feels)
            self.hi = self.__f_to_c(hilo[1].text)
            self.low = self.__f_to_c(hilo[4].text)
            wind_data = tbody[0].text.split(' ')
            wind_data[1] = str(round(float(wind_data[1]) * 1.609, 2))
            wind_data[2] = 'km/h'
            self.wind = ' '.join(wind_data)
            self.pressure = str(round(float(tbody[3].text.split(' ')[0]) * 33.864, 2)) + ' mb'
            self.dew_point = self.__f_to_c(tbody[2].text)
            self.visibility = str(round(float(tbody[4].text.split(' ')[0]) * 1.609, 2)) + ' km'

    def __f_to_c(self, temp):
        if str(temp[:-1]).isdigit():
            return str(round((float(temp[:-1]) - 32) * 5 / 9,2)) + '° C'
        else:
            return temp







