# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 16:58:29 2018

@author: fengxue
"""

def Insertsort(arr):
    length = len(arr)
    for i in range(1,length):
        x = arr[i]
        for j in range(i,-1,-1):
            # j为当前位置，试探j-1位置
            if x < arr[j-1]:
                arr[j] = arr[j-1]
            else:
                # 位置确定为j
                break
        arr[j] = x
    return arr
print(Insertsort([43,5,65,3455,544,53,4,2,4,543]))