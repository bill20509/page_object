from libs.YMK.locators import LauncherLocators
from libs.base import BasePage
import libs.YMK.makeupcam_page as makeupcam_page


class Launcher(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_makeupcam_button(self):
        self.click_element(LauncherLocators.Makeup_cam)
        return makeupcam_page.MakeupCam(self.driver)
