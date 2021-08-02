import time
import ycp_utility
from ycp import Ycp
import yaml
from ycp_gui import Camera
from resourceid import ElementID

with open('./deeplink_test1.yml', 'r') as f:
    test_info = yaml.load(f.read(), Loader=yaml.FullLoader)

print(test_info["Tab"]["EFFECT"]["intensity"])

ycp_utility.clear_ycp_data()
ycp = Ycp()
ycp.driver.execute_script(
    "mobile: deepLink",
    {
        "url": test_info["link"],
        "package": test_info["app_name"]
    }
)
Camera = Camera(ycp.driver)
Camera.alert_dialog_positive_click()
Camera.permission_allow_button()
Camera.permission_foreground_only_button()
Camera.permission_allow_button()
time.sleep(2)
Camera.tap_middle()
elements = ycp.driver.find_elements_by_class_name("android.widget.RelativeLayout")
print(len(elements))
elements[0].screenshot(r"./thumb1.png")
elements[2].screenshot(r"./thumb2.png")