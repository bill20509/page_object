from appium import webdriver


class App:
    def __init__(self):
        # self.udid = "PFYXINFELBU4HMU8"
        # self.platformName =  "Android"
        # self.implicitly_wait = "5"
        #     # "platformVersion": "11.0",
        #     # # "app": build_path,
        #     # "appPackage": "com.cyberlink.youcammakeup",
        #     # "appActivity": "com.cyberlink.youcammakeup.activity.SplashActivity",
        #     # "ignoreHiddenApiPolicyError": True,
        #     # "autoGrantPermissions": True,
        #     # "newCommandTimeout": 60

        self.caps = {
            'udid': "",
            "platformName": "",
            "platformVersion": "11.0",
            # "app": build_path,
            "appPackage": "com.cyberlink.youcammakeup",
            "appActivity": "com.cyberlink.youcammakeup.activity.SplashActivity",
            "ignoreHiddenApiPolicyError": True,
            "noReset": True,
            "autoGrantPermissions": True,
            "newCommandTimeout": 60,
            "autoLaunch": True,
        }
    def set_platform(self, platform):
        self.caps["platformName"] = platform
        return self

    def set_udid(self, udid):
        self.caps["udid"] = udid
        return self

    def create(self):
        driver = webdriver.Remote("http://localhost:4723/wd/hub", self.caps)
        driver.implicitly_wait(5)
        return driver
