# SimpleWeather

A python module to get weather by ip or geo-coordinates. 

Install via source: `python setup.py install`  
Install via pip: `pip install -i https://test.pypi.org/simple/ simpleweather`  
  
>Constructor takes 1 fixed and 1 optional parameter.  

 1. unit : 'F' for Fahrenheit (Imperial), 'C' for Celsius (Metric)
 2. cords : default - None, if passed, the weather of the given coordinates is fetched.

 
>Following are the instance variable which can be called:

 - **city** : Name of the city
 - **current_temp** : Current tempreture 
 - **phrase** : Phrase of the current weather
 - **feels_like** : Feels like tempreture
 - **hi** : Highest recorded tempreture of the day
 - **low** : Lowest recorded tempreture of the day
 - **uv_index** : UV Index out of 10
 - **precip** : Chances of precipetation
 - **wind** : Speed of the wind
 - **humidity** : Humidity recorded
 - **dew_point** : Dew point tempreture
 - **pressure** : Pressure
 - **visibility** : Visibility

> Demo:

    from simpleweather import Weather
    w = Weather(unit='C')
    print(w.current_temp)
    print(w.phrase)
    print(w.wind)

>Output:

    21° C
    Partly Cloudy
    N 11.26 km/h 
