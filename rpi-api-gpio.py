from flask import Flask, render_template, jsonify
from werkzeug import serving
import ssl
import platform
import subprocess


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


# System Information Functions
class SystemInformation():
    def __init__(self):
        self.sys_data = {"current_time": '',"machine_name": ''}
        self.sys_data['current_time'] = datetime.now().strftime("%d-%b-%Y , %I : %M : %S %p")
        self.sys_data['machine_name'] =  platform.node()
        self.os_name = self.get_os_name()
        self.cpu_usage_info = self.get_cpu_usage_info()
        self.cpu_processor_count = self.get_cpu_processor_count()
        self.cpu_core_frequency = self.get_cpu_core_frequency()
        self.cpu_core_volt = self.get_cpu_core_volt()
        self.cpu_temperature = self.get_cpu_temperature()
        self.boot_info = self.get_boot_info()
        self.memory_usage_info = self.get_memory_usage_info()
        self.cpu_genric_info = self.get_cpu_generic_details()
        self.disk_usage_info = self.get_disk_usage_list()
        self.running_process_info = self.get_running_process_list()
        self.utility_processor = self.get_utility_processor()

    def get_cpu_generic_details(self):
        try:
            items = [s.split('\t: ') for s in subprocess.check_output(["cat /proc/cpuinfo  | grep 'model name\|Hardware\|Serial' | uniq "], shell=True).splitlines()]
        except Exception as ex:
            print(ex)
        finally:
            return items

    def get_boot_info(self):
        item = {'start_time': 'Na','running_since':'Na'}
        try:
            item['running_duration'] = subprocess.check_output(['uptime -p'], shell=True)
            item['start_time'] = subprocess.check_output(['uptime -s'], shell=True)
        except Exception as ex:
            print(ex)
        finally:
            return dict(boot_info = item)

    def get_memory_usage_info(self):
        try:
            item = {'total': 0,'used': 0,'available': 0 }
            item['total']=  subprocess.check_output(["free -m -t | awk 'NR==2' | awk '{print $2'}"], shell=True)
            item['used']=  subprocess.check_output(["free -m -t | awk 'NR==3' | awk '{print $3'}"], shell=True)
            item['available']= int(item['total'])- int(item['used'])
        except Exception as ex:
            print(ex)
        finally:
            return dict(memory_usage_info = item)

    def get_os_name(self):
        os_info = subprocess.check_output("cat /etc/*-release | grep PRETTY_NAME | cut -d= -f2", shell=True).replace('\"', '')
        return dict(os_name=os_info)

    def get_cpu_usage_info(self):
        item = {'in_use': 0}
        try:
            item['in_use'] = subprocess.check_output("top -b -n2 | grep 'Cpu(s)'|tail -n 1 | awk '{print $2 + $4 }'", shell=True)
        except Exception as ex:
            print(ex)
        finally:
            return dict(cpu_usage_info = item)

    def get_cpu_processor_count(self):
        proc_info = subprocess.check_output("nproc", shell=True).replace('\"', '')
        return dict(cpu_processor_count=proc_info)

    def get_cpu_core_frequency(self):
        core_frequency = subprocess.check_output("vcgencmd get_config arm_freq | cut -d= -f2", shell=True).replace('\"', '')
        return dict(cpu_core_frequency=core_frequency)

    def get_cpu_core_volt(self):
        core_volt = subprocess.check_output("vcgencmd measure_volts| cut -d= -f2", shell=True).replace('\"', '')
        return dict(cpu_core_volt=core_volt)

    def get_cpu_temperature(self):
        cpuInfo = {'temperature': 0, 'color': 'white'}
        try:
            cpuTemp = float(subprocess.check_output(["vcgencmd measure_temp"], shell=True).split('=')[1].split('\'')[0])
            cpuInfo['temperature']=cpuTemp
            if cpuTemp > 40 and cpuTemp < 50:
                cpuInfo['color'] = 'orange'
            elif cpuTemp > 50:
                cpuInfo['color'] = 'red'
            return cpuInfo
        except Exception as ex:
            print(ex)
        finally:
            return dict(cpu_temperature=cpuInfo)

    def get_disk_usage_list(self):
        try:
            items = [s.split() for s in subprocess.check_output(['df', '-h'], universal_newlines=True).splitlines()]
        except Exception as ex:
            print(ex)
        finally:
            return items[1:]

    def get_running_process_list(self):
        try:
            items = [s.split() for s in subprocess.check_output(["ps -Ao user,pid,pcpu,pmem,comm,lstart --sort=-pcpu"], shell=True).splitlines()]
        except Exception as ex:
            print(ex)
        finally:
            return items[1:]

    def get_utility_processor(self):
        def short_date(a,b,c):
            return u'{0}{1}, {2}'.format(a, b,c)
        return dict(short_date=short_date)


# Start Page
@app.route('/')
@app.route('/info')
def index():
    sys_info = SystemInformation()
    data = {
        "sys_data": sys_info.sys_data
        , "os_name": sys_info.os_name
        , "cpu_usage_info": sys_info.cpu_usage_info
        , "cpu_processor_count": sys_info.cpu_processor_count
        , "cpu_core_frequency": sys_info.cpu_core_frequency
        , "cpu_core_volt": sys_info.cpu_core_volt
        , "cpu_temperature": sys_info.cpu_temperature
        , "boot_info": sys_info.boot_info
        , "memory_usage_info": sys_info.memory_usage_info
        , "cpu_genric_info": sys_info.cpu_genric_info
        , "disk_usage_info": sys_info.disk_usage_info
        , "running_process_info": sys_info.running_process_info
        , "utility_processor": sys_info.utility_processor
    }
    return jsonify(data)

# Web Server Setup
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain("ssl.crt", "ssl.key")
serving.run_simple("0.0.0.0", 8000, app, ssl_context=context)