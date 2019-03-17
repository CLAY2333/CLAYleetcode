// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def searchInsert(self, nums, target):
        count=nums.count(target)
        if(count!=0):
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
