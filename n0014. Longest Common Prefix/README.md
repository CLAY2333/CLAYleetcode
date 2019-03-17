
### Longest Common Prefix :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/longest-common-prefix](https://leetcode-cn.com/problems/longest-common-prefix)
- 执行时间/Runtime: 1328 ms 
- 内存消耗/Mem Usage: 11 MB
- 通过日期/Accept Datetime: 2019-03-04 21:04
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def longestCommonPrefixtwo(self,strs):
        if(strs[0]=="" or strs[1]==""):
            return ""
        if( strs[0][0]!=strs[1][0]):
            return ""
        len_strs1 = len(strs[0])
        len_strs2 = len(strs[1])
        for i in range(len_strs1):
            for j in range(len_strs2):
                if(strs[0][i]==strs[1][j] and strs[0][0:i]==strs[1][0:j]):
                    p=i
        return strs[0][0:p+1]
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        len_strs=len(strs)
        if(len_strs==0):
            return ""
        if(len_strs==1):
            return strs[0]
        if(len_strs==2):
            return  self.longestCommonPrefixtwo([strs[0],strs[1]])
        commonstrs= self.longestCommonPrefixtwo([strs[0],strs[1]])
        for i in range(len(strs)-2):
            commonstrs=self.longestCommonPrefixtwo([commonstrs,strs[i+2]])
        return commonstrs


```
