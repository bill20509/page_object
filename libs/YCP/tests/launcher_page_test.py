import pytest
from libs.app import App
from libs.base import BasePage
from YCP.pages.launcher_page import LauncherPage
# py.test --capture=no YMK_Test.py


class Test(object):

    def setup_method(self):  # run before every test
        self.driver = App().set_udid("PFYXINFELBU4HMU8")\
            .set_platform("Android")\
            .set_version("11")\
            .create()

        self.app = LauncherPage(self.driver)

    @pytest.mark.test
    def test_makeupcam(self):
        pass

    def teardown_method(self):  # quit driver when test case done
        self.driver.quit()


if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.test_makeupcam()
    t.teardown_method()
