import pytest
from libs.app import App
from libs.YCP.pages.launcher_page import LauncherPage
from libs.YCP.pages.photo_edit_page import PhotoEditPage
# py.test --capture=no YMK_Test.py


class Test(object):

    def setup_method(self):  # run before every test
        self.driver = App().set_udid("PFYXINFELBU4HMU8")\
            .set_platform("Android")\
            .set_version("11")\
            .create()

        self.app = LauncherPage(self.driver)

    @pytest.mark.test
    def test_photo_edit_tools(self):
        self.app.deeplink_to_photo_edit()\
            .open_tools()\
            .click_crop_and_rotate()

    def teardown_method(self):  # quit driver when test case done
        self.driver.quit()


if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.test_photo_edit_tools()
    t.teardown_method()
