from flask import Flask, render_template, request
import requests

app = Flask(__name__)


# @app.route('/temperature', methods=['POST'])
# def temprature():
#    return render_template('temperature.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/temperature', methods=['POST'])
def temperature():
    zipcode = request.form['zip']
    r = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',in&appid=079d479eb234001a23f2a18c3847ed84')
    json_object = r.json()
    temp_k = float(json_object['main']['temp'])
    city_name = json_object['name']
    visibility = json_object['visibility']
    temp_c = temp_k - 273.15
    # , atmosphere=atmosphere1)
    return render_template('temperature.html', temp=temp_c, city=city_name, visibility=visibility)


if __name__ == '__main__':
    app.run(debug=True)
