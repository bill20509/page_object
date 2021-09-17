import imagehash
import subprocess
import os
import io
import re
import json
import traceback
from .resourceid import ElementID
from pymediainfo import MediaInfo
from PIL import Image


def pass_prompt(prompt):
    print("[Pass] " + prompt + " Pass")


def fail_prompt(prompt):
    print("[Failed] " + prompt + " Failed")


def get_latest_filename(ycp):
    command = r'adb -s {} shell "ls -t sdcard/DCIM/YouCam\ Perfect/ | head -1"'.format(ycp.cap["deviceName"])
    return os.popen(command).read().strip()


def pulled_file(file_name):
    path = r"sdcard/DCIM/YouCam Perfect/"
    dest_path = "./src/pulled_from_device/"
    dest_name = "latest.png"
    command = "adb pull " + "\"" + path + file_name + "\" " + dest_path + dest_name
    # print(command)
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        traceback.print_exc()


def pulled_from_dcim(img_name):
    command = "adb pull " + "\"" + "/sdcard/DCIM/ScreenShots/" + img_name + "\" " + "./sample_output/" + img_name
    os.system(command)


def screen_shot(src_name):
    img_name = str(src_name) + ".jpg"
    img_name = img_name.replace(" ", "_")
    img_name = img_name.replace("&", "_")
    os.system("adb shell screencap -p /sdcard/DCIM/ScreenShots/" + img_name)


# def judge():
#     input_hash = imagehash.dhash(Image.open("./pulled_from_device/latest.png"))
#     dest_hash = imagehash.dhash(Image.open("./sample_output/sample.jpg"))
#     print(input_hash - dest_hash)
#     if input_hash == dest_hash:
#         pass_prompt("image hash judge")
#     else:
#         fail_prompt("image hash judge")

def get_element(driver, element_id, prompt):
    try:
        return driver.find_element_by_id(element_id)
    except:
        traceback.print_exc()
        fail_prompt(prompt)
    else:
        pass_prompt(prompt)


def check_element_exist(driver, element_id, prompt):
    try:
        driver.find_element_by_id(element_id)
    except:
        fail_prompt(prompt)
    else:
        pass_prompt(prompt)


def button_click(driver, element_id, prompt):
    try:
        driver.find_element_by_id(element_id).click()
    except:
        traceback.print_exc()
        fail_prompt(prompt)
    else:
        pass_prompt(prompt)


def button_click_xpath(driver, element_xpath, prompt):
    try:
        driver.find_element_by_xpath(element_xpath).click()
    except:
        traceback.print_exc()
        fail_prompt(prompt)
    else:
        pass_prompt(prompt)


def swipe_down():
    command = "adb shell input swipe 500 1500 500 500"
    os.system(command)


def tap_middle():
    command = "adb shell input tap 500 1500"
    os.system(command)
    print("tap middle")


def clear_ycp_data():
    command = "adb shell pm clear \"com.cyberlink.youperfect\""
    os.system(command)
    print("clear ycp data")


def camera_info_parse(info):
    info_dict = {}
    buf = io.StringIO(info)
    lines = buf.readlines()
    for line in lines:
        line = re.sub("[:,\n]", "", line.strip())
        print(line)
        line_list = line.split(' ')
        info_dict[line_list[0]] = line_list[1]
    print(info_dict)
    return info_dict


def get_camera_info(ycp_driver):
    info = ycp_driver.find_element_by_id(ElementID.camera_info)
    return info.text


def get_device_model():
    result = subprocess.run(['adb', "shell", "getprop", "ro.product.model"], stdout=subprocess.PIPE)
    return result.stdout.decode("utf-8").strip()


def get_device_api_version():
    result = subprocess.run(['adb', "shell", "getprop", "ro.build.version.sdk"], stdout=subprocess.PIPE)
    return int(result.stdout.decode("utf-8").strip())


def get_device_merory():
    result = subprocess.run(['adb', "shell", "cat", " /proc/meminfo", "|",  "grep", "MemTotal"], stdout=subprocess.PIPE)
    info_list = result.stdout.decode("utf-8").split()
    return int(info_list[1]) / 2 ** 20
    # by type = num, GB


def get_device_brand():
    result = subprocess.run(['adb', "shell", "getprop", "ro.product.brand"], stdout=subprocess.PIPE)
    return result.stdout.decode("utf-8").strip()


def get_hardware_info():
    info = dict()
    info["device_model"] = get_device_model()
    info["device_api"] = get_device_api_version()
    info["device_memory"] = get_device_merory()
    info["device_brand"] = get_device_brand()
    return info

def brand_block():
    with open('./src/block_list.json') as f:
        block_list = json.load(f)
    device_brand = get_device_brand()
    device_model = get_device_model()
    if not (device_brand in block_list):
        return False
    if device_model in block_list[device_brand]:
        return True
    else:
        return False


def check_element_attribute(ycp_driver, element_id, attr, value):
    # print("attr is" + ycp_driver.find_element_by_id(element_id).get_attribute(attr))
    if ycp_driver.find_element_by_id(element_id).get_attribute(attr) == value:
        pass_prompt(element_id + " Tab Check")
    else:
        fail_prompt(element_id + " Tab Check")


def check_value_equal(ycp_driver, element_id, value):
    element_value = ycp_driver.find_element_by_id(element_id).text
    if float(element_value) == float(value):
        pass_prompt(element_id + " Value equal Check")
    else:
        print("{} is {}, should be {}".format(element_id, float(element_value),  float(value)))
        fail_prompt(element_id + " Value equal Check")


def check_string_name(ycp_driver, element_id, cmp):
    string_name = ycp_driver.find_element_by_id(element_id).text
    if str(string_name) == str(cmp):
        pass_prompt(string_name + " module name check")
    else:
        print("{} is {}, should be {}".format(element_id, float(string_name), float(cmp)))
        fail_prompt(element_id + " Value equal Check")