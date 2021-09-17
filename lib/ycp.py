from appium import webdriver
from lib.resourceid import Implicitly_time
class Ycp:
    def __init__(self):
        self.cap = {
            "platformName": "Android",
            "platformVersion": "11",
            'deviceName': 'R5CR5122ACA',
            "app": r"/Users/zhongbill/APK/YouPerfect-5.66.0.6913.57131809.apk",
            "appWaitActivity": "com.cyberlink.*",
            "autoGrantPermissions": True,
            "newCommandTimeout": 9999
            # "language": "fr",
            # "locale": "FR"
        }

        package_namme = "com.cyberlink.youperfect"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.cap)
        self.driver.implicitly_wait(Implicitly_time.IMPLICITLY_WAIT_SLOW)
