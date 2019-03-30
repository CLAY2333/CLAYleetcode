
### Valid Palindrome :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/valid-palindrome](https://leetcode-cn.com/problems/valid-palindrome)
- 执行时间/Runtime: 88 ms 
- 内存消耗/Mem Usage: 18.6 MB
- 通过日期/Accept Datetime: 2019-03-29 01:02
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def isPalindrome(self, s: str) -> bool:
        re=[]
        for i in s:
            if(i.isalpha() or i.isdigit()):
                re.append(i.lower())
        temp=re.copy()
        temp.reverse()
        if(temp==re):
            return True
        else:
            return False

```
