// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def removeDuplicates(self, nums: list) -> int:
        delete_list=[]
        for index,value in enumerate(nums):
            if index>1 and value==nums[index-2]:
                delete_list.insert(0,index)
        for i in delete_list:
            nums.pop(i)
        return len(nums)
