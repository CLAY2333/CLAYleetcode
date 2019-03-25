
### ZigZag Conversion :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/zigzag-conversion](https://leetcode-cn.com/problems/zigzag-conversion)
- 执行时间/Runtime: 136 ms 
- 内存消耗/Mem Usage: 11.7 MB
- 通过日期/Accept Datetime: 2019-03-25 16:47
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        L=len(s)
        List=[[]*L for i in range(numRows)]
        stu=0
        index=0
        re=''
        for i in s:
            if(stu==0):
                if(index<numRows-1):
                    List[index].append(i)
                    index+=1
                else:
                    List[index].append(i)
                    index-=1
                    stu=1
            else:
                if(index>0):
                    List[index].append(i)
                    index-=1
                else:
                    List[index].append(i)
                    index+=1
                    stu=0
        for i in List:
            re+=''.join(i)
        return re
        

```
