import pytest
from selenium.webdriver.common.by import By
import sys
from libs import YMK


# python monkey_test.py PFYXINFELBU4HMU8 11.0 YouCamMakeup-5.95.0.8711.63111936.apk
# python monkey_test.py PFYXINFELBU4HMU8 11.0 YouPerfect-5.71.0.7509.63091059.apk

device_id = str(sys.argv[1])
os_ver = str(sys.argv[2])
build_path = str(sys.argv[3])

class Launcherpage():
    def setUP(self, YMK):
        ymk = YMK.YMK_base.webdriver



    def tearDown(slef, ymk):


if __name__ == '__main__':
    pytest.main()