from libs.YMK.locators import LauncherLocators
from libs.base import BasePage
from libs.YMK.makeupcam_page import MakeupCam


class Launcher(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_makeupcam_button(self):
        self.click_element(LauncherLocators.Makeup_cam)
        return MakeupCam(self.driver)
        # self.driver.find_element_by_id(LauncherLocators.Makeup_cam).click()

    # def click_aging_tile(self):
    #     self.driver.find_element_by_id(LauncherLocators.Aging_tile).click()
    #     return Camera(self.driver)