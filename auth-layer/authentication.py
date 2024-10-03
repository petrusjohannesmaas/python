username = input("Enter your username: ")
password = input("Enter your password: ")

def identification(username, password):
    return {'username' : username, 'password' : password}

database = [
    { 'username': 'piet', 'password': 'testing123' },
    { 'username': 'mercia', 'password': 'demo456' },
    { 'username': 'bob', 'password': 'mocky0192' },
]

def check_credentials(username, password):
    for user in database:
        if user['username'] == username and user['password'] == password:
            return True
    return False

# Check if the provided credentials are correct
if check_credentials(username, password):
    print("Access granted. Here is the data:")
    for user in database:
        print(user)
else:
    print("Access denied. Invalid username or password.")