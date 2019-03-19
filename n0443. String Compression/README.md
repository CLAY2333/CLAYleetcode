
### String Compression :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/string-compression](https://leetcode-cn.com/problems/string-compression)
- 执行时间/Runtime: 100 ms 
- 内存消耗/Mem Usage: 11 MB
- 通过日期/Accept Datetime: 2019-03-19 15:22
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        chars.append("Nooo")
        temp=''
        index=0
        num=1
        while(index<len(chars)-1):
            if(chars[index]==chars[index+1]):
                num+=1
                index+=1
            else:
                temp+=chars[index]
                if(num>1):
                    temp += (str(num))
                num=1
                index+=1
        temp_index=0
        for i in temp:
            chars[temp_index]=i
            temp_index+=1
        return(len(temp))

```
