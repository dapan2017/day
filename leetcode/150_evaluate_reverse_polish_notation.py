# -*- coding: utf-8 -*-
"""
根据逆波兰表示法，求表达式的值。

有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

说明：

整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
示例 1：

输入: ["2", "1", "+", "3", "*"]
输出: 9
解释: ((2 + 1) * 3) = 9
示例 2：

输入: ["4", "13", "5", "/", "+"]
输出: 6
解释: (4 + (13 / 5)) = 6
————————————————
版权声明：本文为CSDN博主「暴躁老哥在线刷题」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_32424059/article/details/86994342
"""

def suanshu(a):
    stack=[]
    for token in a :
        if token in ['+','-','*','/']:
            a,b=stack.pop(),stack.pop()
            if token =='+':
                res=a+b
            elif token=='-':
                res=a-b
            elif token=='*':
                res=a*b
            elif token=='/':
                res=a/b
            stack.append(res)
        else:
            stack.append(int(token))
    return stack.pop()
 
print(suanshu(['2','1','+','3','*']))