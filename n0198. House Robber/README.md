
### House Robber :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/house-robber](https://leetcode-cn.com/problems/house-robber)
- 执行时间/Runtime: 44 ms 
- 内存消耗/Mem Usage: 13.7 MB
- 通过日期/Accept Datetime: 2019-09-24 17:51
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def rob(self, nums: list) -> int:
        D={}
        preMax=0
        nowMax=0
        for index,value in enumerate(nums):
            temp=nowMax
            nowMax=max(preMax+value,nowMax)
            preMax=temp
        return max(preMax,nowMax)

```
