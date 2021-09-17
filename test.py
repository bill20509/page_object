# Default:
# Wifi Connected
# Samsung A52
# BC login

# STICKER_DEEPLINK = "ycp://action_pickphoto/sticker?pack_guid={0}&editImageId={1}"  # Paremeter: guid, ImageID
STICKER_DEEPLINK = "ycp://action_pickphoto/sticker?pack_guid={0}"  # Paremeter: guid

IMAGE_ID = "YouCamPerfectSample-15"
FILE_FOLD = "210720_minicreator_co_op_sticker"
JSON_FILE_NAME = "tomsr.json"
GUID = ""
STICKER_COUNT = 0
ALBUM_NAME = "Body tuner"
ALBUM_NUMBER = 4

from lib.resourceid import ElementID
from lib.ycp import Ycp
from lib.ycp_gui import UI, Camera, Tutorial, Launcher, Setting, Editor
from lib import ycp_utility
import json


# Init
print("./{0}/{1}".format(FILE_FOLD, JSON_FILE_NAME))
with open("./{0}/{1}".format(FILE_FOLD, JSON_FILE_NAME), "rb") as f:  # Read json file
    data = json.load(f)
GUID = data["guid"]
STICKER_COUNT = int(data["sticker_count"])

print(GUID, STICKER_COUNT)
print(STICKER_DEEPLINK.format(GUID, IMAGE_ID))

# START
ycp_utility.clear_ycp_data()
ycp = Ycp()

ui = UI(ycp.driver)
launcher = Launcher(ycp.driver)
setting = Setting(ycp.driver)
editor = Editor(ycp.driver)

ui.tutorial_to_launcher()  # Go to Launcher
launcher.new_setting_button_click()  # Click Setting
setting.about_button_click()  # Click about
setting.secrect_tech_open()  # Open secrrect
setting.iap_open()   # Open IAP
# setting.guid_clipboard_open()  # Open GUID CLIPBOARD

ycp.driver.execute_script(  # Deeplink to Sticker
            "mobile: deepLink",
            {
                "url": STICKER_DEEPLINK.format(GUID),
                "package": "com.cyberlink.youperfect"
            }
        )
ui.camera_permissions()  # Camera permssions
editor.select_album_with_name(ALBUM_NAME)  # Open Download
editor.select_picture_with_number(ALBUM_NUMBER)  # Open number 0 picture
editor.iterate_all_stickers(STICKER_COUNT)  # Sticker iterate
editor.apply_button_click()
ycp.driver.save_screenshot("./" + GUID + ".png")
editor.export_button_click()

# ycp.driver.back()
# ycp.driver.back()
# ycp.driver.back()
# ui.launcher_to_camera()


# camera = Camera(ycp.driver)
# camera.bipa_agree_click()
# camera.camera_hint_click()

