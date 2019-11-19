
### Missing Number :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/missing-number](https://leetcode-cn.com/problems/missing-number)
- 执行时间/Runtime: 156 ms 
- 内存消耗/Mem Usage: 15 MB
- 通过日期/Accept Datetime: 2019-11-19 10:03
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def missingNumber(self, nums: list) -> int:
        S=sum(nums)
        L=len(nums)
        return int((L*(L+1)/2))-S

```
