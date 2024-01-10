from flask import Flask, jsonify

app = Flask(__name__)

# Define a sample route and endpoint
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message='Hello from Flask!')

# You can add more routes and endpoints as needed

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)