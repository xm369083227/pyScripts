#author:xm
#coding:utf-8

import sys,os
base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,base)
#print(sys.path)
from modules import models
from modules.actions import Action


if __name__ == "__main__":
    obj = Action()
    obj.run()