# Default:
# Wifi Connected
# Samsung A52
# BC login
STICKER_DEEPLINK = "ycp://action_pickphoto/sticker?pack_guid={0}"  # Paremeter: guid
FILE_FOLD = "210720_minicreator_co_op_sticker"
JSON_FILE_NAME = "tomsr.json"
ALBUM_NAME = "YouCam Perfect Sample"
ALBUM_NUMBER = 3


from lib.resourceid import ElementID
from lib.ycp import Ycp
from lib.ycp_gui import UI, Camera, Tutorial, Launcher, Setting, Editor
from lib import ycp_utility
import json
from pathlib import Path
import os

# Init
print("./{0}/{1}".format(FILE_FOLD, JSON_FILE_NAME))
with open("./{0}/{1}".format(FILE_FOLD, JSON_FILE_NAME), "rb") as f:  # Read json file
    data = json.load(f)
GUID = data["guid"]
STICKER_COUNT = int(data["sticker_count"])
CURRENT_DIRECTORY = '%s/' % os.getcwd()
SAVE_FOLDER = CURRENT_DIRECTORY + "msr_auto/{0}/".format(GUID)

print(GUID, STICKER_COUNT)
print(STICKER_DEEPLINK.format(GUID))
# START
ycp_utility.clear_ycp_data()
ycp = Ycp()
old_file_name = ycp_utility.get_latest_filename(ycp)

ui = UI(ycp.driver)
launcher = Launcher(ycp.driver)
setting = Setting(ycp.driver)
editor = Editor(ycp.driver)

 # Go to Launcher
# launcher.new_setting_button_click()  # Click Setting
# setting.about_button_click()  # Click about
# setting.secrect_tech_open()  # Open secrrect
# setting.iap_open()   # Open IAP
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
ui.deeplink_to_editor()
# el = ycp.driver.find_element_by_image("./close_button.jpg")
# print(el.location)

editor.iterate_all_stickers(STICKER_COUNT)  # Sticker iterate
# editor.apply_button_click()  # apply sticker
#
# PREVIEW_SAVE_FOLDER = SAVE_FOLDER + "preview/"  # preview save folder
# Path(SAVE_FOLDER + "preview").mkdir(parents=True, exist_ok=True)  # create dir
# ycp.driver.save_screenshot("{}{}.png".format(PREVIEW_SAVE_FOLDER, GUID))  # screenshot to folder
# editor.export_button_click()  # export
# export_file_name = ycp_utility.get_latest_filename(ycp)  # get the latest file name
# while old_file_name == export_file_name:
#     export_file_name = ycp_utility.get_latest_filename(ycp)
# print("exportfilename" + export_file_name)

