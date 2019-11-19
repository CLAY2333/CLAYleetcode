
### Single Number :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/single-number](https://leetcode-cn.com/problems/single-number)
- 执行时间/Runtime: 112 ms 
- 内存消耗/Mem Usage: 16.4 MB
- 通过日期/Accept Datetime: 2019-11-12 17:11
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def singleNumber(self, nums:list) -> int:
        hash={}
        for i in nums:
            if i not in hash:
                hash[i]=1
            else:
                hash.pop(i)
        return hash.popitem()[0]

```
