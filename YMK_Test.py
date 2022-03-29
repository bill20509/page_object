import os
import time
import pytest
from appium import webdriver
import sys
from libs.app import App
from libs.YMK import *

# py.test --capture=no YMK_Test.py


class Test_Launcherpage(object):

    def setup_class(self):  # run before every test
        driver = App().set_udid("PFYXINFELBU4HMU8")\
            .set_platform("Android")\
            .create()

        self.app = launcher_page.Launcher(driver)

    def test_launcher_camera_button(self):
        self.app.YMKbase.deeplink_to_MakeupCam()
        # self.app.back_launcher().click_makeupcam_button().check_BIPA()
        # self.app.find_element("id", "com.cyberlink.youcammakeup:id/cameraImage").click_makeupcam_button().check_BIPA()
        self.app.click_makeupcam_button().check_BIPA().back_launcher().click_makeupcam_button()

    # def teardown_class(self):  # quit driver when test case done


if __name__ == '__main__':
    pytest.main()
