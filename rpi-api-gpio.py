from flask import Flask, jsonify
import os

ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask is running!'

@app.route('/data')
def names():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(data)

if __name__ == "__main__":
    context = ('ssl.crt', 'ssl.key')
    app.run(host='0.0.0.0', ssl_context=context, threaded=True, debug=True)