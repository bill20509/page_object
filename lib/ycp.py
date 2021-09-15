from appium import webdriver

class Ycp:
    def __init__(self):
        self.cap = {
            "platformName": "Android",
            "platformVersion": "11",
            'deviceName': 'R5CR5122ACA',
            "app": r"/Users/zhongbill/APK/YouPerfect-5.66.0.6913.57131809.apk",
            "appWaitActivity": "com.cyberlink.*",
            "autoGrantPermissions": True,
            # "language": "fr",
            # "locale": "FR"
        }
        package_namme = "com.cyberlink.youperfect"
        self.driver = webdriver.Remote("http://localhost:8100/wd/hub", self.cap)
        self.driver.implicitly_wait(8)
