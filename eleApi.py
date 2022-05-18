#Course: CST 205
#Title: Elephan API
#Abstract: Flask Application using Elephant API
#Date: 05/18/2022
from flask import Flask, render_template, jsonify
import requests,json
from requests import Request, Session
from pprint import pprint


#Flask Application 
app = Flask(__name__)


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

if __name__ == '__main__':
    app.run(debug = True)
 
 








