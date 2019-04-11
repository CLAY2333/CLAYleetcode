
### Multiply Strings :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/multiply-strings](https://leetcode-cn.com/problems/multiply-strings)
- 执行时间/Runtime: 772 ms 
- 内存消耗/Mem Usage: 13.3 MB
- 通过日期/Accept Datetime: 2019-04-11 11:44
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def Add(self,S1,S2,num):
        if(len(S2)==0):
            return S1
        for zero in range(num-1):
            S1.append('0')
        on=0
        re=[]
        S2.reverse()
        S1.reverse()
        for index,value in enumerate(S1):
            if(index<len(S2)):
                temp=int(value)+int(S2[index])+on
                on=temp//10
                re.append(str(temp%10))
            else:
                temp=int(value)+on
                re.append(str(temp%10))
                on=temp//10
        if(on!=0):
            re.append(str(on))
        re.reverse()
        return re

    def multiply(self, num1: str, num2: str) -> str:
        if(num1=='0' or num2=='0'):
            return '0'
        re=[]
        temp_re=[]
        on=0
        num=1
        num2=list(num2)
        num1=list(num1)
        num1.reverse()
        num2.reverse()
        for index_2,value_2 in enumerate(num2):
            on = 0
            temp_re=[]
            for index_1,value_1 in enumerate(num1):
                temp=int(value_2)*int(value_1)+on
                on=temp//10
                temp_re.insert(0,str(temp%10))
            if(on!=0):
                temp_re.insert(0,str(on))
            re=self.Add(temp_re,re,num)
            num+=1
        return ''.join(re)

```
