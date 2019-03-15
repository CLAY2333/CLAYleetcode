
### Plus One :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/plus-one](https://leetcode-cn.com/problems/plus-one)
- 执行时间/Runtime: 16 ms 
- 内存消耗/Mem Usage: 10.8 MB
- 通过日期/Accept Datetime: 2019-03-13 21:51
```python
// Author: Netcan @ https://github.com/netcan/Leetcode-Rust
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if(len(digits)==1 and digits[0]==9):
            return [1,0]
        lens=len(digits)
        digits[lens-1]=digits[lens-1]+1
        if(digits[lens-1]<10):
            return digits
        for i in range(lens):
            digits[lens-1-i]-=10
            digits[lens-2-i]+=1
            if (digits[lens-2-i] < 10):
                return digits
            if(digits[0]==10):
                digits[0]=0
                digits.insert(0,1)
                return digits

```
