from appium import webdriver

class Ycp:
    def __init__(self):
        cap = {
            "platformName": "Android",
            "platformVersion": "10",
            'deviceName': 'f769b7a',
            "app": r"C:\Users\Bill God\Desktop\apk\YouPerfect-5.64.0.6715.55151740.apk",
            "appWaitActivity": "com.cyberlink.*",
            "noReset": False
        }
        package_namme = "com.cyberlink.youperfect"
        self.driver = webdriver.Remote("http://localhost:8100/wd/hub", cap)
        self.driver.implicitly_wait(8)
