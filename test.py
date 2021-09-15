from lib.ycp import Ycp
from lib.resourceid import ElementID
from lib.ycp_gui import UI, Camera
from lib import ycp_utility
ycp_utility.clear_ycp_data()
ycp = Ycp()
ycp.driver.execute_script(
    "mobile: deepLink",
    {
        "url": "ycp://action_takephoto?beauty_tab=cheekbone",
        "package": "com.cyberlink.youperfect"
    }
)
camera = Camera(ycp.driver)
camera.bipa_agree_click()
camera.camera_hint_click()


