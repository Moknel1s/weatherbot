BOT_API_TOKEN = '5642461865:AAFLp3lKPz8JL6aQl-BTzI2v58IVAgUzKV0'
WEATHER_API_KEY = '04c2411d85305b0be128892aba5219a8'

CURRENT_WEATHER_API_CALL = (
        'https://api.openweathermap.org/data/2.5/weather?'
        'lat={latitude}&lon={longitude}&'
        'appid=' + WEATHER_API_KEY + '&units=metric'
)