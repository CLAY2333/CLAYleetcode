
### Remove Duplicates from Sorted Array :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array)
- 执行时间/Runtime: 80 ms 
- 内存消耗/Mem Usage: 12.7 MB
- 通过日期/Accept Datetime: 2019-03-05 11:01
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r=0
        if (len(nums) ==0):
            return 0
        nums.append('a')
        for i in range(len(nums)):
            if (len(nums) <= 1):
                nums.pop()
                return 1
            if(nums[r+1]=='a'):
                nums.pop()
                return len(nums)
            if(nums[r]==nums[r+1]):
                del nums[r+1]
                continue
            r+=1
        nums.pop()
        return len(nums)

```