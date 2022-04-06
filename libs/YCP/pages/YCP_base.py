
from libs.base import BasePage
import time
# from libs.YCP.pages.photo_edit_page import PhotoEditPage


class YCPBase(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def deeplink_to_photo_edit(self):
        self.deeplink(
            "ycp://action/pickphoto?editImageId=YouCamPerfectSample-18")
        from libs.YCP.pages.photo_edit_page import PhotoEditPage
        return PhotoEditPage(self.driver)
