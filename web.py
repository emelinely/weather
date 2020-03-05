from flask import Flask
app = Flask(__name__)



@app.route('/')
def weather_info():
    weather_info = []
    with open('weather.log', 'r') as f:
        for line in f:
            weather_info.append( line )
    output = "<xmp>" + weather_info[0] + weather_info[1] + weather_info[2] + weather_info[3] + "</xmp>"
    return output


app.run(host='0.0.0.0')
