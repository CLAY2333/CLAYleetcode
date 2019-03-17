
### Remove Element :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/remove-element](https://leetcode-cn.com/problems/remove-element)
- 执行时间/Runtime: 20 ms 
- 内存消耗/Mem Usage: 10.9 MB
- 通过日期/Accept Datetime: 2019-03-05 11:23
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
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

```
