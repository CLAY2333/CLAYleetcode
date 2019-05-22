
### Partition List :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/partition-list](https://leetcode-cn.com/problems/partition-list)
- 执行时间/Runtime: 56 ms 
- 内存消耗/Mem Usage: 12.9 MB
- 通过日期/Accept Datetime: 2019-05-16 20:06
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head==None:
            return []
        node_list=[]
        while head!=None:
            node_list.append(head.val)
            head=head.next
        one=[]
        two=[]
        for i in node_list:
            if i >=x:
                two.append(i)
            else:
                one.append(i)
        node_list=one+two
        head=ListNode(node_list[0])
        node_list.pop(0)
        temp=head
        for i in node_list:
            N=ListNode(i)
            temp.next=N
            temp=temp.next
        return head

```
