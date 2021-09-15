from lib import ycp_utility
import subprocess

from .resourceid import ElementID
import time

class UI:
    def __init__(self, ycp_driver):
        self.driver = ycp_driver

    def launcher_to_camera(self):
        camera = Camera(self.driver)
        camera.alert_dialog_positive_click()
        camera.permission_allow_button()
        camera.permission_foreground_only_button()
        camera.permission_allow_button()
        camera.bipa_agree_click()
        camera.tap_middle()

    def tutorial_to_launcher(self):
        pass

# class InstallTest:
#     def __init__(self, ycp_driver):
#         self.driver = ycp_driver
#
#     def install_check(self):
#         try:
#             command = "adb -s " + self.driver.cap["deviceName"] + " install \"" + self.driver.cap["app"] + "\""
#             subprocess.run(command, check=True)
#         except subprocess.CalledProcessError:
#             print("[Failed] Install Failed")
#         else:
#             print("[Pass] Install Pass")
#
#     def uninstall_check(self):
#         try:
#             command = "adb -s " + self.driver.cap["deviceName"] + " uninstall \"" + package_namme + "\""
#             subprocess.run(command, check=True)
#         except subprocess.CalledProcessError:
#             print("[Failed]  Uninstall Failed")
#         else:
#             print("[Pass] Uninstall Pass")


class Launcher:
    def __init__(self, driver):
        self.driver = driver

    def churn_recovery_dialog_cancel_button_click(self):
        # time.sleep(5)
        ycp_utility.button_click(self.driver, ElementID.churn_recovery_dialog_cancel_button, "churn_recovery_dialog_cancel_button")

    def editor_button_click(self):
        ycp_utility.button_click(self.driver, ElementID.editorButton, "editorButton")

    def old_editor_button_click(self):
        ycp_utility.button_click(self.driver, ElementID.old_editorButton, "old_editorButton")

    def new_camera_button_click(self):
        ycp_utility.button_click(self.driver, ElementID.cameraButton, "cameraButton")

    def old_camera_button_click(self):
        ycp_utility.button_click(self.driver, ElementID.old_camera, "old_cameraButton")

    def new_setting_button_click(self):
        ycp_utility.button_click(self.driver, ElementID.settingsButton, "new_settingsButton")

    def old_setting_button_click(self):
        ycp_utility.button_click(self.driver, ElementID.settingButton, "old_settingsButton")

    def promo_close_button(self):
        # time.sleep(10)
        ycp_utility.button_click_xpath(self.driver, ElementID.promo_close_button, "promo_close_button")

    def survey_close_button(self):
        ycp_utility.button_click(self.driver, ElementID.survey_close, "survey_close")


class Editor:
    def __init__(self, driver):
        self.driver = driver

    def buttonPositive_click(self):
        ycp_utility.button_click(self.driver, ElementID.buttonPositive, "buttonPositive")

    def permission_allow_button_click(self):
        ycp_utility.button_click(self.driver, ElementID.permission_allow_button, "permission_allow_button")

    def bipa_agree_click(self):
        ycp_utility.button_click(self.driver, ElementID.bipa_agree_button, "bipa_agree_button")

    def select_download_album(self, folder):
        select_folder = "//android.widget.TextView[contains(@text, '')]"
        ycp_utility.button_click_xpath(self.driver, ElementID.select_download_album, "select_download_album")

    def select_first_picture(self):
        ycp_utility.button_click_xpath(self.driver, ElementID.select_first_picture, "select_first_picture")

    def promo_close_button(self):
        # time.sleep(10)
        ycp_utility.button_click_xpath(self.driver, ElementID.promo_close_button, "promo_close_button")

    def beautify_tab_click(self):
        ycp_utility.button_click(self.driver, ElementID.beautify_tab, "beautify_tab")

    def autoface_button_click(self):
        ycp_utility.button_click(self.driver, ElementID.autoface_button, "autoface_button")

    def apply_button_click(self):
        ycp_utility.button_click(self.driver, ElementID.apply_button, "apply_button")

    def export_button_click(self):
        ycp_utility.button_click(self.driver, ElementID.export_button, "export_button")

    def subscribe_now_close_button_click(self):
        ycp_utility.button_click(self.driver, ElementID.subscribe_now_close_button, "subscribe_now_close_button")

    def ad_close_button_click(self):
        ycp_utility.button_click(self.driver, ElementID.ad_close_button, "ad_close_button")

    def bottom_tools_feature_click(self, num):
        e11 = self.driver.find_elements_by_id("com.cyberlink.youperfect:id/bottomToolsFeatureName")
        e11[num].click()  # effect

    def effect_panel_item_click(self, num):
        e11 = self.driver.find_elements_by_id("com.cyberlink.youperfect:id/effect_panel_item_name")
        e11[num].click()  #

    # def iterate_effect_filter(self):
    #     effect_list = ["Original", "Portrait"]
    #     while True:
    #         e14 = self.driver.find_elements_by_id("com.cyberlink.youperfect:id/effect_panel_item_name")
    #         no_element = True
    #         for i in range(len(e14)):
    #             # for j in range(len(e14)):
    #             #     print(e14[j].text)
    #             if e14[i].text in effect_list:
    #                 continue
    #             else:
    #                 no_element = False
    #                 effect_list.append(e14[i].text)
    #                 print(e14[i].text)
    #                 name = e14[i].text
    #                 e14[i].click()
    #                 time.sleep(0.1)
    #                 ycp_utility.screen_shot(name)
    #                 break
    #         if no_element == True:
    #             break


class Camera:
    def __init__(self, ycp_driver):
        self.driver = ycp_driver

    def alert_dialog_positive_click(self):
        ycp_utility.button_click(self.driver, ElementID.alertDialog_buttonPositive, "alertDialog_buttonPositive")

    def permission_allow_button(self):
        ycp_utility.button_click(self.driver, ElementID.photo_permission_allow_button, "photo_permission_allow_button")

    def permission_foreground_only_button(self):
        ycp_utility.button_click(self.driver, ElementID.permission_foreground_only_button, "permission_foreground_only_button")

    def tap_middle(self):
        ycp_utility.tap_middle()

    def photo_shot_click(self):
        ycp_utility.button_click(self.driver, ElementID.photo_shot, "Photo_shot click")

    def apply_button_click(self):
        ycp_utility.button_click(self.driver, ElementID.apply_button, "Apply button click")

    def adjust_click(self):
        ycp_utility.button_click(self.driver, ElementID.adjust_button, "Adjust button click")

    def beautify_tab_click(self):
        ycp_utility.button_click(self.driver, ElementID.camera_tab["beautify"], "camera_beautify_tab click")

    def effect_tab_click(self):
        ycp_utility.button_click(self.driver, ElementID.camera_tab["effect"], "camera_effect_tab click")

    def frame_tab_click(self):
        ycp_utility.button_click(self.driver, ElementID.camera_tab["frame"], "camera_frame_tab click")

    def grid_close_click(self):
        ycp_utility.button_click(self.driver, ElementID.grid_close_button, "grid_close_button click")

    def bipa_agree_click(self):
        ycp_utility.button_click(self.driver, ElementID.bipa_agree_button, "bipa_agree_button click")

class Tutorial:
    def __init__(self, ycp_driver):
        self.driver = ycp_driver

    # Check
    def tutorial_check(self):  # Checklist No,15
        ycp_utility.check_element_exist(self.driver, ElementID.tutorial_page, "tutorial_page")

    def facebook_button_check(self):
        ycp_utility.check_element_exist(self.driver, ElementID.tutorial_facebook_button, "facebook_button")

    def email_button_check(self):
        ycp_utility.check_element_exist(self.driver, ElementID.tutorial_email_button, "email_button")

    def login_more_button_check(self):
        ycp_utility.check_element_exist(self.driver, ElementID.tutorial_login_more_button, "login_more_button")

    def have_an_account_check(self):
        ycp_utility.check_element_exist(self.driver, ElementID.tutorial_have_account_button, "have_account_button")

    def welcome_description_check(self):
        ycp_utility.check_element_exist(self.driver, ElementID.tutorial_welcome_description_button, "welcome_description_button")

    def iap_promotion_page_check(self):
        ycp_utility.check_element_exist(self.driver, ElementID.iap_promotion_page, "iap_promotion_page")

    # Click
    def facebook_button_click(self):
        ycp_utility.button_click(self.driver, ElementID.tutorial_facebook_button, "facebook_button")

    def email_button_click(self):
        ycp_utility.button_click(self.driver, ElementID.tutorial_email_button, "email_button")

    def login_more_button_click(self):
        ycp_utility.button_click(self.driver, ElementID.tutorial_login_more_button, "login_more_button")

    def iap_promotion_page_next_click(self):
        e11 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[1]/android.widget.Image")
        e11.click()

    def get_stared_click(self):
        ycp_utility.button_click(self.driver, ElementID.tutorial_get_stared, "tutorial_get_stared_click")


class Setting:
    def __init__(self, ycp_driver):
        self.driver = ycp_driver

    def buttonPositive_click(self):
        ycp_utility.button_click(self.driver, ElementID.buttonPositive, "buttonPositive")

    def about_button_click(self):
        time.sleep(1)
        ycp_utility.swipe_down()
        print("swipe")
        time.sleep(1)
        # element = self.driver.element_find_by_xpath(ElementID.about_button)
        # print(ElementID.about_button)
        # element.click()
        ycp_utility.button_click_xpath(self.driver, ElementID.about_button, "about_button")

    def quality_button_click(self):
        ycp_utility.button_click_xpath(self.driver, ElementID.quality_button, "quality_button")

    def secrect_tech_open(self):
        ycp_utility.button_click(self.driver, ElementID.secret_tech, "secret open")
        ycp_utility.button_click(self.driver, ElementID.secret_tech, "secret open")
        ycp_utility.button_click(self.driver, ElementID.secret_tech, "secret open")
        ycp_utility.button_click(self.driver, ElementID.secret_tech, "secret open")
        ycp_utility.button_click(self.driver, ElementID.secret_tech, "secret open")

    # in secret tech
    def item_switch_click(self, num):
        elements = self.driver.find_elements_by_id(ElementID.item_switch)
        elements[num].click()

    def photo_quality_number_check(self):
        elements = self.driver.find_elements_by_id(ElementID.item_selected_image)
        number = len(elements)
        memory = ycp_utility.get_device_merory()
        if memory < 800 / 2 ** 10:
            if number != 1:
                ycp_utility.fail_prompt("photo_quality_number_check" + str(number) + "should be 1")
        elif memory < 2:
            if number != 2:
                ycp_utility.fail_prompt("photo_quality_number_check" + str(number) + "should be 2")
        else:
            if number != 3:
                ycp_utility.fail_prompt("photo_quality_number_check" + str(number) + "should be 3")
        ycp_utility.pass_prompt("photo_quality_number_check" + str(number))


    #0 = smart / 1 = Ultra/ 2 = high
    def photo_quality_select(self, num):
        elements = self.driver.find_elements_by_id(ElementID.item_selected_image)
        elements[num].click()

    def turn_on_dev_debug(self):
        self.item_switch_click(0)
        time.sleep(2)
        self.item_switch_click(3)