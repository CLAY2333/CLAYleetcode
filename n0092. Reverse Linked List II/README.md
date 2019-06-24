
### Reverse Linked List II :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/reverse-linked-list-ii](https://leetcode-cn.com/problems/reverse-linked-list-ii)
- 执行时间/Runtime: 44 ms 
- 内存消耗/Mem Usage: 12.8 MB
- 通过日期/Accept Datetime: 2019-06-24 20:49
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if(head.next==None or m==n):
            return head
        first_node=head
        second_node=head
        qiang=ListNode(-9)
        qiang.next=head
        head=qiang
        n+=1
        m+=1
        temp=ListNode(-999)
        temp.next=head
        num=0
        while temp!=None:
            if num==n-1:
                second_node=temp
                break
            else:
                if(num==m-1):
                    first_node=temp
                num+=1
                temp=temp.next
        head_short=first_node.next
        w_short=second_node.next
        d=w_short.next
        head_short_while=head_short
        next_head = head_short_while.next
        next_next_head = next_head.next
        time=0
        while(time!=n-m and next_next_head!=None):
            next_head.next=head_short_while
            head_short_while=next_head
            next_head=next_next_head
            next_next_head=next_head.next
            time+=1
        if(time!=n-m):
            next_head.next=head_short_while
            if(first_node.val==-9):
                head_short.next=None
                return next_head
            first_node.next=next_head
            head_short.next=None
            return head.next
        first_node.next=w_short
        head_short.next=d
        return head.next


```
