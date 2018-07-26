from datetime import datetime
import subprocess


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
        self.cpu_genric_info = None
        self.disk_usage_info = None
        self.running_process_info = None
        self.utility_processor = None

    def refreshAll(self):
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
            items = [s.split('\t: ') for s in subprocess.check_output(["cat /proc/cpuinfo  | grep 'model name\|Hardware\|Serial' | uniq "], shell=True).decode('utf8').splitlines()]
        except Exception as ex:
            print(ex)
        finally:
            return items

    def get_boot_info(self):
        item = {'start_time': 'Na','running_since':'Na'}
        try:
            item['running_duration'] = subprocess.check_output(['uptime -p'], shell=True).decode('utf8')
            item['start_time'] = subprocess.check_output(['uptime -s'], shell=True).decode('utf8')
        except Exception as ex:
            print(ex)
        finally:
            return dict(boot_info = item)

    def get_memory_usage_info(self):
        try:
            item = {'total': 0,'used': 0,'available': 0 }
            item['total']=  subprocess.check_output(["free -m -t | awk 'NR==2' | awk '{print $2'}"], shell=True).decode('utf8')
            item['used']=  subprocess.check_output(["free -m -t | awk 'NR==3' | awk '{print $3'}"], shell=True).decode('utf8')
            item['available']= int(item['total'])- int(item['used'])
        except Exception as ex:
            print(ex)
        finally:
            return dict(memory_usage_info = item)

    def get_os_name(self):
        os_info = subprocess.check_output("cat /etc/*-release | grep PRETTY_NAME | cut -d= -f2", shell=True).decode('utf8').strip().replace('\"', '')
        return dict(os_name=os_info)

    def get_cpu_usage_info(self):
        item = {'in_use': 0}
        try:
            item['in_use'] = subprocess.check_output("top -b -n2 | grep 'Cpu(s)'|tail -n 1 | awk '{print $2 + $4 }'", shell=True).decode('utf8')
        except Exception as ex:
            print(ex)
        finally:
            return dict(cpu_usage_info = item)

    def get_cpu_processor_count(self):
        proc_info = subprocess.check_output("nproc", shell=True).decode('utf8').strip().replace('\"', '')
        return dict(cpu_processor_count=proc_info)

    def get_cpu_core_frequency(self):
        core_frequency = subprocess.check_output("vcgencmd get_config arm_freq | cut -d= -f2", shell=True).decode('utf8').strip().replace('\"', '')
        return dict(cpu_core_frequency=core_frequency)

    def get_cpu_core_volt(self):
        core_volt = subprocess.check_output("vcgencmd measure_volts| cut -d= -f2", shell=True).decode('utf8').strip().replace('\"', '')
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
        items = []
        try:
            items = [s.split() for s in subprocess.check_output(['df', '-h'], universal_newlines=True).decode('utf8').splitlines()]
        except Exception as ex:
            print(ex)
        finally:
            return items[1:]

    def get_running_process_list(self):
        items = []
        try:
            items = [s.split() for s in subprocess.check_output(["ps -Ao user,pid,pcpu,pmem,comm,lstart --sort=-pcpu"], shell=True).decode('utf8').splitlines()]
        except Exception as ex:
            print(ex)
        finally:
            return items[1:]

    def get_utility_processor(self):
        def short_date(a,b,c):
            return u'{0}{1}, {2}'.format(a, b,c)
        return dict(short_date=short_date)