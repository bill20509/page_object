# 工具包
from selenium.webdriver.common.by import By


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    # Deep link
    def deeplink(self, page_link, package_name):
        self.driver.execute_script(
            "mobile: deepLink",
            {
                "url": page_link,
                "package": package_name
            }
        )
        return self

    # take screenshot in current page
    def current_screenshot(self, screenshotname=None):
        currentphoto = 'currentphoto/'
        screenshotName = screenshotname
        self.driver.save_screenshot(currentphoto + screenshotName)

    # Click button
    def click_element(self, element):
        try:
            self.driver.find_element(element.element_type, element.element_id).click()
        except Exception as e:
            print(e)
            print("Can't find " + element.element_desc)
        return BasePage(self.driver)

    # Click the element by name
    def click_element_by_name(self, element, name):
        element.element_id = "//*[@resource-id='{0}'][@text='{1}']".format(element.element_id, name)
        try:
            self.driver.find_element(element.element_type, element.element_id).click()
        except Exception as e:
            print(e)
            print("Can't find " + element.element_desc)
        return BasePage(self.driver)

    # Select element by number
    def select_element_by_number(self, element, number):
        element.element_id = "(//*[@resource-id='{0}'])[{1}]".format(element.element_id, number)
        try:
            self.driver.find_element(element.element_type, element.element_id).click()
        except Exception as e:
            print(e)
            print("Can't find " + element.element_desc)
        return BasePage(self.driver)

