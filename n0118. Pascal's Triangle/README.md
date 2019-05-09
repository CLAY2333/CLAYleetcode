
### Pascal's Triangle :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/pascals-triangle](https://leetcode-cn.com/problems/pascals-triangle)
- 执行时间/Runtime: 52 ms 
- 内存消耗/Mem Usage: 13 MB
- 通过日期/Accept Datetime: 2019-05-09 20:26
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def Loop(self,numRows:int,re):
        now_len=len(re[-1])
        now_list=[]
        for i in range(now_len+1):
            if(i-1>=0 and i<now_len):
                now_list.append(re[-1][i-1]+re[-1][i])
            else:
                now_list.append(1)
        re.append(now_list)
        numRows-=1
        if(numRows!=0):
            self.Loop(numRows,re)
        return re
    def generate(self, numRows: int) -> list:
        if(numRows==0):
            return []
        elif(numRows==1):
            return [[1]]
        elif(numRows==2):
            return [[1],[1,1]]
        else:
            return self.Loop(numRows-2,[[1],[1,1]])

```
