from urllib.request import urlopen
from dataclasses import dataclass
import json


@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float


def get_coordinates() -> Coordinates:
    data = _get_ip_data()
    latitude = data['loc'].split(',')[0]
    longitude = data['loc'].split(',')[1]

    return Coordinates(latitude=latitude, longitude=longitude)

def get_coordinatesMitte() -> Coordinates:
    latitude = 52.520008
    longitude = 13.404954

    return Coordinates(latitude=latitude, longitude=longitude)

def get_coordinatesMoscow() -> Coordinates:
    latitude = 55.751244
    longitude = 37.618423

    return Coordinates(latitude=latitude, longitude=longitude)

def get_coordinatesKyiv() -> Coordinates:
    latitude = 50.450001
    longitude = 30.523333

    return Coordinates(latitude=latitude, longitude=longitude)

def get_coordinatesIstanbul() -> Coordinates:
    latitude = 41.015137
    longitude = 28.979530

    return Coordinates(latitude=latitude, longitude=longitude)

def get_coordinatesNew_York() -> Coordinates:
    latitude =  40.730610
    longitude = -73.935242

    return Coordinates(latitude=latitude, longitude=longitude)

def _get_ip_data() -> dict:
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    return json.load(response)