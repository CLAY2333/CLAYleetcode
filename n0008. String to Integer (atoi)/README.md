
### String to Integer (atoi) :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/string-to-integer-atoi](https://leetcode-cn.com/problems/string-to-integer-atoi)
- 执行时间/Runtime: 136 ms 
- 内存消耗/Mem Usage: 13 MB
- 通过日期/Accept Datetime: 2019-03-26 11:32
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def R(self,stu:str,num:str) -> int :
        if len(num)==0:
            return 0
        if(stu=='+'):
            return int(num)
        else:
            return int(num)*-1
    def myAtoi(self, S:str) -> int:
        Str=S.lstrip()
        if(len(Str)==0):
            return  0
        stu='+'
        SSS=0
        Min='2147483648'
        Max='2147483647'
        if not (Str[0].isdigit() or Str[0]=='+' or Str[0]=='-'):
            return 0
        else:
            if(Str[0]=='-' or Str[0]=='+'):
                stu=Str[0]
                Str=Str[1:]
            new=''
            for i in Str:
                if(i.isdigit()):
                    if(i=='0' and SSS==0):
                        pass
                    else:
                        new+=i
                        SSS=1
                else:
                    break
            if (len(Str) == 0):
                return 0
            if len(new)<10:
                return self.R(stu,new)
            else:
                if(len(new)>10):
                    if (stu == '-'):
                        return self.R(stu, Min)
                    else:
                        return self.R(stu, Max)
                else:
                    for i in range(len(new)):
                        if(new[i]==Min[i]):
                            pass
                        else:
                            if(new[i]>Min[i]):
                                if(stu=='-'):
                                    return self.R(stu ,Min)
                                else:
                                    return self.R(stu,Max)
                            else:
                                return self.R(stu,new)
        if (stu == '-'):
            return self.R(stu, Min)
        else:
            return self.R(stu, Max)

```
