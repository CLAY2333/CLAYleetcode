
### N-Queens II :star::star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/n-queens-ii](https://leetcode-cn.com/problems/n-queens-ii)
- 执行时间/Runtime: 120 ms 
- 内存消耗/Mem Usage: 13 MB
- 通过日期/Accept Datetime: 2019-07-01 16:31
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def totalNQueens(self, n: int) -> list:
        def add_Q(row, column):
            col[row]=1
            # print(row,column)
            checkerboard[column][row]=1
            left_oblique[row+column]=1
            right_oblique[row-column]=1
        def remove_Q(row, column):
            col[row]=0
            checkerboard[column][row]=0
            left_oblique[row+column]=0
            right_oblique[row-column]=0
        def start(row,column):
            for i in range(n):
                if column==n:
                    res[0]+=1
                    return 0
                if col[row+i]!=1 and checkerboard[column][row+i]!=1 and left_oblique[row+i+column]!=1 and right_oblique[row+i-column]!=1:
                    add_Q(row+i,column)
                    start(0,column+1)
                    remove_Q(row+i,column)
                else:
                    if row==n-1:
                        return 0
                    # else:
                    #     start(x+1,y)

        checkerboard=[[0 for i in range(n)] for i in range(n)]
        left_oblique=[0 for i in range(n*n)] #row+column
        right_oblique=[0 for i in range(n*n)] #row-column
        col=[0] * n
        res=[0]
        start(0,0)
        return res[0]

```
