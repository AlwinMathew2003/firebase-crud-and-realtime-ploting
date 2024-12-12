import firebase_admin
from firebase_admin import db, credentials
import random
import time

# Initialize Firebase Admin SDK with your credentials
cred = credentials.Certificate("./qr-reader-74e94-firebase-adminsdk-u67ki-373103a3e0.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://qr-reader-74e94-default-rtdb.firebaseio.com/'
})

# Function to generate a random temperature
def generate_random_temperature():
    # Simulating temperature in the range of 15 to 30 degrees Celsius
    return round(random.uniform(15.0, 30.0), 2)

# Function to continuously update temperature in Firebase
def update_temperature():
    while True:
        temperature = generate_random_temperature()
        ref = db.reference('/temperature')  # The path where temperature data will be stored
        ref.set({'temperature': temperature})  # Update temperature value in Firebase

        print(f"Updated temperature: {temperature}°C")

        time.sleep(2)  # Wait for 10 seconds before updating again

if __name__ == '__main__':
    update_temperature()  # Call the function to start updating the temperature
