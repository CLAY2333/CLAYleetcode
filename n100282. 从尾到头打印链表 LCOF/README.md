
### 从尾到头打印链表 LCOF :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof](https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof)
- 执行时间/Runtime: 124 ms 
- 内存消耗/Mem Usage: 30.4 MB
- 通过日期/Accept Datetime: 2020-02-21 14:19
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res=[]
        while head is not None:
            res.append(head.val)
            head=head.next
        res.reverse()
        return res

```
