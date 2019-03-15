// Author: Netcan @ https://github.com/netcan/Leetcode-Rust
class Solution(object):
    def searchInsert(self, nums, target):
        count=nums.count(target)
        if(count!=0):
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
