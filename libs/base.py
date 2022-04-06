# 工具包
import re
import time
from wand.image import Image

from selenium.webdriver.common.by import By


class BasePage(object):
    DEBUG_PERFORMANCE = False

    def __init__(self, driver):
        self.driver = driver

    # Deep link
    def deeplink(self, page_link, package_name=""):
        if(package_name == ""):
            package_name = self.driver.caps["appPackage"]
        self.driver.execute_script(
            "mobile: deepLink",
            {
                "url": page_link,
                "package": package_name
            }
        )
        return self

    # take screenshot in current page
    def screenshot(self, screenshotname=None):
        photopath = 'screenshot/'
        screenshotName = screenshotname
        self.driver.save_screenshot(photopath + screenshotName)
        return BasePage(self.driver)

    # Click button (element id)
    def click_element(self, element):
        try:
            self.driver.find_element(
                element.element_type, element.element_id).click()
        except Exception as e:
            print(e)
            print("Can't find " + element.element_desc)
        return BasePage(self.driver)

    # Click the element by name (resource-id and text)
    def click_element_by_name(self, element, name):
        element.element_id = "//*[@resource-id='{0}'][@text='{1}']".format(
            element.element_id, name)
        try:
            self.driver.find_element(
                element.element_type, element.element_id).click()
        except Exception as e:
            print(e)
            print("Can't find " + element.element_desc)
        return BasePage(self.driver)

    # Select element by number (resource-id and index[])
    def select_element_by_number(self, element, number):
        element.element_id = "(//*[@resource-id='{0}'])[{1}]".format(
            element.element_id, number)
        try:
            self.driver.find_element(
                element.element_type, element.element_id).click()
        except Exception as e:
            print(e)
            print("Can't find " + element.element_desc)
        return BasePage(self.driver)

    def adjust_slider_to_value(self, element, target_value):
        is_vertical = element.size["height"] > element.size["width"]
        if is_vertical:
            self.__adjust_vertical_slider_to_value(element, target_value)
        else:
            self.__adjust_horizontal_slider_to_value(element, target_value)

    def __adjust_horizontal_slider_to_value(self, element, target_value):
        thumb_size = 18
        width = element.size["width"] - thumb_size
        height = element.size["height"]
        print("width %d, height %d" % (width, height))
        current_value = self.get_slider_value(element)
        target_value = float(target_value)
        print("current_value %f, target_value %f" %
              (current_value, target_value))

        if current_value == target_value:
            return

        start_x = thumb_size / 2
        from_x = start_x + width * current_value
        to_x = start_x + width * target_value
        self.driver.execute_script("mobile:dragFromToForDuration",
                                   {"duration": 0.01, "element": element, "fromX": from_x,
                                    "fromY": height * 0.5, "toX": to_x, "toY": height * 0.5})
        current_value = self.get_slider_value(element)
        print("current_value %f, target_value %f" %
              (current_value, target_value))

        loop = 0
        while current_value != target_value and loop < 10:
            offset = 5
            from_x = start_x + width * current_value
            if current_value > target_value:
                to_x = to_x - offset
            else:
                to_x = to_x + offset
            self.driver.execute_script("mobile:dragFromToForDuration",
                                       {"duration": 0.01, "element": element, "fromX": from_x,
                                        "fromY": height * 0.5, "toX": to_x, "toY": height * 0.5})
            current_value = self.get_slider_value(element)
            print("current_value %f, target_value %f" %
                  (current_value, target_value))
            loop += 1

    def __adjust_vertical_slider_to_value(self, element, target_value):
        thumb_size = 18
        width = element.size["width"]
        height = element.size["height"] - thumb_size
        print("width %d, height %d" % (width, height))
        current_value = self.get_slider_value(element)
        target_value = float(target_value)
        print("current_value %f, target_value %f" %
              (current_value, target_value))

        if current_value == target_value:
            return

        start_y = height - thumb_size / 2
        from_y = start_y - height * current_value
        to_y = start_y - height * target_value
        self.driver.execute_script("mobile:dragFromToForDuration",
                                   {"duration": 0.01, "element": element, "fromX": width * 0.5,
                                    "fromY": from_y, "toX": width * 0.5, "toY": to_y})
        current_value = self.get_slider_value(element)
        print("current_value %f, target_value %f" %
              (current_value, target_value))

        loop = 0
        while current_value != target_value and loop < 10:
            offset = 5
            from_y = start_y - height * current_value
            if current_value > target_value:
                to_y = to_y + offset
            else:
                to_y = to_y - offset
            self.driver.execute_script("mobile:dragFromToForDuration",
                                       {"duration": 0.01, "element": element, "fromX": width * 0.5,
                                        "fromY": from_y, "toX": width * 0.5, "toY": to_y})
            current_value = self.get_slider_value(element)
            print("current_value %f, target_value %f" %
                  (current_value, target_value))
            loop += 1

    def get_slider_value(self, element):
        return int(re.search(r'\d+', element.get_attribute("value")).group())/100

    def swipe_gesture(self, element, fromx=float, tox=float, fromy=float, toy=float, duration=int):
        width = element.size["width"]
        height = element.size["height"]
        print("width %d, height %d" % (width, height))

        from_x = width * fromx
        to_x = width * tox
        from_y = height * fromy
        to_y = height * toy
        self.driver.execute_script("mobile:dragFromToForDuration",
                                   {"duration": duration, "element": element, "fromX": from_x,
                                    "fromY": from_y, "toX": to_x, "toY": to_y})

    def __app_document_path(self):
        desired_caps = self.driver.session
        bundle_id = desired_caps["bundleId"]
        return "@" + bundle_id + ":documents/"

    def delete_folder_in_app_document(self, folder):
        current_time = time.time()
        path = self.__app_document_path() + folder
        try:
            self.driver.execute_script(
                "mobile:deleteFolder", {"remotePath": path})
        except:
            print("deleteFolder: Folder not exist: " + path)
        if self.DEBUG_PERFORMANCE:
            print("[%s] execution time = %s (s)" % (
                self.delete_folder_in_app_document.__name__, (time.time() - current_time)))

    def push_file_to_app_document(self, file_path):
        current_time = time.time()
        path = self.__app_document_path() + file_path
        self.driver.push_file(path, None, file_path)
        if self.DEBUG_PERFORMANCE:
            print("[%s] execution time = %s (s)" % (
                self.push_file_to_app_document.__name__, (time.time() - current_time)))

    def pull_file_from_app_document(self, file_path):
        current_time = time.time()
        path = self.__app_document_path() + file_path
        file = self.driver.pull_file(path)
        if self.DEBUG_PERFORMANCE:
            print("[%s] execution time = %s (s)" % (
                self.pull_file_from_app_document.__name__, (time.time() - current_time)))
        return file

    def pull_folder_from_app_document(self, file_path):
        current_time = time.time()
        path = self.__app_document_path() + file_path
        file = self.driver.pull_folder(path)
        if self.DEBUG_PERFORMANCE:
            print("[%s] execution time = %s (s)" % (
                self.pull_folder_from_app_document.__name__, (time.time() - current_time)))
        return file

    def compare_photo(self, basephotoName=None, currentphotoName=None, diffName=None, resultmatch=0, threshold=0.10):
        basephoto = 'basephoto/' + basephotoName
        currentphoto = 'currentphoto/' + currentphotoName
        diffresult = 'diffphoto/' + diffName
        with Image(filename=basephoto) as base:
            with Image(filename=currentphoto) as img:
                base.fuzz = base.quantum_range * threshold
                result_image, result_metric = base.compare(img, 'absolute')
                with result_image:
                    result_image.save(filename=diffresult)
                print(result_metric)
                assert float(result_metric) == resultmatch
