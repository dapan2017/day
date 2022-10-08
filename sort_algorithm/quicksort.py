# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 09:50:59 2018

@author: fengxue
"""
def Quicksort(arr):
    if len(arr)<2:return arr
    else:
        left=[]
        right=[]
        temp=[]
        temps=arr[0]
        l=len(arr)
        for i in range(l):
            if arr[i]<temps:left.append(arr[i])
            if arr[i]>temps:right.append(arr[i])
            if arr[i]==temps:temp.append(arr[i])
    return Quicksort(left)+temp+Quicksort(right)
    
print(Quicksort([43,32,4,35,46,5,5,34,654,7,65,6,534654,543])) 