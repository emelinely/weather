# weather
code using weather API to replicate weather sounds

## description 
a device that takes weather descriptions from the internet and plays the corresponding sounds by mapping the descriptions to the sound files in order to mimick the outdoors when you're indoors 

### temperature
takes the temperature from openweather api and converts it into celsius

changes the volume of the audio output according to the temperature (warmer is louder and colder is softer)

the current upper temperature limit is 40 degrees celsius

### log
logs the current weather description, temperature and volume in a file called weather.log

## requirements
### built-in
requests allows you to make api calls to openweather api

json allows you to parse the response from openweather api

### external
[simpleaudio](https://pypi.org/project/simpleaudio/) allows you to play sound files

alsaaudio allows you to change the volume of a raspberry pi

scikits.audiolab has not been working, but to install use the following code:
```
sudo apt-get install libasound2-dev
sudo apt-get install libsndfile-dev
sudo pip3 install scikits.audiolab
```

## setup
### openweather api

#### Free plan
Free users can make up to 60 API calls per minute. 

Using the service under Free tier, you can work with the following weather APIs:


### API Key
get your own api key from openweather [here](https://home.openweathermap.org/users/sign_up)

### Raspberry pi
#### Running at boot
You can edit the rc.local file in order to run at boot:

Use sudo nano /etc/rc.local to edit the file, then add sudo python3 /home/pi/weather/main.py just before the exit 0.

This allows the program to run at boot. However, the program might not run forever when using this method. 

Latest version seems to run forever, but more testing is needed.

Because at boot the raspberry pi is not initially connected to the internet, the program will first make sure that it receives data from openweather api before trying to run the code.

##### To stop running process in rc.local at boot
press Alt + PrintScn + k

