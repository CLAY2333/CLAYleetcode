
### Divide Two Integers :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/divide-two-integers](https://leetcode-cn.com/problems/divide-two-integers)
- 执行时间/Runtime: 56 ms 
- 内存消耗/Mem Usage: 13.2 MB
- 通过日期/Accept Datetime: 2019-04-02 23:47
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if(dividend==0):#判断除数是否为0
            return 0
        if(abs(dividend)<abs(divisor)):#如果除数大于被除数则直接返回0
            return 0
        ru=(dividend^divisor)<0#判断符号
        dividend=abs(dividend)
        divisor=abs(divisor)
        if(abs(divisor)==1 and abs(dividend)<=2147483647):
            if(ru):
                return abs(dividend)*-1
            else:
                return abs(dividend)
        elif(abs(dividend)==2147483648 and abs(divisor)==1):
            if(ru):
                return -2147483648
            else:
                return 2147483647
        temp_re=0
        re=0
        temp=dividend>>31
        while(1):
            max = 31
            index = 0
            temp = dividend >> 31
            while(temp<divisor):
                temp=dividend>>max
                max-=1
                index+=1
            temp_re=pow(2,32-index)
            dividend-=(temp_re*divisor)
            re+=temp_re
            if(dividend<divisor):
                break
        if(ru):
            return re*-1
        else:
            return re

```
