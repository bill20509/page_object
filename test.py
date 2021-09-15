from lib.ycp import Ycp
from lib.resourceid import ElementID
from lib.ycp_gui import UI
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
UI = UI(ycp.driver)
UI.launcher_to_camera()
