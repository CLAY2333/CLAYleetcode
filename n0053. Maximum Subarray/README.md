
### Maximum Subarray :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/maximum-subarray](https://leetcode-cn.com/problems/maximum-subarray)
- 执行时间/Runtime: 64 ms 
- 内存消耗/Mem Usage: 13.6 MB
- 通过日期/Accept Datetime: 2019-04-01 00:36
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def maxSubArray(self, nums: list) -> int:
        if(len(nums)==0):
            return 0
        re=nums[0]
        sum_temp=0
        for index,value in enumerate(nums):
            sum_temp=max(value,sum_temp+value)
            re=max(sum_temp,re)
        return re

```
