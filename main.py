import requests, json 
  
test_weather_condition = 'light rain'
possible_weather_conditions = ['thunderstorm with light rain', 'thunderstorm with rain	', 'thunderstorm with heavy rain', 'light thunderstorm', 'thunderstorm', 'heavy thunderstorm',  "ragged thunderstorm", 'thunderstorm with light drizzle	', 'thunderstorm with drizzle	', 'thunderstorm with heavy drizzle', 'light intensity drizzle', 'drizzle', 'heavy intensity drizzle', 'light intensity drizzle rain', 'drizzle rain', 'heavy intensity drizzle rain', 'shower rain and drizzle', 'heavy shower rain and drizzle', 'shower drizzle', 'light rain', 'moderate rain', 'heavy intensity rain', 'very heavy rain', 'extreme rain', 'freezing rain', 'light intensity shower rain', 'shower rain', 'heavy intensity shower rain', 'ragged shower rain', 'light snow', 'Snow', 'Heavy snow', 'Sleet', 'Light shower sleet', 'Shower sleet', 'Light rain and snow', 'Rain and snow', 'Light shower snow', 'Shower snow', 'Heavy shower snow', 'mist', 'Smoke', 'Haze', 'sand/ dust whirls',  'fog', 'sand', 'dust', 'volcanic ash', 'squalls', 'tornado', 'clear sky', 'few clouds', 'scattered clouds', 'broken clouds', 'overcast clouds'] # all possible to check if description is accurate

clear_weather_conditions = ['clear sky', 'few clouds', 'scattered clouds'] 

heavy_rain_weather_conditions = ['heavy intensity rain', 'very heavy rain', 'extreme rain', 'freezing rain', 'heavy intensity shower rain', 'ragged shower rain'] 
rain_weather_conditions = [ 'moderate rain', 'shower rain']
light_rain_weather_conditions = ['light intensity shower rain', 'light rain']

light_drizzle_weather_conditions = ['light intensity drizzle', 'light intensity drizzle rain']
drizzle_weather_conditions = ['drizzle', 'drizzle rain', 'shower rain and drizzle', 'shower drizzle', ]
heavy_drizzle_weather_conditions = ['heavy intensity drizzle', 'heavy shower rain and drizzle', 'heavy intensity drizzle rain']

thunderstorm_weather_conditions = ['light thunderstorm', 'thunderstorm', 'heavy thunderstorm',  "ragged thunderstorm"]
thunderstorm_rain_weather_conditions = ['thunderstorm with light rain', 'thunderstorm with rain	', 'thunderstorm with heavy rain', 'thunderstorm with light drizzle	', 'thunderstorm with drizzle	', 'thunderstorm with heavy drizzle']

cloudy_weather_conditions = ['broken clouds', 'overcast clouds', 'fog', 'mist',]

snow_weather_conditions = ['light snow', 'Snow', 'Heavy snow', 'Sleet', 'Light shower sleet', 'Shower sleet', 'Light rain and snow', 'Rain and snow', 'Light shower snow', 'Shower snow', 'Heavy shower snow']

other_weather_conditions = [ 'Smoke', 'Haze', 'sand/ dust whirls',  'sand', 'dust', 'volcanic ash', 'squalls', 'tornado'] 
  
complete_url = "http://api.openweathermap.org/data/2.5/weather?appid=a3e304c7b5f418e6e8463db911baabac&q=San Francisco"
  
# get method of requests module 
# return response object 
response = requests.get(complete_url) 
  
# json method of response object  
# convert json format data into 
# python format data 
x = response.json() 

  
# store the value of "weather" 
# key in variable z 
z = x["weather"] 
  
# store the value corresponding  
# to the "description" key at  
# the 0th index of z 
test_weather_condition = z[0]["description"] 
  
# print following value
print(str(test_weather_condition)) 


if test_weather_condition in possible_weather_conditions:
  if test_weather_condition in clear_weather_conditions:
    print('Playing CLEAR weather conditions')
    a = "clear.wav"
  elif test_weather_condition in heavy_rain_weather_conditions:
    print('Playing HEAVY RAIN weather condition')
    a = "heavy_rain.wav"
  elif test_weather_condition in rain_weather_conditions:
    print('Playing RAIN weather condition')
    a = "rain.wav"
  elif test_weather_condition in light_rain_weather_conditions:
    print('Playing LIGHT RAIN weather condition')
    a = "light_rain.wav"
  elif test_weather_condition in light_drizzle_weather_conditions:
    print('Playing LIGHT DRIZZLE weather condition')
    a = "light_drizzle.wav"
  elif test_weather_condition in drizzle_weather_conditions:
    print('Playing DRIZZLE weather condition')
    a = "drizzle.wav"
  elif test_weather_condition in heavy_drizzle_weather_conditions:
    print('Playing HEAVY DRIZZLE weather condition')
    a = "heavy_drizzle.wav"
  elif test_weather_condition in thunderstorm_weather_conditions:
    print('Playing THUNDERSTORM weather condition')
    a = "thunderstorm.wav"
  elif test_weather_condition in thunderstorm_rain_weather_conditions:
    print('Playing THUNDERSTORM RAIN weather condition')
    a = "thunderstorm_with_rain.wav"
  elif test_weather_condition in cloudy_weather_conditions:
    print('Playing CLOUDY weather condition')
    a = "cloudy.wav"
  elif test_weather_condition in snow_weather_conditions:
    print('Playing SNOW weather condition')
    a = "snow.wav"
  elif test_weather_condition in other_weather_conditions:
    print('Playing OTHER weather condition')
    a = "other.wav"
else:
  print('This is NOT a possible weather condition')
