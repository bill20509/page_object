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
    command = r'adb {} shell "ls -t sdcard/DCIM/YouCam\ Perfect/ | head -1"'.format(ycp.cap["deviceName"])
    return os.popen(command).read().strip()


def pulled_latest_file():
    img_name = get_latest_filename()
    path = r"sdcard/DCIM/YouCam Perfect/"
    dest_path = "./src/pulled_from_device/"
    dest_name = "latest.png"
    command = "adb pull " + "\"" + path + img_name + "\" " + dest_path + dest_name
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
    command = "adb shell input swipe 500 1500 100 100"
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


def output_limit_judge(quality):
    # output size high < 1600:
    if quality == "High":
        pulled_latest_file()
        media_info = MediaInfo.parse("./pulled_from_device/latest.png")
        image_track = media_info.image_tracks[0]
        memory = get_device_merory()
        print(str(image_track.width) + str(image_track.height))
        if memory < 0.8:
            if max(int(image_track.width), int(image_track.height)) > 1024:
                fail_prompt(quality + " quality (<1024)")
            else:
                pass_prompt(quality + " quality (<1024)")
        else:
            if max(int(image_track.width), int(image_track.height)) > 1600:
                fail_prompt(quality + " quality (<1600)")
            else:
                pass_prompt(quality + " quality (<1600)")
    elif quality == "Ultra":
        pulled_latest_file()
        media_info = MediaInfo.parse("./pulled_from_device/latest.png")
        image_track = media_info.image_tracks[0]
        print(str(image_track.width) + str(image_track.height))
        if max(int(image_track.width), int(image_track.height)) > 3200:
            fail_prompt(quality + " quality (<3200)")
        else:
            pass_prompt(quality + " quality (<3200)")
    elif quality == "Smart":
        pulled_latest_file()
        media_info = MediaInfo.parse("./pulled_from_device/latest.png")
        image_track = media_info.image_tracks[0]
        print(str(image_track.width) + str(image_track.height))
        if get_device_api_version() > 23:
            if max(int(image_track.width), int(image_track.height)) > 6144:
                fail_prompt(quality + " quality (<6144)")
            else:
                pass_prompt(quality + " quality (<6144)")
        else:
            if max(int(image_track.width), int(image_track.height)) > 4096:
                fail_prompt(quality + " quality (<4096)")
            else:
                pass_prompt(quality + " quality (<4096)")

    # block_list = {"xiaomi": "Redmi Note 7"}
    # info_dict = ycp_utility.camera_info_parse(info)
    # device_model = ycp_utility.get_device_model()
    # device_os = ycp_utility.get_device_os_version()
    # memory = ycp_utility.get_device_merory()
    # memory = (int(memory) / (2 ** 20))
    # device_brand = ycp_utility.get_device_brand()
    #
    # res = info_dict["Cam"].split("x")
    # preview_max_length = max(res[0], res[1])
    # print(preview_max_length)
    # if preview_max_length > 2000:
    #     print("error error")
    #
    #
    # if memory < 1:
    #     print("<1")
    # elif memory >= 1 and memory < 2:
    #     print("1~2")
    # elif memory >= 2:
    #     print(">2")
    # else:
    #     print("error")
    # if block_list[device_brand] == device_model:
    #     print("block!!!")
    # else:
    #     print("don't block")


# info = open("camera_info.info")
# print(info.text())
# info.close()

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