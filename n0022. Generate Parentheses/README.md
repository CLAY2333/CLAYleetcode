
### Generate Parentheses :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/generate-parentheses](https://leetcode-cn.com/problems/generate-parentheses)
- 执行时间/Runtime: 56 ms 
- 内存消耗/Mem Usage: 13.2 MB
- 通过日期/Accept Datetime: 2019-04-01 15:20
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def loop(self,n:int,re:list,Str:str,stu:int):
        if(n>0):
            if(stu<0 or stu>n):
                return 0
            self.loop(n,re,Str+'(',stu+1)
            if(stu-1>=0):
                self.loop(n-1,re,Str+')',stu-1)
        else:
            re.append(Str)
    def generateParenthesis(self, n: int) -> list:
        re=[]
        Str=''
        stu=0
        self.loop(n,re,Str,stu)
        return re

```
