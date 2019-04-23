
### Permutation Sequence :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/permutation-sequence](https://leetcode-cn.com/problems/permutation-sequence)
- 执行时间/Runtime: 60 ms 
- 内存消耗/Mem Usage: 13.1 MB
- 通过日期/Accept Datetime: 2019-04-23 11:55
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
from itertools import permutations
import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        re=[]
        now_re=[]
        nums=[]
        times=[0]
        k-=1
        re=''
        for i in range(1,n+1):
            nums.append(i)
        for i in range(n):
            epoch=math.factorial(n-1)
            re+=str(nums[k//epoch])
            nums.pop(nums.index(nums[k//epoch]))
            k=k%epoch
            n-=1
        return re

```
