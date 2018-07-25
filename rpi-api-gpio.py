from flask import Flask, jsonify
from werkzeug import serving
import ssl

app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask is running!'

@app.route('/data')
def names():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(data)

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain("ssl.crt", "ssl.key")
serving.run_simple("0.0.0.0", 8000, app, ssl_context=context)