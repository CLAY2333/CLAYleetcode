
### Climbing Stairs :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/climbing-stairs](https://leetcode-cn.com/problems/climbing-stairs)
- 执行时间/Runtime: 24 ms 
- 内存消耗/Mem Usage: 10.8 MB
- 通过日期/Accept Datetime: 2019-03-14 15:23
```python
// Author: Netcan @ https://github.com/netcan/Leetcode-Rust
class Solution(object):
    D = {'test': -999}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        D=self.D
        if str(n) in D.keys():
            return D[str(n)]
        if(n==1 or n==0):
            return 1
        if(n==2):
            return 2
        if(n==3):
            return 3
        D[str(n)]=self.climbStairs(n-1)+self.climbStairs(n-2)
        return D[str(n)]

```
