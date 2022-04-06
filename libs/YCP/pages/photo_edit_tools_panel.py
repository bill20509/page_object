from .YCP_base import YCPBase
from libs.YCP.locator import ePhotoEditToolsPanel
from .photo_edit_tools_page import PhotoEditToolsPage


class PhotoEditToolsPanel(YCPBase):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def click_crop_and_rotate(self):
        self.click_element(ePhotoEditToolsPanel.crop_and_rotate)
        return PhotoEditToolsPage(self.driver)
