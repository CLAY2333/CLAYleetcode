// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index=0
        _index=0
        zero_nums=len(nums)-len(list(set(nums)))+1
        for index,value in enumerate(nums):
            if nums[zero_index]!=0:
                zero_index+=1
                continue
            if value!=0:
                nums[zero_index]=value
                nums[index]=0
                zero_index+=1
                continue
