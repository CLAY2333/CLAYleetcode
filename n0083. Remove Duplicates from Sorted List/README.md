
### Remove Duplicates from Sorted List :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list)
- 执行时间/Runtime: 44 ms 
- 内存消耗/Mem Usage: 10.8 MB
- 通过日期/Accept Datetime: 2019-03-14 16:52
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new=head
        list_my=[]
        while(new!=None):
            list_my.append(new.val)
            new=new.next
        list_my=list(set(list_my))
        list_my=sorted(list_my)
        re=head
        for i in range(len(list_my)):
            head.val=list_my[i]
            if(i+1==len(list_my)):
                head.next=None
            else:
                head=head.next
        return re

```
