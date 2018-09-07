#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-Author-Lian

import os
import sys
import platform

if platform.system() == "Windows":
    BASE_DIR = "\\".join(os.path.abspath(os.path.dirname(__file__)).split("\\")[:-1])

else:
    BASE_DIR = "/".join(os.path.abspath(os.path.dirname(__file__)).split("/")[:-1])

sys.path.insert(0,BASE_DIR)

from conf import settings
from modules import models
from modules import actions


if __name__ == '__main__':
    obj = actions.Action()
    obj.func()



