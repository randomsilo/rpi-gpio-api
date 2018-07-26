from flask import Flask, render_template, jsonify
from werkzeug import serving
import ssl
import platform

from sysinfo.rpisysinfo import RpiSysInfo

app = Flask(__name__)

# Basic Device
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





# Start Page
@app.route('/')
@app.route('/info')
def index():
    rpi_sys_info = RpiSysInfo()
    rpi_sys_info.refreshAll()

    data = {
        "sys_data": rpi_sys_info.sys_data
        , "os_name": rpi_sys_info.os_name
        , "cpu_usage_info": rpi_sys_info.cpu_usage_info
        , "cpu_processor_count": rpi_sys_info.cpu_processor_count
        , "cpu_core_frequency": rpi_sys_info.cpu_core_frequency
        , "cpu_core_volt": rpi_sys_info.cpu_core_volt
        , "cpu_temperature": rpi_sys_info.cpu_temperature
        , "boot_info": rpi_sys_info.boot_info
        , "memory_usage_info": rpi_sys_info.memory_usage_info
        , "cpu_genric_info": rpi_sys_info.cpu_genric_info
        , "disk_usage_info": rpi_sys_info.disk_usage_info
        , "running_process_info": rpi_sys_info.running_process_info
        , "utility_processor": rpi_sys_info.utility_processor
    }
    return jsonify(data)

# Web Server Setup
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain("ssl.crt", "ssl.key")
serving.run_simple("0.0.0.0", 8000, app, ssl_context=context)