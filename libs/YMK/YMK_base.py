import libs.base
import libs.YMK as YMK
from libs.base import BasePage
from libs.YMK.locators import DeepLink

package_name = "com.cyberlink.youcammakeup"


class YMKbase(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def deeplink_to_MakeupCam(self):
        self.deeplink(DeepLink.MakeupCam_page, package_name)
        return YMK.makeupcam_page.MakeupCam(self.driver)
