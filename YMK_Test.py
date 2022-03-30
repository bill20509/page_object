import pytest
from libs.app import App
from libs.YMK import *

# py.test --capture=no YMK_Test.py


class Test_YMK(object):

    def setup_method(self):  # run before every test
        self.driver = App().set_udid("PFYXINFELBU4HMU8")\
            .set_platform("Android")\
            .set_version("11")\
            .create()

        self.app = YMK_base.YMKbase(self.driver)

    @pytest.mark.test
    def test_makeupcam(self):
        self.app.deeplink_to_MakeupCam().click_back_launcher().click_makeupcam_button()

    def test_body_tuner(self):
        self.app.deeplink_to_body_tuner()

    @pytest.mark.try1
    def test_aging(self):
        self.app.deeplink_to_aging().click_Tryit().choose_photo()

    @pytest.mark.test
    def test_launcher(self):
        self.app.deeplink_to_launcher()

    def teardown_method(self):  # quit driver when test case done
        self.driver.quit()
