
### Rotate Function :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/rotate-function](https://leetcode-cn.com/problems/rotate-function)
- 执行时间/Runtime: 532 ms 
- 内存消耗/Mem Usage: 11.9 MB
- 通过日期/Accept Datetime: 2019-03-21 23:07
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        temp_sum=0
        index=0
        sum_list=sum(A)
        for i in A:
            temp_sum += index * i
            index += 1
        max=temp_sum
        for i in range(len(A)-1):
            temp_sum-=A[-1]*(len(A))
            temp_sum+=sum_list
            if temp_sum >max:
                max=temp_sum
            A.insert(0,A.pop())
        return max

if __name__=='__main__':
    S=Solution()
    A=[4, 3, 2, 6]
    print(S.maxRotateFunction(A))

```
