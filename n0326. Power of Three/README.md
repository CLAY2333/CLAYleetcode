
### Power of Three :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/power-of-three](https://leetcode-cn.com/problems/power-of-three)
- 执行时间/Runtime: 432 ms 
- 内存消耗/Mem Usage: 10.7 MB
- 通过日期/Accept Datetime: 2019-03-18 16:52
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0: return False
        temp=math.log10(n)/math.log10(3)
        temp=temp%1
        if(temp==0):
            return True
        else:
            return False

```
