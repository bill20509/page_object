# 工具包
from selenium.webdriver.common.by import By


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    # Deep link
    def deeplink(self, page_link, package_name):
        print("Go to: " + page_link)
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
            print("Cant' find " + element.element_desc)
        return BasePage(self.driver)

    def find_element(self, identify, element): # check element is exist or not
        flag = None
        try:
            if identify == "id":
                self.driver.find_element(By.ID, element)
            elif identify == "xpath":
                self.driver.find_element(By.XPATH, element)
            elif identify == "class":
                self.driver.find_element(By.CLASS_NAME, element)
            elif identify == "link text":
                self.driver.find_element(By.LINK_TEXT, element)
            elif identify == "partial link text":
                self.driver.find_element(By.PARTIAL_LINK_TEXT, element)
            elif identify == "name":
                self.driver.find_element(By.NAME, element)
            elif identify == "tag name":
                self.driver.find_element(By.TAG_NAME, element)
            elif identify == "css selector":
                self.driver.find_element(By.CSS_SELECTOR, element)
            flag = True
            print(element + ' is exist')
        except Exception:
            flag = False
            print(element + ' is not exist')
        finally:
            return self
