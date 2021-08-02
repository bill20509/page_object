# Writen
import time
from lib import ycp_utility
from lib.ycp import Ycp
from lib.ycp_gui import Tutorial, Launcher, Setting, Camera

time_start = time.time() #開始計時

ycp_utility.clear_ycp_data()
ycp = Ycp()


Tutorial = Tutorial(ycp.driver)
Launcher = Launcher(ycp.driver)
Setting = Setting(ycp.driver)
Camera = Camera(ycp.driver)

Tutorial.get_stared_click()
# Launcher.churn_recovery_dialog_cancel_button_click()
Launcher.old_setting_button_click()

Setting.about_button_click()
Setting.secrect_tech_open()
Setting.turn_on_dev_debug()
ycp.driver.back()
ycp.driver.back()
ycp.driver.back()

# time.sleep(5)
# Launcher.promo_close_button()
# Launcher.promo_close_button()
Launcher.old_camera_button_click()

time.sleep(3)
Camera.alert_dialog_positive_click()
Camera.permission_allow_button()
Camera.permission_foreground_only_button()
Camera.permission_allow_button()
Camera.bipa_agree_click()
time.sleep(1)
Camera.tap_middle()
ycp_utility.preview_limit_judge(ycp_utility.camera_info_parse(Camera.get_camera_info()))
ycp.driver.quit()
time_end = time.time()    #結束計時
time_c = time_end - time_start   #執行所花時間
print('time cost', time_c, 's')

