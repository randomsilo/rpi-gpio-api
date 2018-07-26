import unittest

from sysinfo.rpisysinfo import RpiSysInfo

class RpiSysInfoTestSuite(unittest.TestCase):
    """First test cases."""

    def test_unittest_setup(self):
        assert True

    def test_simple(self):
        rpi_sys_info = RpiSysInfo()
        
        print("\n=== %s === \n%s" % ("os_name", rpi_sys_info.get_os_name() ))
        print("\n=== %s === \n%s" % ("cpu_usage_info", rpi_sys_info.get_cpu_usage_info() ))
        print("\n=== %s === \n%s" % ("cpu_processor_count", rpi_sys_info.get_cpu_processor_count() ))
        print("\n=== %s === \n%s" % ("cpu_core_frequency", rpi_sys_info.get_cpu_core_frequency() ))
        print("\n=== %s === \n%s" % ("cpu_core_volt", rpi_sys_info.get_cpu_core_volt() ))
        print("\n=== %s === \n%s" % ("cpu_temperature", rpi_sys_info.get_cpu_temperature() ))
        print("\n=== %s === \n%s" % ("boot_info", rpi_sys_info.get_boot_info() ))
        print("\n=== %s === \n%s" % ("memory_usage_info", rpi_sys_info.get_memory_usage_info() ))
        print("\n=== %s === \n%s" % ("cpu_generic_info", rpi_sys_info.get_cpu_generic_details() ))
        print("\n=== %s === \n%s" % ("disk_usage_info", rpi_sys_info.get_disk_usage_list() ))
        
        assert True

if __name__ == '__main__':
    unittest.main()