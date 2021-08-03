# Default status
# Network: Disconnected
# Login: Off
# Premium: On
# Launcher: Old
import time
import traceback
import datetime
import sys
from lib import ycp_utility
from lib.ycp import Ycp
from lib.ycp_gui import Tutorial, Launcher, Setting, Camera
from lib.mail import *
# Initialize test result
result = True
attached_list = []


def preview_limit_judge(info):
    # preview size limit
    preview = info["Preview"].split("x")
    if max(int(preview[0]), int(preview[1])) > 2000:
        ycp_utility.fail_prompt("Preview size > 2000")
    else:
        ycp_utility.pass_prompt("Preview size ")


# Initialize log
log_path = r"./log/preview_limit_" + str(datetime.date.today()).replace("-", "_") + "_log"
sys.stdout = open(log_path, 'w')


try:
    # <====== Initialize Start =====>
    ycp_utility.clear_ycp_data()
    ycp = Ycp()
    tutorial = Tutorial(ycp.driver)
    launcher = Launcher(ycp.driver)
    setting = Setting(ycp.driver)
    camera = Camera(ycp.driver)
    # <====== Initialize End =====>

    # <====== Tutorial Start =====>
    tutorial.get_stared_click()
    # <====== Tutorial End =====>

    # <====== Launcher Start =====>
    # launcher.churn_recovery_dialog_cancel_button_click()
    launcher.old_setting_button_click()
    # <====== Launcher End =====>

    # <====== Setting Start =====>
    setting.about_button_click()
    setting.secrect_tech_open()
    setting.turn_on_dev_debug()
    ycp.driver.back()
    ycp.driver.back()
    ycp.driver.back()
    # <====== Setting End =====>

    # <====== Launcher Start =====>
    # time.sleep(5)
    # launcher.promo_close_button()
    # launcher.promo_close_button()
    launcher.old_camera_button_click()
    # <====== Launcher End =====>

    # <====== Camera Start =====>
    time.sleep(3)
    camera.alert_dialog_positive_click()
    camera.permission_allow_button()
    camera.permission_foreground_only_button()
    camera.permission_allow_button()
    camera.bipa_agree_click()
    time.sleep(1)
    camera.tap_middle()
    # <====== Camera End =====>

    # <====== Test Start =====>
    info = ycp_utility.get_camera_info(ycp.driver)
    preview_limit_judge(ycp_utility.camera_info_parse(info))
    ycp.driver.quit()
    # <====== Test End =====>
except Exception as e:
    result = False
    print(e)
    traceback.print_exc()
finally:
    sys.stdout.close()
    attached_list.append(log_path)

    # Send report
    mail_html = attach_html(r"./src/report_template/preview_limit_report.html",
                            {"title": "Preview_Limit",
                             "result": "Pass" if result else "Fail"})
    mail = AutoMail("Preview_Limit", mail_html, attached_list)
    mail.send()