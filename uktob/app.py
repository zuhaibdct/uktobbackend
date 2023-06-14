from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}  # Dictionary to store registered users (as a stand-in for a real database)

@app.route('/api/register', methods=['POST'])
def register_user():
    """
    Registers a new user with a username and password.
    Expects a JSON payload with 'username' and 'password' fields.
    Returns a JSON response with a success message or an error message if registration fails.
    """
    data = request.get_json()  # Get the JSON data from the request body
    username = data.get('username', '')
    password = data.get('password', '')
    
    if not username or not password:
        return jsonify(error='Both username and password are required'), 400
    
    if username in users:
        return jsonify(error='Username already exists'), 400
    
    users[username] = password
    return jsonify(message='Registration successful')

@app.route('/api/login', methods=['POST'])
def login_user():
    """
    Logs in a user with a username and password.
    Expects a JSON payload with 'username' and 'password' fields.
    Returns a JSON response with an access granted message or an access denied message.
    """
    data = request.get_json()  # Get the JSON data from the request body
    username = data.get('username', '')
    password = data.get('password', '')
    
    if not username or not password:
        return jsonify(error='Both username and password are required'), 400
    
    if username in users and users[username] == password:
        return jsonify(message='Access granted')
    else:
        return jsonify(error='Access denied')

@app.route('/api/sum', methods=['POST'])
def calculate_sum():
    """
    Calculates the sum of a list of numbers.
    Expects a JSON payload with a 'numbers' field containing an array of numbers.
    Returns a JSON response with the sum of the numbers or an error message if invalid input is provided.
    """
    data = request.get_json()  # Get the JSON data from the request body
    numbers = data.get('numbers', [])  # Extract the 'numbers' array from the JSON data
    
    if not numbers:
        return jsonify(error='No numbers provided'), 400
    
    try:
        total_sum = sum(numbers)
        return jsonify(sum=total_sum)
    except TypeError:
        return jsonify(error='Invalid numbers provided'), 400
    
@app.route('/api/concatenate', methods=['POST'])
def concatenate_strings():
    """
    Concatenates two strings.
    Expects a JSON payload with 'string1' and 'string2' fields.
    Returns a JSON response with the concatenated string or an error message if either string is missing.
    """
    data = request.get_json()  # Get the JSON data from the request body
    string1 = data.get('string1', '')  # Extract the first string from the JSON data
    string2 = data.get('string2', '')  # Extract the second string from the JSON data

    if not string1 or not string2:
        return jsonify(error='Both strings are required'), 400
    
    concatenated_string = string1 + string2
    return jsonify(concatenated_string=concatenated_string)

if __name__ == '__main__':
    app.run(debug=True)
