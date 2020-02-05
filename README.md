# weather
code using weather API to replicate weather sounds

## description 
a device that takes weather descriptions from the internet and plays the corresponding sounds by mapping the descriptions to the sound files in order to mimick the outdoors when you're indoors 



## requirements
### built-in
requests allows you to make api calls to openweather api

json allows you to parse the response from openweather api

### external
[simpleaudio](https://pypi.org/project/simpleaudio/) allows you to play sound files

alsaaudio allows you to change the volume of a raspberry pi

## setup
### openweather api

#### Free plan
Free users can make up to 60 API calls per minute. 

Using the service under Free tier, you can work with the following weather APIs:


### API Key
get your own api key from openweather [here](https://home.openweathermap.org/users/sign_up)`

### Raspberry pi
#### Running at boot
You can edit the rc.local file in order to run at boot:

Use sudo nano /etc/rc.local to edit the file, then add sudo python3 /home/pi/weather/main.py just before the exit 0.

This allows the program to run at boot. However, the program might not run forever when using this method. 

Laatest version seems to run forever, but more testing is needed.
##### To stop running process in rc.local at boot
press Alt + PrintScn + k
