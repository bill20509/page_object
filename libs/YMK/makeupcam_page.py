from libs.YMK.Locators import MakeupCamLocators
from libs.base import BasePage

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MakeupCam(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def check_BIPA_and_close(self):
        self.click_element(MakeupCamLocators.BIPA_Agree)
        return MakeupCam(self.driver)
