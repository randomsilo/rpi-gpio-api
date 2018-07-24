from flask import Flask, jsonify
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app)

@app.route('/')
def index():
    return 'Flask is running!'

@app.route('/data')
def names():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(data)

if __name__ == "__main__":
    context = ('ssl.crt', 'ssl.key')
    app.run(host='0.0.0.0', ssl_context=context, threaded=True, debug=False)