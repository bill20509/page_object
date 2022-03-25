# 工具包

class functions(object):
    def __init__(self, driver):
        self.driver = driver

    # take screenshot in current page
    def current_screenshot(self, screenshotname=None):
        currentphoto = 'currentphoto/'
        screenshotName = screenshotname
        self.driver.save_screenshot(currentphoto + screenshotName)