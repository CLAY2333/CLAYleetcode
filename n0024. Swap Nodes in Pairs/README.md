
### Swap Nodes in Pairs :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/swap-nodes-in-pairs](https://leetcode-cn.com/problems/swap-nodes-in-pairs)
- 执行时间/Runtime: 52 ms 
- 内存消耗/Mem Usage: 13.2 MB
- 通过日期/Accept Datetime: 2019-04-01 15:53
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        new_head=ListNode(0)
        new_head.next=head
        temp=ListNode(0)
        temp_now=head
        temp_up=new_head
        while(temp_now!=None):
            if(temp_now!=None and temp_now.next!=None):
                temp=temp_now.next.next
                temp_up.next=temp_now.next
                temp_up.next.next=temp_now
                temp_now.next=temp
                temp_up=temp_now
                temp_now=temp
            else:
                return new_head.next
        return new_head.next

```
