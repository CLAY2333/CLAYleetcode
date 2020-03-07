
### 队列的最大值 LCOF :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof](https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof)
- 执行时间/Runtime: 272 ms 
- 内存消耗/Mem Usage: 16.8 MB
- 通过日期/Accept Datetime: 2020-03-07 17:51
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
from collections import deque

class MaxQueue:

    def __init__(self):
        self.queue=deque()
        self.queue_sort=deque()

    def max_value(self) -> int:
        if not self.queue:
            return -1
        else:
            max=self.queue_sort[0]
            return max

    def push_back(self, value: int) -> None:
        if not self.queue:
            self.queue.append(value)
            self.queue_sort.append(value)
        else:
            self.queue.append(value)
            while self.queue_sort and self.queue_sort[-1]<=value:
                self.queue_sort.pop()
            self.queue_sort.append(value)
        return

    def pop_front(self) -> int:
        if not self.queue:
            return -1
        temp=self.queue.popleft()
        if temp==self.queue_sort[0]:
            self.queue_sort.popleft()
        return temp


```
