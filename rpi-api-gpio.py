import ssl
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('ssl.crt', 'ssl.key')

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    context = ('cert.crt', 'key.key')
    app.run(host='0.0.0.0', port=443, ssl_context=context, threaded=True, debug=True)