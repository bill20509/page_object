
from .YCP_base import YCPBase
from libs.YCP.pages.photo_edit_tools_panel import PhotoEditToolsPanel
from libs.YCP.locator import ePhotoEdit


class PhotoEditPage(YCPBase):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def back(self):
        pass

    def save(self):
        pass

    def open_tools(self):
        self.click_element(ePhotoEdit.tools_button)
        return PhotoEditToolsPanel(self.driver)

    def goto_effects(self):
        pass

    def goto_animation(self):
        pass

    def goto_removal(self):
        pass

    def goto_beautify(self):
        pass
