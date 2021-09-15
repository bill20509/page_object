from appium import webdriver

class Ycp:
    def __init__(self):
        self.cap = {
            "platformName": "Android",
            "platformVersion": "10",
            'deviceName': 'f769b7a',
            # "app": r"/Users/zhongbill/APK/YouPerfect-5.66.0.6913.57131809.apk",
            # "appWaitActivity": "com.cyberlink.*",
            "noReset": False
        }
        package_namme = "com.cyberlink.youperfect"
        self.driver = webdriver.Remote("http://localhost:8100/wd/hub", self.cap)
        self.driver.implicitly_wait(8)
