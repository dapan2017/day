#
# 代码中的类名、方法名、参数名已经指定,请勿修改,直接返回方法规定的值即可
'''
描述
输入一个升序数组 array 和一个数字S,在数组中查找两个数,使得他们的和正好是S,如果有多对数字的和等于S,返回任意一组即可,如果无法找出这样的数字,返回一个空数组即可。

  
示例1
输入：[1,2,4,7,11,15],15
返回值：[4,11]
说明：
返回[4,11]或者[11,4]都是可以的       

示例2
输入：[1,5,11],10
返回值：[]
说明：
不存在,返回空数组     

示例3
输入：[1,2,3,4],5
返回值：[1,4]
说明：
返回[1,4],[4,1],[2,3],[3,2]都是可以的   

示例4
输入：[1,2,2,4],4
返回值：[2,2]
'''
# 
# @param array int整型一维数组 
# @param sum int整型 
# @return int整型一维数组
#
import numpy as np 
import datetime

l1 = [1,2,4,7,11,15],15
l2 = [1,5,11],10
l3 = [1,2,3,4],5
l4 = [1,2,2,4],4
l = [l1,l2,l3,l4]
class Solution:
    def FindNumbersWithSum(self , array: list[int], sum: int) -> list[int]:
        cha = sum - np.array(array) 
        for i in cha:
            if i in array:
                return [i,sum - i] 
        # write code here


start = datetime.datetime.now()

a = Solution()
for i in l:
    print(i)
    print(a.FindNumbersWithSum(i[0],i[1]))

end = datetime.datetime.now()
print('totally time is ' ,end - start)

class Solution2:
    def FindNumbersWithSum(self , array: list[int], sum: int) -> list[int]:
        left,right = 0 , len(array)-1
        while left < right :
            while array[left] + array[right] == sum:
                return [array[left],array[right]]
            while array[left] + array[right] < sum:
                left +=1
            while array[left] + array[right] > sum:
                right -= 1
        return []
start = datetime.datetime.now()

a = Solution2()
for i in l :
    print(a.FindNumbersWithSum(i[0],i[1]))

end = datetime.datetime.now()
print('totally time is ' ,end - start)     