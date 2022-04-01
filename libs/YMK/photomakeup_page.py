from libs.YMK.locators import PhotoMakeupLocators
from libs.YMK.locators import PickPhotoLocators
from libs.base import BasePage


class Photomakeup(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def pick_photo(self, folder, photo=1):
        self.click_element_by_name(PickPhotoLocators.select_folder, folder)
        self.select_element_by_number(PickPhotoLocators.select_photo, photo)
        return Photomakeup(self.driver)

    def click_back(self):
        self.click_element(PhotoMakeupLocators.Back)
        return Photomakeup(self.driver)

    def click_makeup_menu(self, name):
        self.click_element_by_name(PhotoMakeupLocators.Makeup_menu, name)
        return Photomakeup(self.driver)

    def select_brand(self, name):
        self.click_element(PhotoMakeupLocators.brand_menu)
        self.click_element_by_name(PhotoMakeupLocators.brand, name)
        return Photomakeup(self.driver)

    def select_colorball(self, number):
        self.select_element_by_number(PhotoMakeupLocators.content, number)
        return Photomakeup(self.driver)


