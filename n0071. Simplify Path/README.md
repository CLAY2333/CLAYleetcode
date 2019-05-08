
### Simplify Path :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/simplify-path](https://leetcode-cn.com/problems/simplify-path)
- 执行时间/Runtime: 60 ms 
- 内存消耗/Mem Usage: 13.1 MB
- 通过日期/Accept Datetime: 2019-05-08 10:53
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list=path.split('/')
        re=[]
        for index,value in enumerate(path_list):
            if value=='' or value=='.':
                continue
            if(value!='..'):
                P='/'+value
                re.append(P)
            else:
                if(len(re)==0):
                    continue
                re.pop(-1)
        re=''.join(re)
        if re=='':
            return '/'
        return re

```
