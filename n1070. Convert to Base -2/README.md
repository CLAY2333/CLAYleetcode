
### Convert to Base -2 :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/convert-to-base-2](https://leetcode-cn.com/problems/convert-to-base-2)
- 执行时间/Runtime: 52 ms 
- 内存消耗/Mem Usage: 12.9 MB
- 通过日期/Accept Datetime: 2019-04-01 14:39
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def baseNeg2(self, N: int) -> str:
        if(N==0 or N==1):
            return str(N)
        re_str=''
        while 1:
            temp_1=int(N%(-2))
            re_str+=str(abs(temp_1))
            N=(N+temp_1)//-2
            if(N==0):
                L=list(re_str)
                L.reverse()
                return ''.join(L)

```
