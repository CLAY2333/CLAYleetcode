
### Add Binary :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/add-binary](https://leetcode-cn.com/problems/add-binary)
- 执行时间/Runtime: 28 ms 
- 内存消耗/Mem Usage: 10.8 MB
- 通过日期/Accept Datetime: 2019-03-14 13:36
```python
// Author: Netcan @ https://github.com/netcan/Leetcode-Rust
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum=int(a)+int(b)
        sum=str(sum)
        list_num=[]
        for i in range(len(sum)):
            list_num.append(int(sum[i]))
        if(len(sum)==1):
            if(list_num[0]>1):
                list_num[0] -= 2
                list_num.insert(0,1)
                return "".join(str(x) for x in list_num)
            else:
                return "".join(str(x) for x in list_num)
        for i in range(len(sum)):
            if(list_num[len(sum)-1-i]>1):
                list_num[len(sum)-1-i]-=2
                list_num[len(sum)-2-i]+=1
            if(len(sum)-2-i==0):
                if(list_num[len(sum)-2-i]>1):
                    list_num[len(sum) - 2 - i]-=2
                    list_num.insert(0,1)
                    return "".join(str(x) for x in list_num)
                else:
                    return "".join(str(x) for x in list_num)
        return "".join(str(x) for x in list_num)

```
