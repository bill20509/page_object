from appium import webdriver


class App:

    def __init__(self):
        # 'udid': device_name,
        # "platformName": platform_name,
        # "platformVersion": os_ver,
        # # "app": build_path,
        # "appWaitActivity": "com.cyberlink.*",
        # "autoGrantPermissions": True,
        # "newCommandTimeout": 60,
        # "autoLaunch": auto_launch,
        # # "fullReset": True,
        # "disableWindowAnimation": True,
        # "waitForIdleTimeout": 0
        self.caps = {
            'udid': "",
            "platformName": "",
            "platformVersion": "",
            "appPackage": "com.cyberlink.youcammakeup",
            "appActivity": "com.cyberlink.youcammakeup.activity.SplashActivity",
            "ignoreHiddenApiPolicyError": True,
            "noReset": True,
            "autoGrantPermissions": True,
            "newCommandTimeout": 60,
            "autoLaunch": False,
        }

    def set_udid(self, udid):
        self.caps["udid"] = udid
        return self

    def set_platform(self, platform):
        self.caps["platformName"] = platform
        return self

    def set_version(self, version):
        self.caps["platformVersion"] = version
        return self

    def create(self):
        driver = webdriver.Remote("http://localhost:4723/wd/hub", self.caps)
        driver.implicitly_wait(5)
        return driver

    # def close(self):
    #     self.driver.quit()
