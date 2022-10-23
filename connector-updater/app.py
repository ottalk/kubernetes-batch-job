from flask import Flask,request,jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

@app.route('/get_config', methods=['GET']) 
def get_config():
    return "CONFIG"

@app.route('/post_config', methods=['POST']) 
def post_config():
    data = request.json
    return jsonify(data)

@app.route('/put_config', methods=['PUT']) 
def put_config():
    data = request.json
    return jsonify(data)