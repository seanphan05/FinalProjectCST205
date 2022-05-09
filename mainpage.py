from flask import Flask, render_template, request
from image_dict import image_dict
import random, os , glob
from PIL import Image
import weather
from dereks_work.pet_api_main import get_cat_dog_url_and_prices

# create an instance of Flask
app = Flask(__name__)

bootstrap = Bootstrap5(app)
@app.route('/')
def t_test0():
    return render_template('index.html')

@app.route('/MontereyWeatherBroadcast')
def get_weather():
    return render_template('weather.html')

@app.route('/PetAdoption')
def get_pet():
    return render_template('animal.html', pet_info=get_cat_dog_url_and_prices(5, use_test_data=True))