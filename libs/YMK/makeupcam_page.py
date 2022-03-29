from libs.YMK.locators import MakeupCamLocators
from libs.base import BasePage
import libs.YMK.launcher_page as launcher_page


class MakeupCam(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def check_BIPA(self):
        self.click_element(MakeupCamLocators.BIPA_Agree)
        return MakeupCam(self.driver)

    def back_launcher(self):
        self.click_element(MakeupCamLocators.Back)
        return launcher_page.Launcher(self.driver)
