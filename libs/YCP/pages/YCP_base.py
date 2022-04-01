from libs.base import BasePage

try:
    from libs.YCP.pages.photo_edit_page import PhotoEditPage
except ImportError:
    pass


class YCPBase(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def deeplink_to_photo_edit(self):
        self.deeplink(
            "ycp://action/pickphoto?editImageId=YouCamPerfectSample-18", "123")
        return PhotoEditPage(self.driver)
