
### 青蛙跳台阶问题  LCOF :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof](https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof)
- 执行时间/Runtime: 40 ms 
- 内存消耗/Mem Usage: 13.5 MB
- 通过日期/Accept Datetime: 2020-02-26 15:45
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def numWays(self, n: int) -> int:
        c=0
        a=0
        b=1
        if n==0:
            return 1
        for i in range(n):
            c=a+b
            a=b
            b=c
        return c%1000000007

```
