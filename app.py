from flask import Flask, request
from flask import render_template
import folium
import json

app = Flask(__name__)


#@app.route('/', methods=["GET", "POST"])
@app.route('/')
def index():
#    return render_template("location.html")
#    folium_map = folium.Map(location=[35.028181766844064, 135.76002961368505], zoom_start=17)
#    folium_map.save('templates/map.html')
    return render_template('index.html')

#@app.route('/result', methods=["POST", "GET"])
#def send():
#    data = json.loads(request.data.decode('utf-8'))
#    lat = data["lat"]
#    lon = data["lon"]
#    return '1'

#folium_map = folium.Map(location=[lat, lon], zoom_start=17)
#    folium_map.save('templates/map.html')
 #   return render_template('111.html')

@app.route('/map')
def map():
    return render_template('map.html')


if __name__ == '__main__':
    app.run(debug=True)
