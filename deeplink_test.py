import time
import os
import sys
import yaml
import datetime
import traceback
from lib import ycp_utility
from lib.ycp import Ycp
from lib.ycp_gui import Camera, Editor
from lib.mail import AutoMail
from src.resourceid import ElementID
# Initial rootdir
rootdir = r"./src/deeplink_testcase/camera/"
# Initialize Pass/Fail count
pass_count = 0
fail_count = 0
attached_list = []
fail_list = []
def check_pack_name(ycp_driver, pack_name):
    pass
    # current_name = ycp_driver.find_element_by_xpath(ElementID.pack_name).text
    # if pack_name == current_name:
    #     ycp_utility.pass_prompt(pack_name + " pack check")
    # else:
    #     ycp_utility.fail_prompt(pack_name + " pack check")
    #     print("current is " + current_name)


def check_adjust(ycp_driver, adjust_info):
    n = len(adjust_info)
    if n >= 1:
        ycp_utility.check_value_equal(ycp_driver,  ElementID.intensity_first_number, int(adjust_info[0]))
    if n >= 2:
        ycp_utility.check_value_equal(ycp_driver, ElementID.intensity_second_number, int(adjust_info[1]))
    if n >= 3:
        ycp_utility.check_value_equal(ycp_driver, ElementID.intensity_third_number, int(adjust_info[2]))
    if n >= 4:
        ycp_utility.check_value_equal(ycp_driver, ElementID.intensity_fourth_number, int(adjust_info[3]))


# Initialize log
log_path = r"./log/deeplink_" + str(datetime.date.today()).replace("-", "_") + "_log"
sys.stdout = open(log_path, 'w')
# Append all file_path int root dir to file_list
test_case_list = []
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        file_path = subdir + os.sep + file
        test_case_list.append(file_path)
print(test_case_list)
print(len(test_case_list))
# Iterate all test_case
for test_case in test_case_list:
    try:
        # Open test_case file
        print("<========= Test Case: {} Start =========>".format(test_case))
        test_info = {}
        with open(test_case, 'r') as f:
            test_info = yaml.load(f.read(), Loader=yaml.FullLoader)
        # Initialize
        ycp_utility.clear_ycp_data()
        ycp = Ycp()
        ycp.driver.execute_script(
            "mobile: deepLink",
            {
                "url": test_info["link"],
                "package": test_info["app_name"]
            }
        )
        if test_info["room"] == "Camera":
            camera = Camera(ycp.driver)
            camera.alert_dialog_positive_click()
            camera.permission_allow_button()
            camera.permission_foreground_only_button()
            camera.permission_allow_button()
            camera.bipa_agree_click()
            camera.tap_middle()
            # check tab
            ycp_utility.check_element_attribute(ycp.driver, ElementID.camera_tab[test_info["entry"].lower()],
                                                "selected", "true")
            for tab in test_info["Tab"]:
                if tab == "EFFECT":
                    camera.effect_tab_click()
                    # check tab
                    ycp_utility.check_element_attribute(ycp.driver, ElementID.camera_tab[tab.lower()], "selected",
                                                        "true")
                    # check pack name
                    check_pack_name(ycp.driver, test_info["Tab"][tab]["entry_name"])
                    # check intensity
                    if test_info["Tab"][tab]["adjust"]:
                        camera.adjust_click()
                        check_adjust(ycp.driver, test_info["Tab"]["EFFECT"]["intensity"])
                        camera.grid_close_click()

                elif tab == "FRAME":
                    camera.frame_tab_click()
                    # check tab
                    ycp_utility.check_element_attribute(ycp.driver, ElementID.camera_tab[tab.lower()], "selected",
                                                        "true")
                    # check pack name
                    check_pack_name(ycp.driver, test_info["Tab"][tab]["entry_name"])

                elif tab == "Beautify":
                    camera.beautify_tab_click()
                    # check tab
                    ycp_utility.check_element_attribute(ycp.driver, ElementID.camera_tab[tab.lower()], "selected",
                                                        "true")
                    for key in test_info["Tab"][tab]["feature"]:
                        ycp_utility.button_click(ycp.driver, ElementID.beautify_feature[key.lower()], key + "Click")
                        # ycp_utility.check_value_equal(ycp.driver, ElementID.slider_value,
                        #                               int(test_info["Tab"][tab]["feature"][key])

                        # check intensity
                        ycp_utility.check_value_equal(ycp.driver, ElementID.slider_right_value,
                                                      int(test_info["Tab"][tab]["feature"][key]))
        elif test_info["room"] == "Edit":
            Editor = Editor(ycp.driver)
            if not test_info["sample"]:
                Editor.buttonPositive_click()
            Editor.permission_allow_button_click()
            Editor.bipa_agree_click()
            if not test_info["sample"]:  # select picture
                Editor.select_download_album(test_info["picture"]["folder"])
            #     pass
            # ycp_utility.check_string_name(ycp.driver, ElementID.moduleTitle, test_info["entry"])  # check module
            # ycp_utility.check_value_equal(ycp.driver, ElementID.effect_seek_bar, test_info["tab"]["FILTER"]["intensity"])  # check intensity
        # PASS: pass_count++
        pass_count += 1
    except Exception as e:
        traceback.print_exc()
        # Something fail: fail_count++ and attach fail case to list
        fail_count += 1
        attached_list.append(test_case)
        fail_name = test_case.split("\\")[1]
        fail_list.append(fail_name.split(".")[0])
    finally:
        print("<========= Test Case: {} End =========>".format(test_case))

# All test ends: report
report = """Total Case:{}, PASS:{}, FAIL:{}.
\tFail List: {}
""".format(len(test_case_list), pass_count, fail_count, fail_list)
print(report)
sys.stdout.close()

# Attach log to lis
attached_list.append(log_path)
# Send report mail
mail = AutoMail(report, attached_list)
mail.send()


