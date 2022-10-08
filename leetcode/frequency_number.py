# -*- coding: utf-8 -*-
'''
数字出现的次数
输入一个包含n个整数的一维数组input，input中的数都在[1,n]之间，请输出每个数出现的次数
要求：时间复杂度为O（n）,且只使用常量额外空间
例1:
输入：[1,2,3,4,4,5,7]
输出：[1,1,1,2,1,0,1]
例2:
输入：[11,7,3,6,4,8,7,11,3,6,9]
输出：[0,0,2,1,0,2,2,1,1,0,2]
'''


def solution(lst):
    number_lst = [0]*len(lst)

    # print(number_lst)
    
    for i in lst:
        number_lst[i - 1] +=1
    return number_lst

if __name__ == '__main__':
    lst = [1,2,3,4,4,5,7]
    sort_lst = list(range(1,len(lst)+1))
    print(sort_lst)
    print(solution(lst))