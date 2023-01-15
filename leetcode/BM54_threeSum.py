
class Solution:
    def threeSum(self , num) :
        num=sorted(num)
        res=[]
        num_len=len(num)
        for idx in range(len(num)-2):
            left=idx+1
            right=num_len-1
            while left<right:
                if num[idx]+num[left]+num[right]==0 and [num[idx],num[left],num[right]] not in res:
                    res.append([num[idx],num[left],num[right]])
                elif num[idx]+num[left]+num[right]>0:
                    right-=1
                else:
                    left+=1
        return res