from flask import Flask, jsonify, render_template
import firebase_admin
from firebase_admin import db, credentials

# Initialize Firebase
cred = credentials.Certificate("./qr-reader-74e94-firebase-adminsdk-u67ki-373103a3e0.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://qr-reader-74e94-default-rtdb.firebaseio.com/"})

app = Flask(__name__)

# Serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')  # Serve the HTML file

# Fetch temperature data from Firebase
@app.route('/temperature')
def get_temperature():
    ref = db.reference('/temperature')  # Reference the path where temperature is stored
    temperature_data = ref.get()  # Fetch the data

    if temperature_data:
        temperature = temperature_data.get('temperature', None)
        print(temperature)
        if temperature:
            return jsonify({'temperature': round(temperature, 2)})
        else:
            return jsonify({'error': 'Temperature data not available'}), 404
    else:
        return jsonify({'error': 'Unable to fetch temperature data'}), 500

if __name__ == '__main__':
    app.run(debug=True)
