from flask import Flask, render_template, jsonify
from werkzeug import serving
import ssl

from sysinfo.rpisysinfo import RpiSysInfo

app = Flask(__name__)


# CPU
@app.route('/cpu')
def cpu():
    rpi_sys_info = RpiSysInfo()
    rpi_sys_info.get_cpu_data()


    data = {
        "cpu_usage_info": rpi_sys_info.cpu_usage_info
        , "cpu_processor_count": rpi_sys_info.cpu_processor_count
        , "cpu_core_frequency": rpi_sys_info.cpu_core_frequency
        , "cpu_core_volt": rpi_sys_info.cpu_core_volt
        , "cpu_temperature": rpi_sys_info.cpu_temperature
        , "cpu_generic_info": rpi_sys_info.cpu_generic_info
    }
    return jsonify(data)

# Platform
@app.route('/platform')
def platform():
    rpi_sys_info = RpiSysInfo()
    rpi_sys_info.get_platform_data()

    data = {
        "platform.machine": platform.machine()
        , "platform.version": platform.version()
        , "platform.uname": platform.uname()
        , "platform.system": platform.system()
    }
    return jsonify(data)


# Device
@app.route('/device')
def device():
    rpi_sys_info = RpiSysInfo()
    rpi_sys_info.get_device_data()

    data = {
        "os_name": rpi_sys_info.os_name
        , "sys_data": rpi_sys_info.sys_data
        , "boot_info": rpi_sys_info.boot_info
        , "memory_usage_info": rpi_sys_info.memory_usage_info
        , "disk_usage_info": rpi_sys_info.disk_usage_info
    }
    return jsonify(data)

# Web Server Setup
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain("ssl.crt", "ssl.key")
serving.run_simple("0.0.0.0", 8000, app, ssl_context=context)