#!/usr/bin/python
import urllib2 as url
import json
from math import sqrt

"""In this module we do a few simple operations to demonstrate a RESTful API. You could do some real heavy lifting here,
but that wasn't necessary to demonstrate how REST works in flask. Also, I know that I shouldn't leave a key here, but
it's openweathermap. If you want to query the weather on my key, go ahead."""
OPEN_WEATHER_KEY = "3b67980a03d7bdd536bdcc831931148f"


# Obviously I cheated on my weather API and passed the zip to a real weather API with urllib2 and jsonified the result
def weather_by_zip(zipcode, key=OPEN_WEATHER_KEY):
    info = url.urlopen("http://api.openweathermap.org/data/2.5/weather?zip={0},us&appid="
                       "{1}".format(zipcode, key))
    weather = json.load(info)
    return weather


# This is a fast way to do fibonacci, but it has an upper limit after which you will get an OverflowError
def fibonacci(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))


if __name__ == '__main__':
    print fibonacci(150)
