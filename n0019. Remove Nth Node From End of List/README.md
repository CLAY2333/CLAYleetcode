
### Remove Nth Node From End of List :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list)
- 执行时间/Runtime: 60 ms 
- 内存消耗/Mem Usage: 13.1 MB
- 通过日期/Accept Datetime: 2019-04-01 01:11
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if(head.next==None):
            return None
        temp=head
        temp_back=head
        temp_now=head
        index_now=0
        index_back=0
        while(temp!=None):
            temp=temp.next
            if(index_now!=n):
                index_now+=1
            else:
                temp_now=temp_now.next
            if(index_back!=n+1):
                index_back+=1
            else:
                temp_back=temp_back.next
        if temp_back==head and temp_now!=head:
            temp_back.next=temp_now.next
        elif(temp_now==head):
            head=head.next
        else:
            temp_now=temp_back.next
            temp_back.next=temp_now.next
        return head

```
