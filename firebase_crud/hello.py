import firebase_admin
from firebase_admin import db, credentials

# Initialize Firebase
cred = credentials.Certificate("./qr-reader-74e94-firebase-adminsdk-u67ki-373103a3e0.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://qr-reader-74e94-default-rtdb.firebaseio.com/"})

# Create a new user
def create_user(user_id, name, age):
    ref = db.reference(f"/users/{user_id}")
    ref.set({
        'name': name,
        'age': age
    })
    print(f'User {name} created with ID: {user_id}')

# Read user data
def read_user(user_id):
    ref = db.reference(f"/users/{user_id}")
    user_data = ref.get()
    if user_data:
        print(f'User ID: {user_id}, Data: {user_data}')
    else:
        print(f'User ID: {user_id} does not exist.')

# Update user data
def update_user(user_id, name=None, age=None):
    ref = db.reference(f"/users/{user_id}")
    updates = {}
    if name:
        updates['name'] = name
    if age:
        updates['age'] = age
    ref.update(updates)
    print(f'User {user_id} updated.')

# Delete user data
def delete_user(user_id):
    ref = db.reference(f"/users/{user_id}")
    ref.delete()
    print(f'User {user_id} deleted.')

if __name__ == '__main__':
    # Example operations
    create_user('user1', 'John Doe', 30)
    create_user('user2', 'Jane Smith', 25)
    read_user('user1')
    update_user('user1', age=31)
    read_user('user1')
    delete_user('user2')
    read_user('user2')  # Try to read the deleted user
