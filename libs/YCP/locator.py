from json import tool
from libs.element import Element


class eLauncher:
    camera_button = Element("123", "id")


class ePhotoEdit:
    tools_button = Element('//*[@text="Tools"]', "xpath")


class ePhotoEditToolsPanel:
    crop_and_rotate = Element('//*[@text="Crop & Rotate"]', "xpath")
