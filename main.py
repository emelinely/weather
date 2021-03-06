import requests, json 
import simpleaudio as sa
import time
import alsaaudio

test_weather_condition = 'light rain'
possible_weather_conditions = ['thunderstorm with light rain', 'thunderstorm with rain	', 'thunderstorm with heavy rain', 'light thunderstorm', 'thunderstorm', 'heavy thunderstorm',  "ragged thunderstorm", 'thunderstorm with light drizzle	', 'thunderstorm with drizzle	', 'thunderstorm with heavy drizzle', 'light intensity drizzle', 'drizzle', 'heavy intensity drizzle', 'light intensity drizzle rain', 'drizzle rain', 'heavy intensity drizzle rain', 'shower rain and drizzle', 'heavy shower rain and drizzle', 'shower drizzle', 'light rain', 'moderate rain', 'heavy intensity rain', 'very heavy rain', 'extreme rain', 'freezing rain', 'light intensity shower rain', 'shower rain', 'heavy intensity shower rain', 'ragged shower rain', 'light snow', 'Snow', 'Heavy snow', 'Sleet', 'Light shower sleet', 'Shower sleet', 'Light rain and snow', 'Rain and snow', 'Light shower snow', 'Shower snow', 'Heavy shower snow', 'mist', 'Smoke', 'haze', 'sand/ dust whirls',  'fog', 'sand', 'dust', 'volcanic ash', 'squalls', 'tornado', 'clear sky', 'few clouds', 'scattered clouds', 'broken clouds', 'overcast clouds'] 

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
  """converts temperature from kelvin into celsius"""
  celsius = temperature - 270
  return celsius

def temperature_to_volume(celsius, a):
  """sets volume, if weather is clear, volume is lower"""
  if a == "clear.wav":
    volume = round(50 + celsius*1.25)
  else:
    volume = round(50 + celsius*1.50)
  if volume > 100:
    volume = 100
  m.setvolume(round(volume))
  print("set volume to {}".format( m.getvolume()))
  return volume
  
def wind_speed_to_km(wind_speed):
  """converts wind speed into km"""
  wind_speed_km = round(wind_speed*3.6)
  return wind_speed_km

def play_sounds(wind_speed_km, a):
  """plays weather sound, and wind if wind speed is high enough"""
  if wind_speed_km <= 19:
    play(a)
  elif wind_speed_km > 19 and wind_speed_km <= 38:
    play(a)
  elif wind_speed_km >38 and wind_speed_km <=61:
    b = "wind1.wav"
    play2(a, b)
  elif wind_speed_km >61 and wind_speed_km <=88:
    b = "wind2.wav"
    play2(a, b)
  elif wind_speed_km >88 and wind_speed_km <=117:
    b = "wind3.wav"
    play2(a, b)
  elif wind_speed_km >117:
    b = "wind4.wav"
    play2(a, b)

def find_weather_sound(weather_condition):
    """finds sound to play, given weather decription"""
    if weather_condition in possible_weather_conditions:
      if weather_condition in clear_weather_conditions:
        print('Playing CLEAR weather conditions:')
        a = "clear.wav"
      elif weather_condition in heavy_rain_weather_conditions:
        print('Playing HEAVY RAIN weather conditions:')
        a = "heavy_rain.wav"
      elif weather_condition in rain_weather_conditions:
        print('Playing RAIN weather conditions:')
        a = "rain.wav"
      elif weather_condition in light_rain_weather_conditions:
        print('Playing LIGHT RAIN weather conditions:')
        a = "light_rain.wav"
      elif weather_condition in light_drizzle_weather_conditions:
        print('Playing LIGHT DRIZZLE weather conditions:')
        a = "light_drizzle.wav"
      elif weather_condition in drizzle_weather_conditions:
        print('Playing DRIZZLE weather conditions:')
        a = "drizzle.wav"
      elif weather_condition in heavy_drizzle_weather_conditions:
        print('Playing HEAVY DRIZZLE weather conditions:')
        a = "heavy_drizzle.wav"
      elif weather_condition in thunderstorm_weather_conditions:
        print('Playing THUNDERSTORM weather conditions:')
        a = "thunderstorm.wav"
      elif weather_condition in thunderstorm_rain_weather_conditions:
        print('Playing THUNDERSTORM RAIN weather conditions:')
        a = "thunderstorm_with_rain.wav"
      elif weather_condition in cloudy_weather_conditions:
        print('Playing CLOUDY weather conditions:')
        a = "cloudy.wav"
      elif weather_condition in snow_weather_conditions:
        print('Playing SNOW weather conditions:')
        a = "snow.wav"
      elif weather_condition in other_weather_conditions:
        print('Playing OTHER weather conditions:')
        a = "other.wav"
    else:
      print('This is NOT a possible weather condition')
    return a

def play(a):
  """play a single wav file"""
  wave_obj = sa.WaveObject.from_wave_file("/home/pi/weather/sounds/" + a)
  play_obj = wave_obj.play()
  play_obj.wait_done()

def play2(a,b):
  """play 2 wav files"""
  wav_obja = sa.WaveObject.from_wave_file("/home/pi/weather/sounds/" + a)
  wav_objb = sa.WaveObject.from_wave_file("/home/pi/weather/sounds/" + b)
  play_obja = wav_obja.play()
  play_objb = wav_objb.play()
  play_obja.wait_done()
  play_objb.wait_done()


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
  wind_speed = x["wind"]["speed"]
  a = find_weather_sound(weather_condition)
  celsius = convert_temperature(temperature)
  volume = temperature_to_volume(celsius, a)
  wind_speed_km = wind_speed_to_km(wind_speed)
  with open('weather.log', 'w') as writer:
    writer.write('{}\n'.format(weather_condition))
    writer.write('temperature is {} degrees celsius\n'.format(celsius))
    writer.write('playing at volume {}\n'.format(volume))
    writer.write('wind speed is {}'.format(wind_speed_km))
  print("temperature is {:.2f}°C".format(celsius))
  print(str(weather_condition))
  print("wind speed is {} km/h".format(str(wind_speed_km)))
  play_sounds(wind_speed_km, a)
  print(a)

  
