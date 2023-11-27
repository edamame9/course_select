# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 14:19:58 2023

@author: d1090654
"""
import sys
sys.path.append("C:/course_select")
def modify(professor,course_des,course_goal):
    file_path = "course_list.txt"
    print("---------修改模式---------")
    print("可修改課程描述，如下所指內容:")
    print(course_des)
    print("可修改課程目標，如下所指內容:")
    print(course_goal)
    m = input("按'1'修改課程描述，按'2'修改課程目標，按其他任意建退出修改模式:")
    courses = []
    s = []
    if m == '1':
        print("--選擇修改課程描述--")
        m_content = input("輸入修改內容，內容不可為空:")
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                course_data = line.strip().split()
                courses.append(course_data)
        i = 0
        print(courses[0][0])
        for i in range(len(courses)):
            j = 0
            for j in range(len(courses[i])):
                if courses[i][j] == course_des:
                    courses[i][j] = m_content
                    course_des = m_content
    elif m == '2':
        print("--選擇修改課程目標--")
        m_content = input("輸入修改內容，內容不可為空:")
        for line in file:
            course_data = line.split().split()
            print(course_data)
            if course_data == course_des:
                course_data = m_content
                course_goal = m_content
            courses.append(course_data)
    else:
        print("---------退出修改模式---------")
        return 0
    content = ""
    for i in range(len(courses)):
        j = 0
        for j in range(len(courses[i])):
            if(((j+1) %8 )!= 0):
                content = content +str(courses[i][j])+ "\t"
            else:
                content = content +str(courses[i][j])
            j += 1
        if(i != len(courses)-1):
            content = content +"\n"
        i += 1
    wfile = open(file_path,"w",encoding="utf-8")
    wfile.write(content)
    wfile.close()
    print("--修改完成--")
    modify(professor, course_des, course_goal)
    