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

        self.app.deep_link_to_page(locators.DeepLink.MakeupCam_page, "com.cyberlink.youcammakeup")
        # self.app.back_launcher().click_makeupcam_button().check_BIPA()
        # self.app.findElement("id", "com.cyberlink.youcammakeup:id/cameraImage").click_makeupcam_button().check_BIPA()

    # def test_launcher_camera_button_is_show(self):
    #     page = YMK.launcher_page.Launcher(self.driver)
    #     page.findElement("id", "com.cyberlink.youcammakeup:id/cameraImage")
    # def test_enter_makeup_cam(self):
    #     self.app.click_makeupcam_button()
    #     time.sleep(5)
    # def test_check_BIPA_and_close(self):
    #     try:
    #         WebDriverWait(self, 10, 0.1).until(EC.visibility_of_element_located((By.ID, "com.cyberlink.youcammakeup:id/agree_btn")))
    #         element = self.app.findElement(By.ID, "com.cyberlink.youcammakeup:id/agree_btn")
    #         element.click()
    #     except:
    #         return False

    # def teardown_class(self):  # quit driver when test case done


if __name__ == '__main__':
    pytest.main()
