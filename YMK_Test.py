import pytest
from libs.app import App
from libs.YMK import *

# py.test --capture=no YMK_Test.py


class Test_YMK(object):

    def setup_method(self):  # run before every test
        # 設定device
        self.driver = App().set_udid("PFYXINFELBU4HMU8")\
            .set_platform("Android")\
            .set_version("11")\
            .create()

        self.app = YMK_base.YMKbase(self.driver)

    @pytest.mark.test
    def test_makeupcam(self):
        self.app.deeplink_to_MakeupCam().click_back_launcher().click_makeupcam_button()

    def test_photo_edit_room(self):
        self.app.deeplink_to_Photomakeup().pick_photo("YouCam Makeup Sample", 4)\
            .click_makeup_menu("Mouth").select_brand("PERFECT").select_colorball(2)

    @pytest.mark.test
    def test_aging(self):
        self.app.deeplink_to_aging().click_Tryit().choose_photo()

    @pytest.mark.test
    def test_launcher(self):
        self.app.deeplink_to_launcher()

    # def teardown_method(self):  # quit driver when test case done
    #     self.driver.quit()
