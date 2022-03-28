from enum import Enum


class Element:
    def __init__(self, element_id, element_type, desc):
        self.element_id = element_id
        self.element_type = element_type
        self.element_desc = desc

