
### Sqrt(x) :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/sqrtx](https://leetcode-cn.com/problems/sqrtx)
- 执行时间/Runtime: 28 ms 
- 内存消耗/Mem Usage: 10.8 MB
- 通过日期/Accept Datetime: 2019-03-14 14:21
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<2:
            return x
        left=0
        right=x
        while(left<right):
            mid=(left+right)/2
            if((mid*mid)>x):
                right=mid
            else:
                left=mid+1
        return right-1

```
