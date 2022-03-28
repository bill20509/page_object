import os
import time
import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
import sys
from libs.app import App
from libs.YMK import *

# py.test --capture=no YMK_Test.py

class Test_Launcherpage(object):

    def setup_class(self):  # run before every test
        driver = App().set_udid()\
            .set_platform("Android")\
            .create()

        self.app = Launcher(driver)

        # self.caps = {
        #     'udid': "PFYXINFELBU4HMU8",
        #     "platformName": "Android",
        #     "platformVersion": "11.0",
        #     # "app": build_path,
        #     "appPackage": "com.cyberlink.youcammakeup",
        #     "appActivity": "com.cyberlink.youcammakeup.activity.SplashActivity",
        #     "ignoreHiddenApiPolicyError": True,
        #     "autoGrantPermissions": True,
        #     "newCommandTimeout": 60,
        #     "autoLaunch": True,
        # }
        # self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.caps)
        # self.driver.implicitly_wait(5)

    def test_launcher_camerabutton_is_show(self):
        a = self.app.click_makeupcam_button().click_element("152").

        # page = YMK.launcher_page.Launcher(self.driver)
        # page.findElement("id", "com.cyberlink.youcammakeup:id/cameraImage")

    def test_enter_makeup_cam(self):
        self.app.click_makeupcam_button()
        time.sleep(5)

    def teardown(self):  # quit driver when test case done
        self.driver.quit()
        self.


if __name__ == '__main__':
    pytest.main()
