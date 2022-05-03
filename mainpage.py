from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from image_dict import image_dict
import random

# create an instance of Flask
app = Flask(__name__)

bootstrap = Bootstrap5(app)


filters = ['No Filter', 'Negative Filter', 'GrayScale Filter', 'Sepia Filter']
# Main Page Routes
@app.route('/')
def get_homepage():
    return render_template('index.html')


# Weather Broadcast Routes
@app.route('/MontereyWeatherBroadcast')
def get_weather():
    random.shuffle(image_dict)
    return render_template('weather.html', image_dict=image_dict, filters=filters)

@app.route('/MontereyWeatherBroadcast/image')
def change_image():
    random.shuffle(image_dict)
    return image_dict[0]

# Pet Adoption Routes
@app.route('/PetAdoption')
def get_pet():
    return render_template('animal.html')