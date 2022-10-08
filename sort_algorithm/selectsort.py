# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 16:02:08 2018

@author: fengxue
"""
def Selectsort(s): 
    for i in range(0, len(s) - 1):
        index = i
        for j in range(i + 1, len(s)):
            if s[index] > s[j]:
                index = j
        s[i], s[index] = s[index], s[i]
    return s
           
print(Selectsort([34,5,87,3,56,45,432,4,65,6,3]))