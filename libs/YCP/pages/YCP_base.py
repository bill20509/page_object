from libs.base import BasePage
from libs.YCP.pages.photo_edit_page import PhotoEditPage


class YCPBase(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def deeplink_to_photo_edit(self):
        self.deeplink(
            " ycp://action/pickphoto?editImageId=YouCamPerfectSample-18", "123")
        return PhotoEditPage(self.driver)
