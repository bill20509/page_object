from appium.webdriver import webdriver


class YMK:
    def __init__(self, device_name, os_ver, build_path, platform_name = "Android", waiting_time = 2):
        self.IMPLICITLY_WAIT_SLOW = waiting_time
        self.cap = {
            'udid': device_name,
            "platformName": platform_name,
            "platformVersion": os_ver,
            # "app": build_path,
            "appWaitActivity": "com.cyberlink.*",
            "autoGrantPermissions": True,
            "newCommandTimeout": 60,
            "autoLaunch": True,
            # "fullReset": True,
            "disableWindowAnimation": True,
            "waitForIdleTimeout": 0
        }
        self.package_name = "com.cyberlink.youcammakeup"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.cap)
        self.driver.implicitly_wait(self.IMPLICITLY_WAIT_SLOW)
