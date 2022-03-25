import re


class Element:
    def __init__(self, source: str):
        try:
            self.class_name = str(re.findall(r'class="[^"]*"', source)[0]).split("=")[1].strip("\"")
        except:
            self.class_name = ""

        try:
            self.package_name = str(re.findall(r'package="[^"]*"', source)[0]).split("=")[1].strip("\"")
        except:
            self.package_name = ""

        try:
            self.resource_id = str(re.findall(r'resource-id="[^"]*"', source)[0]).split("=")[1].strip("\"")
        except:
            self.resource_id = ""

        try:
            self.clickable = str(re.findall(r'clickable="[^"]*"', source)[0]).split("=")[1].strip("\"")
        except:
            self.clickable = "false"

        try:
            self.long_clickable = str(re.findall(r'long-clickable="[^"]*"', source)[0]).split("=")[1].strip("\"")
        except:
            self.long_clickable = "false"

        try:
            self.scrollable = str(re.findall(r'scrollable="[^"]*"', source)[0]).split("=")[1].strip("\"")
        except:
            self.scrollable = "false"

        try:
            self.text = str(re.findall(r'text="[^"]*"', source)[0]).split("=")[1].strip("\"")
        except:
            self.text = ""

    def __str__(self):
        return self.class_name + ": " + self.resource_id + "clickable :" + self.clickable + "long-clickable :" + self.long_clickable

    def __repr__(self):
        return self.class_name + ": " + self.resource_id + "clickable :" + self.clickable + "long-clickable :" + self.long_clickable