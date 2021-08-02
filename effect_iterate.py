import time
from lib import ycp_utility
from lib.ycp import Ycp
from lib.ycp_gui import Tutorial, Launcher, Setting, Camera, Editor


ycp_utility.clear_ycp_data()
ycp = Ycp()

Tutorial = Tutorial(ycp.driver)
Launcher = Launcher(ycp.driver)
Setting = Setting(ycp.driver)
Camera = Camera(ycp.driver)
Editor = Editor(ycp.driver)

Tutorial.get_stared_click()
# Launcher.churn_recovery_dialog_cancel_button_click()
Launcher.old_editor_button_click()
Editor.buttonPositive_click()
Editor.permission_allow_button_click()
Editor.bipa_agree_click()
Editor.select_download_album()
Editor.select_first_picture()
Editor.beautify_tab_click()
Editor.bottom_tools_feature_click(0)
# 0 = effect
Editor.effect_panel_item_click(1)
# # 1 = Portrait
time.sleep(2)
Editor.iterate_effect_filter()
