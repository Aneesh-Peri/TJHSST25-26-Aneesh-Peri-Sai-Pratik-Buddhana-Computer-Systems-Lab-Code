from flask import Flask, render_template, jsonify

import requests
from datetime import datetime

app = Flask(__name__)

API_KEY = "789f97f14e2340c285993de7df1b568a" 

def get_sun_data():
    location_url = f"https://api.ipgeolocation.io/ipgeo?apiKey={API_KEY}"
    loc_response = requests.get(location_url)
    loc_data = loc_response.json()
    lat = loc_data.get("latitude", 38.9)
    lon = loc_data.get("longitude", -77.05)
    astro_url = f"https://api.ipgeolocation.io/astronomy?apiKey={API_KEY}&lat={lat}&long={lon}"
    astro_response = requests.get(astro_url)
    astro_data = astro_response.json()
    return {
        "latitude": lat,
        "longitude": lon,
        "sun_azimuth": astro_data.get("sun_azimuth", 0),
        "sun_elevation": astro_data.get("sun_altitude", 0),
        "sunrise": astro_data.get("sunrise", "N/A"),
        "sunset": astro_data.get("sunset", "N/A")
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status')
def status():
    sun_data = get_sun_data()
    status_data = {
        "system_status": "Tracking",
        "sun_azimuth": sun_data["sun_azimuth"],
        "sun_elevation": sun_data["sun_elevation"],
        "mirror_azimuth": 130.0,
        "mirror_elevation": 45.0,
        "sunrise": sun_data["sunrise"],
        "sunset": sun_data["sunset"],
        "latitude": sun_data["latitude"],
        "longitude": sun_data["longitude"],
        "last_updated": datetime.now().strftime("%H:%M:%S")
    }
    return jsonify(status_data)

@app.route("/actuator/up")
def actuator_up():
    print("Actuator moving UP 1 inch")
    return jsonify({"status": "up"})


@app.route("/actuator/down")
def actuator_down():
    print("Actuator moving DOWN 1 inch")
    return jsonify({"status": "down"})


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
