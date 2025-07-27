from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, Joian!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
