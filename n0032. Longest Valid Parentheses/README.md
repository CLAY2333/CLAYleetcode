
### Longest Valid Parentheses :star::star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/longest-valid-parentheses](https://leetcode-cn.com/problems/longest-valid-parentheses)
- 执行时间/Runtime: 72 ms 
- 内存消耗/Mem Usage: 14.4 MB
- 通过日期/Accept Datetime: 2019-10-08 15:47
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        Stack=[]
        Max=0
        Stack.append(-1)
        for index,value in enumerate(s):
            if value!=')':
                Stack.append(index)
            else:
                if Stack[-1]!=-1 and s[Stack[-1]]=='(':
                    del Stack[-1]
                    if index-Stack[-1]>Max:
                         Max=index-Stack[-1]
                else:
                    Stack.append(index)
        return Max

```
