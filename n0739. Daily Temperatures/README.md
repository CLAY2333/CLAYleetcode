
### Daily Temperatures :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/daily-temperatures](https://leetcode-cn.com/problems/daily-temperatures)
- 执行时间/Runtime: 724 ms 
- 内存消耗/Mem Usage: 19.8 MB
- 通过日期/Accept Datetime: 2019-12-11 16:33
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        re = []
        Len = len(T)
        T_hash = {}
        T_re = list(reversed(T))
        Stack = []

        for index, value in enumerate(T_re):
            if len(Stack) == 0:
                re.append(0)
                Stack.insert(0, index)
                T_hash[index] = value
            else:
                while len(Stack) != 0 and T_hash[Stack[0]] <= value:
                    del Stack[0]
                if len(Stack) == 0:
                    re.append(0)
                    Stack.insert(0, index)
                    T_hash[index] = value
                else:
                    re.append(index - Stack[0])
                    Stack.insert(0, index)
                    T_hash[index] = value
        return list(reversed(re))

```
