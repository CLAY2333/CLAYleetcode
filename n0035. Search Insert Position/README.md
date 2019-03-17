
### Search Insert Position :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/search-insert-position](https://leetcode-cn.com/problems/search-insert-position)
- 执行时间/Runtime: 16 ms 
- 内存消耗/Mem Usage: 11.3 MB
- 通过日期/Accept Datetime: 2019-03-05 11:56
```python
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

```
