from lib.ycp import Ycp
from appium import webdriver
from lib.ycp_gui import UI, Camera, Tutorial, Launcher, Setting, Editor
from lib import ycp_utility
import json
from pathlib import Path
import os

ycp = Ycp()
el = ycp.driver.find_element_by_image("./start_button.png")