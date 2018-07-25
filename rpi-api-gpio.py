from flask import Flask, jsonify
from werkzeug import serving
import ssl
import platform

app = Flask(__name__)

@app.route('/')
def index():
    return 'rpi-api-gpio is active.'

@app.route('/device')
def names():
    data = {
        "platform.machine": platform.machine()
        , "platform.version": platform.version()
        , "platform.uname": platform.uname()
        , "platform.system": platform.system()
        , "platform.processor": platform.processor()
    }
    return jsonify(data)

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain("ssl.crt", "ssl.key")
serving.run_simple("0.0.0.0", 8000, app, ssl_context=context)