
### Group Anagrams :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/group-anagrams](https://leetcode-cn.com/problems/group-anagrams)
- 执行时间/Runtime: 240 ms 
- 内存消耗/Mem Usage: 16.1 MB
- 通过日期/Accept Datetime: 2019-04-15 16:44
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def groupAnagrams(self, strs:list) -> list:
        D={}
        re=[]

        for index,value in enumerate(strs):
            temp_value=value
            now_value=''.join(sorted(temp_value))
            if D.get(now_value)==None:
                D[now_value]=len(re)
                re.append([value])
            else:
                re[D.get(now_value)].append(value)
        return re

```
