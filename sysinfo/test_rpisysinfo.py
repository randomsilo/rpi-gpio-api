import unittest

from sysinfo.rpisysinfo import RpiSysInfo

class RpiSysInfoTestSuite(unittest.TestCase):
    """First test cases."""

    def test_unittest_setup(self):
        assert True

    def test_simple(self):
        rpi_sys_info = RpiSysInfo()
        
        print("=== %s === \n %s" % ("SECTION", rpi_sys_info.get_cpu_generic_details() ))
        
        assert True

if __name__ == '__main__':
    unittest.main()