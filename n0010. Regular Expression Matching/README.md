
### Regular Expression Matching :star::star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/regular-expression-matching](https://leetcode-cn.com/problems/regular-expression-matching)
- 执行时间/Runtime: 60 ms 
- 内存消耗/Mem Usage: 13.4 MB
- 通过日期/Accept Datetime: 2019-06-25 11:20
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = dict()  
        pattern=p
        text=s
        def dp(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if j==len(pattern):
                if(i==len(text)):
                    return True
                else:
                    return False
            if i<len(text):
                if(pattern[j]==text[i] or pattern[j]=='.'):
                    first=True
                else:
                    first=False
            else:
                first=False
            if j<=len(pattern)-2 and pattern[j+1]=='*':
                if(dp(i,j+2) or (first and dp(i+1,j))):
                    ans=True
                else:
                    ans=False
            else:
                if(first and dp(i+1,j+1)):
                    ans=True
                else:
                    ans=False
            memo[(i,j)]=ans
            return ans
        return dp(0, 0)

```
