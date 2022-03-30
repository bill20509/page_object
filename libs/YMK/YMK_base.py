import libs.base
import libs.YMK as YMK
from libs.base import BasePage
from libs.YMK.locators import DeepLink

package_name = "com.cyberlink.youcammakeup"


class YMKbase(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def deeplink_to_launcher(self):
        self.deeplink(DeepLink.Launcher_page, package_name)
        return YMK.launcher_page.Launcher(self.driver)

    def deeplink_to_MakeupCam(self):
        self.deeplink(DeepLink.MakeupCam_page, package_name)
        return YMK.makeupcam_page.MakeupCam(self.driver)

    def deeplink_to_body_tuner(self):
        self.deeplink(DeepLink.Bodytuner_page, package_name)
        return YMK.bodytuner_page.Bodytuner(self.driver)

    def deeplink_to_aging(self):
        self.deeplink(DeepLink.Aging_page, package_name)
        return YMK.aging_page.Aging(self.driver)

        # "ymk://extra/NATURAL_LOOKS",
        # "ymk://action/skincare",
        # "ymk://action/trymakeupcamlooks",
        # "ymk://action/haircam",
        # "ymk://action_pickphoto/",
        # "ymk://action/tryBackground",
        # "ymk://action_pickphoto/body_tuner"