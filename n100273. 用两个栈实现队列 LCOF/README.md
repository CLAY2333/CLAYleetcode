
### 用两个栈实现队列 LCOF :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof)
- 执行时间/Runtime: 668 ms 
- 内存消耗/Mem Usage: 16.9 MB
- 通过日期/Accept Datetime: 2020-02-25 15:18
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class CQueue:

    def __init__(self):
        self.A=[]
        self.B=[]
    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B:
            return self.B.pop()
        elif self.A:
            self.B=self.A.copy()
            self.A=[]
            self.B.reverse()
            return self.B.pop()
        else:
            return -1

```
