# -*- encoding: utf-8 -*-

import configparser

class ParseConFile(object):
    def __init__(self, file_path):
        self.file = file_path
        self.conf = configparser.ConfigParser()
        self.conf.read(self.file, encoding='utf-8')

    def get_all_sections(self):
        return self.conf.sections()

    def get_all_options(self, section):
        try:
            return self.conf.options(section)
        except configparser.NoSectionError as e:
            print(e)

    def get_str_value(self, section, option) -> str:
        try:
            return self.conf.get(section, option)
             
        except configparser.NoOptionError as e1:
            print(e1)
        except configparser.NoSectionError as e2:
            print(e2)
    
    def get_bool_value(self, section, option) -> bool:
        try:
            return self.conf.getboolean(section, option)
        except configparser.NoOptionError as e1:
            print(e1)
        except configparser.NoSectionError as e2:
            print(e2)

    def get_int_value(self, section, option) -> int:
        try:
            return self.conf.getint(section, option)
        except configparser.NoOptionError as e1:
            print(e1)
        except configparser.NoSectionError as e2:
            print(e2)

    def get_option_value(self, section) -> dict:
        try:
            return dict(self.conf.items(section))
        except configparser.NoSectionError as e:
            print(e)
