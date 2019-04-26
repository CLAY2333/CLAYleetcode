
### Unique Paths :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/unique-paths](https://leetcode-cn.com/problems/unique-paths)
- 执行时间/Runtime: 56 ms 
- 内存消耗/Mem Usage: 13 MB
- 通过日期/Accept Datetime: 2019-04-25 14:16
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if(m==1 or n==1):
            return 1
        m-=1
        n-=1
        temp_m=m+n
        temp_n=n
        sum_m=1
        sum_n=1
        for i in range(n):
            sum_m*=temp_m
            sum_n*=temp_n
            temp_m-=1
            temp_n-=1
        return sum_m//sum_n


```
