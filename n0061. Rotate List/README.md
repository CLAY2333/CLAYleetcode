
### Rotate List :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/rotate-list](https://leetcode-cn.com/problems/rotate-list)
- 执行时间/Runtime: 60 ms 
- 内存消耗/Mem Usage: 13.1 MB
- 通过日期/Accept Datetime: 2019-04-24 15:24
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if(k==0):
            return head
        if head==None:
            return head
        link1=head
        link2=ListNode(-999)
        link2.next=head
        times=0
        while(link1.next):
            link1=link1.next
            times+=1
            if(times>=k):
                link2=link2.next
        times+=1

        if(times<=k):
            k=k%(times)
            if(k==0):
                return head
        link1=head
        link2=ListNode(-999)
        link2.next=head
        times=0
        while(link1.next):
            link1=link1.next
            times+=1
            if(times>=k):
                link2=link2.next
        temp=link2.next
        link2.next=None
        link1.next=head
        return temp

```
