#
# 代码中的类名、方法名、参数名已经指定,请勿修改,直接返回方法规定的值即可
#
# 
# @param numbers int整型一维数组 
# @return int整型
#
'''
描述
给一个长度为 n 的数组,数组中有一个数字出现的次数超过数组长度的一半,请找出这个数字。
例如输入一个长度为9的数组[1,2,3,2,2,2,5,4,2]。由于数字2在数组中出现了5次,超过数组长度的一半,因此输出2。

数据范围:n \le 50000n≤50000,数组中元素的值 0 \le val \le 100000≤val≤10000
要求:空间复杂度:O(1)O(1),时间复杂度 O(n)O(n)

示例1
[1,2,3,2,2,2,5,4,2]
返回值：2
'''
class Solution:
    def MoreThanHalfNum_Solution(self , numbers: list[int]) -> int:
        mp = dict()
        for i in range(len(numbers)):
            if numbers[i] in mp:
                mp[numbers[i]] +=1
            else:
                mp[numbers[i]] = 1
            if mp[numbers[i]] > int(len(numbers)/2):
                return numbers[i]
        return 0

a = [1,2,3,2,2,2,5,4,2]
b = Solution()
print(b.MoreThanHalfNum_Solution(a))