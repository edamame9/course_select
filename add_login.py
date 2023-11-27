# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 15:06:37 2023

@author: d1090654
"""

import numpy as np
import sys
import globals

user_f = open("C:/course_select/User_list.txt","r+",encoding="utf-8")
# a = "AAA"
# user_f.write(a)
# user_f.close()
class User():
    def __init__(self,uid,pw,name):
        self.uid = uid
        self.pw = pw
        self.name = name
def login():
    print("Enter your id and passward:")
    s = user_f.read().split("\n")
    info = input().split()
    if(len(info) > 2 or len(info) < 2):
        print("Must input a set of id and a set of password.")
        return 0
    globals.uid = info[0]
    upw = info[1]
    for i in range(len(s)):
        unit = s[i].split()
        user = User(unit[0],unit[1],unit[2])
        if(globals.uid == user.uid and upw == user.pw):
            if globals.uid[0] == 'D':
                globals.state = 1
            elif globals.uid[0] == 'T':
                globals.state = 2
            print("login successfully!")
            return 1
        # print(user.name)
        # print(user.uid)
        # print(user.pw)
    print("ERROR! Wrong user id or password.")
    login()
login()
