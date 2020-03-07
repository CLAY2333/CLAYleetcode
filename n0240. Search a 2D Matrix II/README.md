
### Search a 2D Matrix II :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/search-a-2d-matrix-ii](https://leetcode-cn.com/problems/search-a-2d-matrix-ii)
- 执行时间/Runtime: 36 ms 
- 内存消耗/Mem Usage: 17.8 MB
- 通过日期/Accept Datetime: 2020-02-16 13:45
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==0 or len(matrix[0])==0 or target<matrix[0][0] or target>matrix[-1][-1]:
            return False
        index_1=len(matrix)-1
        index_2=0
        while -1<index_1<len(matrix) and -1<index_2<len(matrix[0]):
            if matrix[index_1][index_2]<target:
                index_2+=1
            elif matrix[index_1][index_2]>target:
                index_1-=1
            else:
                return True
        return False

```
