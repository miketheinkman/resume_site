#!/usr/bin/python
import urllib2 as url
import json

OPEN_WEATHER_KEY = "3b67980a03d7bdd536bdcc831931148f"


def weather_by_zip(zipcode, key=OPEN_WEATHER_KEY):
    info = url.urlopen("http://api.openweathermap.org/data/2.5/weather?zip={0},us&appid="
                       "{1}".format(zipcode, key))
    weather = json.load(info)
    return weather


if __name__ == '__main__':
    print weather_by_zip("77573")