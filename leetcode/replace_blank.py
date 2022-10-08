# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 15:59:51 2018
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
@author: fengxue
"""

def Replace_blank(string):
    new_string=''
    for i in string:
        if i!=' ':
            new_string+=i
        elif i==' ':
            new_string+='%20'
    return new_string
print(Replace_blank('we are happy'))