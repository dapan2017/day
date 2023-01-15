




class Solution1:
    def judge(self , str:str) -> bool:
        str_1 = str[::-1]
        if str_1 == str:
            return True
        else:
            return False

class Solution2:
    def judge(self , str:str ) -> bool:
        left = 0
        right = len(str) - 1
        while left < right :
            if str[left] == str[right]:
                left +=1
                right -= 1
            else:
                return False
        return True



a = Solution2()
print(a.judge('asdfdfdsafds'))
print(a.judge('asdffdsa'))
