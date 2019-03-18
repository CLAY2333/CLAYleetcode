
### Add Two Numbers :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/add-two-numbers](https://leetcode-cn.com/problems/add-two-numbers)
- 执行时间/Runtime: 88 ms 
- 内存消耗/Mem Usage: 10.8 MB
- 通过日期/Accept Datetime: 2019-03-18 14:38
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if(l2==None and l1==None):
            return l1
        if(l2==None):
            l2=ListNode(0)
        if(l1==None):
            l1=ListNode(0)
        str_l1=0
        str_l2=0
        temp_1=l1
        temp_2=l2
        k=1
        while(1):
            if(temp_1==None):
                break
            str_l1+=(temp_1.val)*k
            k*=10
            temp_1=temp_1.next
        k=1
        while(1):
            if(temp_2==None):
                break
            str_l1+=(temp_2.val)*k
            k*=10
            temp_2=temp_2.next
        int_sum=str_l2+str_l1
        str_sum=str(int_sum)
        list_sum=[]
        list_sum.append(ListNode(0))
        for i in range(len(str_sum)):
            list_sum[i].val=str_sum[len(str_sum)-1-i]
            if(i==len(str_sum)-1):
                break
            list_sum.append(ListNode(0))
            list_sum[i].next=list_sum[i+1]
        return list_sum[0]

```
