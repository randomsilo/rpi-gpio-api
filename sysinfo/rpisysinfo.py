from datetime import datetime
import subprocess
import platform

# System Information Functions
class RpiSysInfo():
    def __init__(self):
        self.sys_data = {"current_time": '',"machine_name": ''}
        self.sys_data['current_time'] = datetime.now().strftime("%d-%b-%Y , %I : %M : %S %p")
        self.sys_data['machine_name'] =  platform.node()
        self.os_name = None
        self.cpu_usage_info = None
        self.cpu_processor_count = None
        self.cpu_core_frequency = None
        self.cpu_core_volt = None
        self.cpu_temperature = None
        self.boot_info = None
        self.memory_usage_info = None
        self.cpu_generic_info = None
        self.disk_usage_info = None

    def get_cpu_data(self):
        self.cpu_usage_info = self.get_cpu_usage_info()
        self.cpu_processor_count = self.get_cpu_processor_count()
        self.cpu_core_frequency = self.get_cpu_core_frequency()
        self.cpu_core_volt = self.get_cpu_core_volt()
        self.cpu_temperature = self.get_cpu_temperature()
        return True
    
    def get_device_data(self):
        self.os_name = self.get_os_name()
        self.boot_info = self.get_boot_info()
        self.memory_usage_info = self.get_memory_usage_info()
        self.cpu_generic_info = self.get_cpu_generic_details()
        self.disk_usage_info = self.get_disk_usage_list()
        return True

    def get_platform_data(self):
        return True


    def get_cpu_generic_details(self):
        try:
            items = [s.split('\t: ') for s in subprocess.check_output(["cat /proc/cpuinfo  | grep 'model name\|Hardware\|Serial' | uniq "], shell=True)
                .decode('utf8')
                .replace('\t', '')
                .splitlines()]
        except Exception as ex:
            print(ex)
        finally:
            return items

    def get_boot_info(self):
        item = {'running_duration': 'Na','start_time':'Na'}
        try:
            item['running_duration'] = subprocess.check_output(['uptime -p'], shell=True)\
                .decode('utf8')\
                .replace('\n', '')
            item['start_time'] = subprocess.check_output(['uptime -s'], shell=True)\
                .decode('utf8')\
                .replace('\n', '')
        except Exception as ex:
            print(ex)
        finally:
            return item

    def get_memory_usage_info(self):
        try:
            item = {'total': 0,'used': 0,'free': 0, 'available': 0 }
            item['total']=  subprocess.check_output(["free -m -t | awk 'NR==2' | awk '{print $2'}"], shell=True)\
                .decode('utf8')\
                .replace('\n', '')
            item['used']=  subprocess.check_output(["free -m -t | awk 'NR==2' | awk '{print $3'}"], shell=True)\
                .decode('utf8')\
                .replace('\n', '')
            item['free']=  subprocess.check_output(["free -m -t | awk 'NR==2' | awk '{print $4'}"], shell=True)\
                .decode('utf8')\
                .replace('\n', '')
            item['free']=  subprocess.check_output(["free -m -t | awk 'NR==2' | awk '{print $7'}"], shell=True)\
                .decode('utf8')\
                .replace('\n', '')
        except Exception as ex:
            print(ex)
        finally:
            return item

    def get_os_name(self):
        os_info = subprocess.check_output("cat /etc/*-release | grep PRETTY_NAME | cut -d= -f2", shell=True)\
            .decode('utf8')\
            .strip()\
            .replace('\"', '')
        return dict(os_name=os_info)

    def get_cpu_usage_info(self):
        item = {'in_use': 0}
        try:
            item['in_use'] = subprocess.check_output("top -b -n2 | grep 'Cpu(s)'|tail -n 1 | awk '{print $2 + $4 }'", shell=True)\
                .decode('utf8')\
                .replace('\n', '')
        except Exception as ex:
            print(ex)
        finally:
            return item

    def get_cpu_processor_count(self):
        proc_info = subprocess.check_output("nproc", shell=True)\
            .decode('utf8')\
            .strip()\
            .replace('\"', '')
        return proc_info

    def get_cpu_core_frequency(self):
        core_frequency = subprocess.check_output("vcgencmd get_config arm_freq | cut -d= -f2", shell=True)\
            .decode('utf8')\
            .strip()\
            .replace('\"', '')
        return core_frequency

    def get_cpu_core_volt(self):
        core_volt = subprocess.check_output("vcgencmd measure_volts| cut -d= -f2", shell=True)\
            .decode('utf8')\
            .strip()\
            .replace('\"', '')
        return core_volt

    def get_cpu_temperature(self):
        cpuInfo = {'temperature': 0, 'color': 'white'}
        try:
            cpuTemp = float(subprocess.check_output(["vcgencmd measure_temp"], shell=True)\
                .decode('utf8')\
                .strip()\
                .split('=')[1].split('\'')[0])
            cpuInfo['temperature']=cpuTemp
            if cpuTemp > 40 and cpuTemp < 50:
                cpuInfo['color'] = 'orange'
            elif cpuTemp > 50:
                cpuInfo['color'] = 'red'
            return cpuInfo
        except Exception as ex:
            print(ex)
        finally:
            return cpuInfo

    def get_disk_usage_list(self):
        items = []
        try:
            items = [s.split() for s in subprocess.check_output(['df', '-h'], shell=True)\
                .decode('utf8')\
                .splitlines()]
        except Exception as ex:
            print(ex)
        finally:
            return items[1:]