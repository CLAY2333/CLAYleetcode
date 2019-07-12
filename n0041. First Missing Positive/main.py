// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def firstMissingPositive(self, nums: list) -> int:
        if 1 not in nums:
            return 1
        if nums==[1]:
            return 2
        n=len(nums)
        for index,value in enumerate(nums):
            if value<=0 or value>n:
                nums[index]=1
        for index,value in enumerate(nums):
            if(abs(value)==n):
                nums[0]=nums[0]*-1
            else:
                nums[abs(value)]=abs(nums[abs(value)])*-1
        for index,value in enumerate(nums):
            if index==0:
                continue
            if value<=0:
                continue
            else:
                return index
        if nums[0]>0:
            return n
        else:
            return n+1
