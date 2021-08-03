# Default Status
# Network: Disconnected
# Premium: On
import time
import traceback
import sys
from lib.mail import *
from lib import ycp_utility
from lib.ycp import Ycp
from lib.ycp_gui import Tutorial, Launcher, Setting, Camera
import datetime
from pymediainfo import MediaInfo

# Initialize report
result = True
attached_list = []

# Initialize log
log_path = r"./log/output_limit_" + str(datetime.date.today()).replace("-", "_") + "_log"
sys.stdout = open(log_path, 'w')


def output_limit_judge(quality, filename):
    # output size high < 1600:
    if quality == "High":
        ycp_utility.pulled_file(filename)
        media_info = MediaInfo.parse("./src/pulled_from_device/latest.png")
        image_track = media_info.image_tracks[0]
        memory = ycp_utility.get_device_merory()
        print(str(image_track.width) + str(image_track.height))
        if memory < 0.8:
            if max(int(image_track.width), int(image_track.height)) > 1024:
                ycp_utility.fail_prompt(quality + " quality (<1024)")
            else:
                ycp_utility.pass_prompt(quality + " quality (<1024)")
        else:
            if max(int(image_track.width), int(image_track.height)) > 1600:
                ycp_utility.fail_prompt(quality + " quality (<1600)")
            else:
                ycp_utility.pass_prompt(quality + " quality (<1600)")
    elif quality == "Ultra":
        ycp_utility.pulled_file(filename)
        media_info = MediaInfo.parse("./src/pulled_from_device/latest.png")
        image_track = media_info.image_tracks[0]
        print(str(image_track.width) + str(image_track.height))
        if max(int(image_track.width), int(image_track.height)) > 3200:
            ycp_utility.fail_prompt(quality + " quality (<3200)")
        else:
            ycp_utility.pass_prompt(quality + " quality (<3200)")
    elif quality == "Smart":
        ycp_utility.pulled_file(filename)
        media_info = MediaInfo.parse("./src/pulled_from_device/latest.png")
        image_track = media_info.image_tracks[0]
        print(str(image_track.width) + str(image_track.height))
        if ycp_utility.get_device_api_version() > 23:
            if max(int(image_track.width), int(image_track.height)) > 6144:
                ycp_utility.fail_prompt(quality + " quality (<6144)")
            else:
                ycp_utility.pass_prompt(quality + " quality (<6144)")
        else:
            if max(int(image_track.width), int(image_track.height)) > 4096:
                ycp_utility.fail_prompt(quality + " quality (<4096)")
            else:
                ycp_utility.pass_prompt(quality + " quality (<4096)")

    # block_list = {"xiaomi": "Redmi Note 7"}
    # info_dict = ycp_utility.camera_info_parse(info)
    # device_model = ycp_utility.get_device_model()
    # device_os = ycp_utility.get_device_os_version()
    # memory = ycp_utility.get_device_merory()
    # memory = (int(memory) / (2 ** 20))
    # device_brand = ycp_utility.get_device_brand()
    #
    # res = info_dict["Cam"].split("x")
    # preview_max_length = max(res[0], res[1])
    # print(preview_max_length)
    # if preview_max_length > 2000:
    #     print("error error")
    #
    #
    # if memory < 1:
    #     print("<1")
    # elif memory >= 1 and memory < 2:
    #     print("1~2")
    # elif memory >= 2:
    #     print(">2")
    # else:
    #     print("error")
    # if block_list[device_brand] == device_model:
    #     print("block!!!")
    # else:
    #     print("don't block")


try:
    # <===== Initialize Start =====>
    ycp_utility.clear_ycp_data()
    ycp = Ycp()
    latest_file = ycp_utility.get_latest_filename(ycp)  # To make sure the latest_file is updated
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

    # <===== High Quality End ======>
    output_limit_judge("High", latest_file)  # Quality high test start
    # <===== High Quality End ======>

    if ycp_utility.brand_block(): # Brand Block
        print("block")
        ycp.driver.quit()
        exit()
    if ycp_utility.get_device_merory() < 800 / 2 ** 10:  # Memory Block
        print("memory below 800MB")
        ycp.driver.quit()
        exit()
    time.sleep(10) # Wait 10s to let file saved

    # <===== Ultra Quality Start =====>
    ycp.driver.back()
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
    while latest_file == ycp_utility.get_latest_filename(ycp):
        continue
    latest_file = ycp_utility.get_latest_filename(ycp)
    output_limit_judge("Ultra", latest_file)
    # <===== Ultra Quality End =====>

    if ycp_utility.get_device_merory() < 2:  # Memory Block
        print("memory below 2GB")
        ycp.driver.quit()
        exit()
    time.sleep(10) # Wait 10s to let file saved

    # <===== Smart Quality Start =====>
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
    while latest_file == ycp_utility.get_latest_filename(ycp):
        continue
    latest_file = ycp_utility.get_latest_filename(ycp)
    output_limit_judge("Smart", latest_file)
    ycp.driver.quit()
    # <===== Smart Quality End =====>
except Exception as e:
    print(e)
    traceback.print_exc()
finally:
    sys.stdout.close()
    attached_list.append(log_path)
    info = ycp_utility.get_hardware_info()
    # Send report
    mail_html = attach_html(r"./src/report_template/output_limit_report.html",
                            {"title": "Output_Limit",
                             "result": "Pass" if result else "Fail",
                             "device_brand": info["device_brand"],
                             "device_model": info["device_model"],
                             "device_memory": info["device_memory"],
                             "device_api": info["device_api"]
                             })

    mail = AutoMail("Output_Limit", mail_html, attached_list)
    mail.send()
