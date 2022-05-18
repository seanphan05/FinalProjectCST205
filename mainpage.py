#######################################################
"""
Course: CST 205 Multimedia Design & Programming

Title: Web Application to Broadcast Monterey Weather and Traffic Condition, Webpage for Pet Adoption

Author:
Trung Phan
Derek Lilienthal
Colby Medeiros
Liliana Valencia

Date: Apr 27 2022

Responsibility
Trung Phan:
- Web application mockup design
- Web application front-end development (Weather Broadcast Page and Pet Adoption Page)
- Weather Broadcast Traffic API, Image Filters, Button functions
- Project Document
Derek Lilienthal:
- Pet API, Pet adoption page developement
- Crypto currency API
Colby Medeiros:
- Weather Broadcast API
Liliana Valencia
- Elephant API and Page

Source:
- http://dev.virtualearth.net
- http://api.openweathermap.org
- https://api.coinstats.app
- https://dog.ceo
- https://api.thecatapi.com
- https://elephant-api.herokuapp.com
- Google Images and wikipedia
"""
#######################################################

from flask import Flask, render_template, request
from image_dict import image_dict
import random, os , glob
from PIL import Image
import weather
from flask import Flask, render_template
import requests,json
from requests import Request, Session
from dereks_work.pet_api_main import get_cat_dog_url_and_prices


# create an instance of Flask
app = Flask(__name__)

filters = ['No Filter', 'Negative Filter', 'GrayScale Filter', 'Sepia Filter']
current_image = ''
# Main Page Routes
@app.route('/')
def get_homepage():
    return render_template('index.html')


# Weather Broadcast Routes
@app.route('/MontereyWeatherBroadcast')
def get_weather():
    random.shuffle(image_dict)
    global current_image
    current_image = image_dict[0]["Name"]
    data = weather.get_monterey_info()
    return render_template('weather.html', image_dict=image_dict, filters=filters, data=data)

@app.route('/MontereyWeatherBroadcast/image')
def change_image():
    random.shuffle(image_dict)
    global current_image
    current_image = image_dict[0]["Name"]
    return image_dict[0]

@app.route('/MontereyWeatherBroadcast/filter', methods=['POST'])
def apply_filter():
    # clean old data
    filter_list = ['grayscale', 'sepia', 'negative']
    for path in glob.glob("static/images/*.jpg"):
        if any(filter in path for filter in filter_list):
            os.remove(path)

    # get data from POST request
    data = request.get_json()
    name = current_image
    image_path = "static/images/" + name + ".jpg"
    filter = data['Filter']

    if filter == 'Sepia Filter':
        org_image = Image.open(image_path)
        image = Image.new('RGB', (org_image.width, org_image.height))
        for x in range(image.width):
            for y in range(image.height):
                p = org_image.getpixel((x, y))
                tr = int(0.393 * p[0] + 0.769 * p[1] + 0.189 * p[2])
                tg = int(0.349 * p[0] + 0.686 * p[1] + 0.168 * p[2])
                tb = int(0.272 * p[0] + 0.534 * p[1] + 0.131 * p[2])
                sep_pixel = (255 if tr > 255 else tr, 255 if tg > 255 else tg, 255 if tb > 255 else tb)
                image.putpixel((x, y), sep_pixel)
        new_path = 'static/images/' + name + '-sepia' + '.jpg'
        image.save(new_path)

    elif filter == 'GrayScale Filter':
        image = Image.open(image_path).convert('L')
        new_path = 'static/images/' + name + '-grayscale' + '.jpg'
        image.save(new_path)
    elif filter == 'Negative Filter':
        image = Image.open(image_path)
        neg = [((255 - p[0]), (255 - p[1]), (255 - p[2])) for p in image.getdata()]
        image.putdata(list(neg))
        new_path = 'static/images/' + name + '-negative' + '.jpg'
        image.save(new_path)
    else:
        new_path = image_path
    return new_path
    
@app.route('/MontereyWeatherBroadcast/update')
def update_info():
    return weather.get_monterey_info()

# Pet Adoption Routes
@app.route('/PetAdoption')
def get_pet():
    return render_template('animal.html', pet_info=get_cat_dog_url_and_prices(5, use_test_data=False))


#Flask App
@app.route('/elephant', methods=['GET'])
def hello():
    endpoint = 'https://elephant-api.herokuapp.com/elephants'
    r = requests.get(endpoint)
    eleData= json.loads(r.content)
    elejson = r.json()
#dictionary
    dict = {       

        'name': elejson[1]['name'],
        'Image': elejson[1]['image'],  
        'species': elejson[1]['species'],
        'sex': elejson[1]['sex'],
        'DOB': elejson[1]['dob'],
        'DOD': elejson[1]['dod'],
        'notes': elejson[1]['note'],
        'name1': elejson[5]['name'],
        'Image1': elejson[5]['image'],  
        'species1': elejson[5]['species'],
        'sex1': elejson[5]['sex'],
        'DOB1': elejson[5]['dob'],
        'DOD1': elejson[5]['dod'],
        'notes1': elejson[5]['note'],
        'name2': elejson[3]['name'],
        'Image2': elejson[3]['image'],  
        'species2': elejson[3]['species'],
        'sex2': elejson[3]['sex'],
        'DOB2': elejson[3]['dob'],
        'DOD2': elejson[3]['dod'],
        'notes2': elejson[3]['note'],
        'name3': elejson[6]['name'],
        'Image3': elejson[6]['image'],  
        'species3': elejson[6]['species'],
        'sex3': elejson[6]['sex'],
        'DOB3': elejson[6]['dob'],
        'DOD3': elejson[6]['dod'],
        'notes3': elejson[6]['note'],
        'name4': elejson[7]['name'],
        'Image4': elejson[7]['image'],  
        'species4': elejson[7]['species'],
        'sex4': elejson[7]['sex'],
        'DOB4': elejson[7]['dob'],
        'DOD4': elejson[7]['dod'],
        'name5': elejson[8]['name'],
        'Image5': elejson[8]['image'],  
        'species5': elejson[8]['species'],
        'sex5': elejson[8]['sex'],
        'DOB5': elejson[8]['dob'],
        'DOD5': elejson[8]['dod']
        
    }
    return render_template('layout.html', dict= dict)