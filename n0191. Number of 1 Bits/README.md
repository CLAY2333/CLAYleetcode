
### Number of 1 Bits :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/number-of-1-bits](https://leetcode-cn.com/problems/number-of-1-bits)
- 执行时间/Runtime: 24 ms 
- 内存消耗/Mem Usage: 11.8 MB
- 通过日期/Accept Datetime: 2019-11-19 20:29
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num=0
        n=bin(n)
        for i in n:
            if i=='1':
                num+=1
        return num

```
