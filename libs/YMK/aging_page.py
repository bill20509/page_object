from libs.YMK.locators import AgingLocators
from libs.base import BasePage
import libs.YMK.launcher_page as launcher_page


class Aging(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_Tryit(self):
        self.click_element(AgingLocators.Try_it)
        return Aging(self.driver)

    def choose_photo(self):
        self.click_element(AgingLocators.Choose_photo)
        return Aging(self.driver)

    def click_photo(self):
        self.click_element(AgingLocators.Choose_photo)
        return Aging(self.driver)

    def click_Start(self):
        self.click_element(AgingLocators.Start)
        return Aging(self.driver)

    def click_Allow(self):
        self.click_element(AgingLocators.Allow)
        return Aging(self.driver)

    def click_Back(self):
        self.click_element(AgingLocators.Back)
        return launcher_page.Launcher(self.driver)
