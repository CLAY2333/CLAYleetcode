// Author: Netcan @ https://github.com/netcan/Leetcode-Rust
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        num=nums.count(val)
        for i in range(num):
            nums.remove(val)

        return len(nums)
