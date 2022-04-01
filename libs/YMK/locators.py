# 各項element ID
from selenium.webdriver.common.by import By
from libs.element import Element


class OpeningTutorialPageLocators:
    GetStarted_button = Element("com.cyberlink.youcammakeup:id/getStartBtn", By.ID, "xxx buton")
    Skip_button = "com.cyberlink.youcammakeup:id/tutorialSkipBtn"
    Skip_confirm_button = "com.cyberlink.youcammakeup:id/alertDialog_buttonPositive"
    Background_id = "com.cyberlink.youcammakeup:id/opening_tutorial_background"


class LauncherLocators:
    Makeup_cam = Element("com.cyberlink.youcammakeup:id/cameraImage", By.ID, "MakeupCam button")
    Photo_makeup = "com.cyberlink.youcammakeup:id/photoMakeupImage"
    Store_button = "com.cyberlink.youcammakeup:id/shop_button"
    Aging_tile = "com.cyberlink.youcammakeup:id/launcherAgingTile"
    Skincare_tile = "com.cyberlink.youcammakeup:id/launcherSkinCareTile"
    YCV_tile = "com.cyberlink.youcammakeup:id/launcherPromoteTile1"
    YCP_tile = "com.cyberlink.youcammakeup:id/launcher_ycp_tile"
    Crown_LayoutA = "com.cyberlink.youcammakeup:id/launcherSubscriptionEntryButton"
    Crown_LayoutB = "com.cyberlink.youcammakeup:id/premium_button"
    AD_banner_LayoutB = "com.cyberlink.youcammakeup:id/CenterAdContainer"
    Me_button = "com.cyberlink.youcammakeup:id/bc_me_icon"

class PickPhotoLocators:
    # select_folder = Element("//*[contains(@text, 'YouCam Makeup Sample')]", By.XPATH, "Photo folder")
    # select_photo = Element("(//android.widget.ImageView[@content-desc='YouCam Makeup'])[1]", By.XPATH, "Select photo")
    select_folder = Element("com.cyberlink.youcammakeup:id/albumDisplayName", By.XPATH, "Select folder")
    select_photo = Element("com.cyberlink.youcammakeup:id/photoItemImage", By.XPATH, "Select photo")
    Back = Element("com.cyberlink.youcammakeup:id/topToolBarBackBtnContainer", By.ID, "Photo picker back button")

class PhotoMakeupLocators:
    Back = Element("com.cyberlink.youcammakeup:id/topToolBarBackBtnContainer", By.ID, "Back to Launcher page")
    CANCEL = Element("com.cyberlink.youcammakeup:id/alertDialog_buttonNegative", By.ID, "CANCEL change")
    LEAVE = Element("com.cyberlink.youcammakeup:id/alertDialog_buttonPositive", By.ID, "Leave photo edit page")
    Undo = Element("com.cyberlink.youcammakeup:id/EditViewUndoBtn", By.ID, "Undo edit button")
    Redo = Element("com.cyberlink.youcammakeup:id/EditViewRedoBtn", By.ID, "Redo edit button")
    SAVE = Element("com.cyberlink.youcammakeup:id/topToolBarExportBtn", By.ID, "Save Photo")
    Makeup_menu = Element("com.cyberlink.youcammakeup:id/makeup_menu_expandable_title", By.XPATH, "Makeup menu")
    brand_menu = Element("//*[@resource-id='com.cyberlink.youcammakeup:id/toolView']", By.XPATH, "Open brand menu")
    brand = Element("com.cyberlink.youcammakeup:id/skuItemVendorName", By.XPATH, "Select brand")
    content = Element("com.cyberlink.youcammakeup:id/item_color_content", By.XPATH, "Select content color ball")
    # Looks = Element("//*[@resource-id='com.cyberlink.youcammakeup:id/makeup_menu_expandable_title'][@text='Looks']", By.XPATH, "Looks")
    # Mouth = Element("//*[@resource-id='com.cyberlink.youcammakeup:id/makeup_menu_expandable_title'][@text='Mouth']", By.XPATH, "Mouth")

class MakeupCamLocators:
    BIPA_Agree = Element("com.cyberlink.youcammakeup:id/agree_btn", By.ID, "BIPA agree button")
    Feature_Notice_Close = "com.cyberlink.youcammakeup:id/close"
    Back = Element("com.cyberlink.youcammakeup:id/cameraBackIcon", By.ID, "Back to Launcher page")


class AgingLocators:
    Try_it = Element("com.cyberlink.youcammakeup:id/tryItButton", By.ID, "Try it button")
    Choose_photo = Element("com.cyberlink.youcammakeup:id/photoEntryButtonText", By.ID, "Choose photo")
    Take_photo = "com.cyberlink.youcammakeup:id/cameraEntryButtonText"
    Live_camera = "com.cyberlink.youcammakeup:id/cameraEntryButtonText"
    Photo = "com.cyberlink.youcammakeup:id/modeImage1"
    Before_After = "com.cyberlink.youcammakeup:id/modeImage2"
    Grid = "com.cyberlink.youcammakeup:id/modeImage3"
    Video = "com.cyberlink.youcammakeup:id/modeImage4"
    Back = "com.cyberlink.youcammakeup:id/topToolBarBackBtn"
    Home = "com.cyberlink.youcammakeup:id/homeButton"
    Save = "com.cyberlink.youcammakeup:id/topToolBarDoneBtn"
    Start = "com.cyberlink.youcammakeup:id/photoEntryButtonBackground"
    Agree = "com.cyberlink.youcammakeup:id/agree_btn"
    OK = "com.cyberlink.youcammakeup:id/alertDialog_buttonPositive"
    Allow = "com.android.permissioncontroller:id/permission_allow_button"


class ChurnUserRecoveryLocators:
    Close_button = "com.cyberlink.youcammakeup:id/churn_recovery_dialog_cancel_button"
    Continue_button = "com.cyberlink.youcammakeup:id/churn_recovery_dialog_continue_button"


class MeLocators:
    Settings_button = "com.cyberlink.youcammakeup:id/bc_top_bar_left_btn"


class DeepLink:
    MakeupCam_page = "ymk://action_makeupcam"
    PhotoMakeup_page = "ymk://action/pickphoto/"
    Bodytuner_page = "ymk://action_pickphoto/body_tuner"
    Launcher_page = "ymk://launcher"
    Aging_page = "ymk://action/ai_aging"
