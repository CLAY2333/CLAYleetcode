
### Merge k Sorted Lists :star::star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/merge-k-sorted-lists](https://leetcode-cn.com/problems/merge-k-sorted-lists)
- 执行时间/Runtime: 100 ms 
- 内存消耗/Mem Usage: 16.9 MB
- 通过日期/Accept Datetime: 2019-06-27 10:02
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        if(len(lists)==0):
            return []
        L=[]
        for i in lists:
            while i !=None:
                L.append(i.val)
                i=i.next
        L.sort()
        if(len(L)==0):
            return []
        res=ListNode(L[0])
        temp=res
        for i in L[1:]:
            Node=ListNode(i)
            temp.next=Node
            temp=Node
        return res

```
