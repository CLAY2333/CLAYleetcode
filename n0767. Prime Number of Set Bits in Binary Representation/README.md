
### Prime Number of Set Bits in Binary Representation :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/prime-number-of-set-bits-in-binary-representation](https://leetcode-cn.com/problems/prime-number-of-set-bits-in-binary-representation)
- 执行时间/Runtime: 356 ms 
- 内存消耗/Mem Usage: 11.2 MB
- 通过日期/Accept Datetime: 2019-03-21 10:10
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        D=[2, 3, 5, 7, 11, 13, 17, 19]
        sum=0
        for i in range(L,R+1):
            if str(bin(i))[2:len(bin(i))].count('1') in D:
                sum+=1
        return sum

```
