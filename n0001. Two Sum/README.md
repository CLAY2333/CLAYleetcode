
### Two Sum :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/two-sum](https://leetcode-cn.com/problems/two-sum)
- 执行时间/Runtime: 40 ms 
- 内存消耗/Mem Usage: 11.8 MB
- 通过日期/Accept Datetime: 2019-02-21 16:20
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def twoSum(self, num, target):
        dict = {}
        for i in xrange(len(num)):
            x = num[i]
            if target-x in dict:
                return (dict[target-x], i)
            dict[x] = i

```
