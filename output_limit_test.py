# Default Status
# Network: Disconnected
# Premium: On
import time
import traceback
import sys
from lib import ycp_utility
from lib.ycp import Ycp
from lib.ycp_gui import Tutorial, Launcher, Setting, Camera
import datetime

# Initialize report
result = ""

# Initialize log
log_path = r"./log/output_limit_" + str(datetime.date.today()).replace("-", "_") + "_log"
sys.stdout = open(log_path, 'w')

try:
    # <===== Initialize Start =====>
    ycp_utility.clear_ycp_data()
    ycp = Ycp()
    latest_file = ycp_utility.get_latest_filename(ycp) # To make sure the latest_file is updated
    Tutorial = Tutorial(ycp.driver)
    Launcher = Launcher(ycp.driver)
    Setting = Setting(ycp.driver)
    Camera = Camera(ycp.driver)
    # <===== Initialize End =====>

    # <===== Tutorial Start =====>
    Tutorial.get_stared_click()
    # Launcher.churn_recovery_dialog_cancel_button_click()
    Launcher.old_camera_button_click()
    # <===== Tutorial End =====>

    # <===== Camera Start =====>
    Camera.alert_dialog_positive_click()
    Camera.permission_allow_button()
    Camera.permission_foreground_only_button()
    Camera.permission_allow_button()
    Camera.bipa_agree_click()
    time.sleep(1)  # Sleep 1s to avoid tap middle too fast
    Camera.tap_middle()
    Camera.photo_shot_click()
    Camera.apply_button_click()
    # <===== Camera End =====>

    # To wait image file update
    while latest_file == ycp_utility.get_latest_filename(ycp):
        continue
    latest_file = ycp_utility.get_latest_filename(ycp)

    ycp_utility.output_limit_judge("High")
    if ycp_utility.brand_block():
        print("block")
        ycp.driver.quit()
        exit()
    if ycp_utility.get_device_merory() < 800 / 2 ** 10:
        print("memory below 800MB")
        ycp.driver.quit()
        exit()
    time.sleep(10)
    ycp.driver.back()
    # Launcher.survey_close_button()
    Launcher.old_setting_button_click()
    Setting.quality_button_click()
    Setting.photo_quality_number_check()
    Setting.photo_quality_select(1)
    Setting.buttonPositive_click()
    ycp.driver.back()
    ycp.driver.back()
    Launcher.old_camera_button_click()
    Camera.tap_middle()
    Camera.photo_shot_click()
    Camera.apply_button_click()
    while latest_file == ycp_utility.get_latest_filename():
        continue
    latest_file = ycp_utility.get_latest_filename()
    ycp_utility.output_limit_judge("Ultra")

    if ycp_utility.get_device_merory() < 2:
        print("memory below 2GB")
        ycp.driver.quit()
        exit()
    time.sleep(10)
    ycp.driver.back()
    Launcher.old_setting_button_click()
    Setting.quality_button_click()
    Setting.photo_quality_select(0)
    Setting.buttonPositive_click()
    ycp.driver.back()
    ycp.driver.back()
    Launcher.old_camera_button_click()
    Camera.tap_middle()
    Camera.photo_shot_click()
    Camera.apply_button_click()
    while latest_file == ycp_utility.get_latest_filename():
        continue
    latest_file = ycp_utility.get_latest_filename()
    ycp_utility.output_limit_judge("Smart")
    ycp.driver.quit()
except Exception as e:
    print("exceprtion occur")
    traceback.print_exc()
finally:

    print("report time")
