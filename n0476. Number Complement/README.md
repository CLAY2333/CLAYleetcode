
### Number Complement :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/number-complement](https://leetcode-cn.com/problems/number-complement)
- 执行时间/Runtime: 32 ms 
- 内存消耗/Mem Usage: 11.9 MB
- 通过日期/Accept Datetime: 2019-03-23 10:59
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_2=str(bin(num))
        re=''
        for i in num_2[2:len(num_2)]:
            if(i=='1'):
                re+='0'
            else:
                re+='1'
        result=int(re,2)
        return result

```
