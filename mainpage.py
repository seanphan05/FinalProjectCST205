from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from colby_work import weather
# create an instance of Flask
app = Flask(__name__)

bootstrap = Bootstrap5(app)
@app.route('/')
def t_test0():
    return render_template('index.html')

@app.route('/MontereyWeatherBroadcast')
def get_weather():
    data = weather.get_monterey_weather()
    return render_template('weather.html', data=data)

@app.route('/PetAdoption')
def get_pet():
    return render_template('animal.html')