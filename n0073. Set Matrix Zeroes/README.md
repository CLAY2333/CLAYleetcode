
### Set Matrix Zeroes :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/set-matrix-zeroes](https://leetcode-cn.com/problems/set-matrix-zeroes)
- 执行时间/Runtime: 136 ms 
- 内存消耗/Mem Usage: 13.1 MB
- 通过日期/Accept Datetime: 2019-05-06 18:47
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def setZeroes(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ED=[[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
        for index_x,value_x in enumerate(matrix):
            for index_y,value_y in enumerate(value_x):
                if value_y==0 and ED[index_x][index_y]!=1:
                    ED[index_x][index_y]=1
                    for i in range(len(matrix)):
                        if(matrix[i][index_y]!=0):
                            ED[i][index_y] = 1
                            matrix[i][index_y]=0
                    for i in range(len(matrix[0])):
                        if(matrix[index_x][i]!=0):
                            ED[index_x][i] = 1
                            matrix[index_x][i] = 0

```
