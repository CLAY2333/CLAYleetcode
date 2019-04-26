// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def sortColors(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index=-1
        times=0
        while(times<len(nums)):
            index+=1
            if nums[index]==0:
                nums.pop(index)
                nums.insert(0,0)
            elif nums[index]==2:
                nums.pop(index)
                index-=1
                nums.append(2)
            times+=1
