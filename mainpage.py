from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from image_dict import image_dict
import random
import weather
# create an instance of Flask
app = Flask(__name__)

bootstrap = Bootstrap5(app)
@app.route('/')
def t_test0():
    return render_template('index.html')

@app.route('/MontereyWeatherBroadcast')
def get_weather():
    random.shuffle(image_dict)
    data = weather.get_monterey_weather()
    return render_template('weather.html', image_dict=image_dict, filters=filters, data=data)

@app.route('/MontereyWeatherBroadcast/image')
def change_image():
    random.shuffle(image_dict)
    return image_dict[0]

@app.route('/MontereyWeatherBroadcast/update')
def update_info():
    return weather.get_monterey_weather()

# Pet Adoption Routes
@app.route('/PetAdoption')
def get_pet():
    return render_template('animal.html')