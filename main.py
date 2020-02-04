import requests, json 
import simpleaudio as sa
import time
import alsaaudio

test_weather_condition = 'light rain'
possible_weather_conditions = ['thunderstorm with light rain', 'thunderstorm with rain	', 'thunderstorm with heavy rain', 'light thunderstorm', 'thunderstorm', 'heavy thunderstorm',  "ragged thunderstorm", 'thunderstorm with light drizzle	', 'thunderstorm with drizzle	', 'thunderstorm with heavy drizzle', 'light intensity drizzle', 'drizzle', 'heavy intensity drizzle', 'light intensity drizzle rain', 'drizzle rain', 'heavy intensity drizzle rain', 'shower rain and drizzle', 'heavy shower rain and drizzle', 'shower drizzle', 'light rain', 'moderate rain', 'heavy intensity rain', 'very heavy rain', 'extreme rain', 'freezing rain', 'light intensity shower rain', 'shower rain', 'heavy intensity shower rain', 'ragged shower rain', 'light snow', 'Snow', 'Heavy snow', 'Sleet', 'Light shower sleet', 'Shower sleet', 'Light rain and snow', 'Rain and snow', 'Light shower snow', 'Shower snow', 'Heavy shower snow', 'mist', 'Smoke', 'haze', 'sand/ dust whirls',  'fog', 'sand', 'dust', 'volcanic ash', 'squalls', 'tornado', 'clear sky', 'few clouds', 'scattered clouds', 'broken clouds', 'overcast clouds'] # all possible to check if description is accurate

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

other_weather_conditions = [ 'Smoke', 'haze', 'sand/ dust whirls',  'sand', 'dust', 'volcanic ash', 'squalls', 'tornado'] 

city = "San Francisco"
complete_url = "http://api.openweathermap.org/data/2.5/weather?appid=a3e304c7b5f418e6e8463db911baabac&q=" + city  
m = alsaaudio.Mixer('PCM')

def convert_temperature(temperature):
  celsius = temperature - 270
  return celsius

def temperature_to_volume(celsius):
  volume = round(50 + celsius*1.25)
  return volume

def play_weather_sound(weather_condition, celsius):
    """plays sound, given weather decription and temperature"""
    m.setvolume(round(volume))
    print("set volume to {}".format( m.getvolume()))
    if weather_condition in possible_weather_conditions:
      if weather_condition in clear_weather_conditions:
        print('Playing CLEAR weather conditions')
        a = "clear.wav"
      elif weather_condition in heavy_rain_weather_conditions:
        print('Playing HEAVY RAIN weather condition')
        a = "heavy_rain.wav"
      elif weather_condition in rain_weather_conditions:
        print('Playing RAIN weather condition')
        a = "rain.wav"
      elif weather_condition in light_rain_weather_conditions:
        print('Playing LIGHT RAIN weather condition')
        a = "light_rain.wav"
      elif weather_condition in light_drizzle_weather_conditions:
        print('Playing LIGHT DRIZZLE weather condition')
        a = "light_drizzle.wav"
      elif weather_condition in drizzle_weather_conditions:
        print('Playing DRIZZLE weather condition')
        a = "drizzle.wav"
      elif weather_condition in heavy_drizzle_weather_conditions:
        print('Playing HEAVY DRIZZLE weather condition')
        a = "heavy_drizzle.wav"
      elif weather_condition in thunderstorm_weather_conditions:
        print('Playing THUNDERSTORM weather condition')
        a = "thunderstorm.wav"
      elif weather_condition in thunderstorm_rain_weather_conditions:
        print('Playing THUNDERSTORM RAIN weather condition')
        a = "thunderstorm_with_rain.wav"
      elif weather_condition in cloudy_weather_conditions:
        print('Playing CLOUDY weather condition')
        a = "cloudy.wav"
      elif weather_condition in snow_weather_conditions:
        print('Playing SNOW weather condition')
        a = "snow.wav"
      elif weather_condition in other_weather_conditions:
        print('Playing OTHER weather condition')
        a = "other.wav"
    else:
      print('This is NOT a possible weather condition')
      
    wave_obj = sa.WaveObject.from_wave_file("/home/pi/weather/sounds/" + a)
    play_obj = wave_obj.play()
    play_obj.wait_done()

while True: 
  try:
    response = requests.get(complete_url) 
  except:
    time.sleep(10)
    continue
  x = response.json() 
  z = x["weather"] 
  temperature = x['main']['temp']
  weather_condition = z[0]["description"] 
  celsius = convert_temperature(temperature)
  volume = temperature_to_volume(celsius)
  print("temperature is {}".format(celsius))
  print(str(weather_condition))
  play_weather_sound(weather_condition, temperature)


  
