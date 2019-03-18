
### Self Dividing Numbers :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/self-dividing-numbers](https://leetcode-cn.com/problems/self-dividing-numbers)
- 执行时间/Runtime: 56 ms 
- 内存消耗/Mem Usage: 11.1 MB
- 通过日期/Accept Datetime: 2019-03-19 01:01
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        List=[]
        for i in range(left,right+1):
            temp_str=str(i)
            index=0
            if '0' in temp_str:
                continue
            for j in range(len(temp_str)):
                if(i%int(temp_str[j])!=0):
                    index=1
                    break
            if index==0:
                List.append(i)
            index=0
        return List

```
