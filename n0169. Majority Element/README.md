
### Majority Element :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/majority-element](https://leetcode-cn.com/problems/majority-element)
- 执行时间/Runtime: 220 ms 
- 内存消耗/Mem Usage: 15.3 MB
- 通过日期/Accept Datetime: 2019-11-25 15:53
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def majorityElement(self, nums: list) -> int:
        if len(nums)==0:
            return 0
        maxtimes=1
        maxnum=nums[0]
        hash={}
        for value in nums:
            if value not in hash:
                hash[value]=1
            else:
                hash[value]+=1
                if hash[value]>maxtimes:
                    maxtimes=hash[value]
                    maxnum=value
        return maxnum

```
