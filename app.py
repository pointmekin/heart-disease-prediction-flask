from flask import Flask, jsonify, request

app = Flask(__name__)

# Define a simple route
@app.route('/')
def hello():
    return 'Hello, World!'

# Define a route that accepts GET requests and returns JSON data
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'name': 'John Doe',
        'age': 30,
        'occupation': 'Developer'
    }
    return jsonify(data)

# Define a route that accepts POST requests and returns JSON data
@app.route('/api/submit', methods=['POST'])
def submit_data():
    # Assuming the request body is in JSON format
    data = request.get_json()
    # Process the data...

    # Return a response
    response = {
        'message': 'Data submitted successfully',
        'data': data
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)