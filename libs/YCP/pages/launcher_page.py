from .photo_pick_page import PhotoPickPage
from libs.YCP.pages.YCP_base import YCPBase
from libs.YCP.locator import eLauncher


class LauncherPage(YCPBase):

    BIPA_count = 1

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def goto_photo_edit(self) -> PhotoPickPage:
        self.click_element(eLauncher.camera_button)
        LauncherPage.BIPA_count -= 1

        return PhotoPickPage(self.driver)
