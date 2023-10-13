# -*- encoding: utf-8 -*-
import os


class BaseIpmi(object):
    def __init__(self, ipmi_add, user, password, islocal=False) -> None:
        self.ipmi_add = ipmi_add
        self.user = user
        self.password = password
        self.islocal = islocal

    def ipmitool_is_ok(self):
        return os.system('ipmitool --help') == 0
    
    def ipmitool_version(self, version):
        pass

    


