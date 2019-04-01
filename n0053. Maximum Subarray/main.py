// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def maxSubArray(self, nums: list) -> int:
        if(len(nums)==0):
            return 0
        re=nums[0]
        sum_temp=0
        for index,value in enumerate(nums):
            sum_temp=max(value,sum_temp+value)
            re=max(sum_temp,re)
        return re
