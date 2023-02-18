from coordinates import get_coordinates, get_coordinatesMitte, get_coordinatesIstanbul, get_coordinatesKyiv, get_coordinatesMoscow, get_coordinatesNew_York
from api_service import get_weather


def weather() -> str:
    wthr = get_weather(get_coordinates())
    return f'{wthr.location}, {wthr.description}\n' \
           f'Temperature is {wthr.temperature}°C, feels like {wthr.temperature_feeling}°C'



def weatherMitte() -> str:
    wthr = get_weather(get_coordinatesMitte())
    return f'{wthr.location}, {wthr.description}\n' \
           f'Temperature is {wthr.temperature}°C, feels like {wthr.temperature_feeling}°C'

def weatherIstanbul() -> str:
    wthr = get_weather(get_coordinatesIstanbul())
    return f'{wthr.location}, {wthr.description}\n' \
           f'Temperature is {wthr.temperature}°C, feels like {wthr.temperature_feeling}°C'

def weatherMoscow() -> str:
    wthr = get_weather(get_coordinatesMoscow())
    return f'{wthr.location}, {wthr.description}\n' \
           f'Temperature is {wthr.temperature}°C, feels like {wthr.temperature_feeling}°C'

def weatherKyiv() -> str:
    wthr = get_weather(get_coordinatesKyiv())
    return f'{wthr.location}, {wthr.description}\n' \
           f'Temperature is {wthr.temperature}°C, feels like {wthr.temperature_feeling}°C'

def weatherNew_York() -> str:
    wthr = get_weather(get_coordinatesNew_York())
    return f'{wthr.location}, {wthr.description}\n' \
           f'Temperature is {wthr.temperature}°C, feels like {wthr.temperature_feeling}°C'

