# ml-service.py

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/service', methods=['GET'])
def service():
    return jsonify(message="Service is running"), 200

if __name__ == '__main__':
    app.run(port=50022)