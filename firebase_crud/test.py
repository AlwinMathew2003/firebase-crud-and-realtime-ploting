import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("./qr-reader-74e94-firebase-adminsdk-u67ki-373103a3e0.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

username = input("Enter username: ")
seat_number = int(input("Enter seat number: "))

def getUser(username,seat_number):

    users_ref = db.collection('users')
    query = users_ref.where('name', '==', username).where('seat_number', '==', seat_number)
    results = query.get()

    # Check if any user matches the query
    if results:

        print("User found.")
        print(results[0].to_dict())
    else:
        print("User not found.")
getUser(username,seat_number)