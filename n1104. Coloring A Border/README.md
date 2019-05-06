
### Coloring A Border :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/coloring-a-border](https://leetcode-cn.com/problems/coloring-a-border)
- 执行时间/Runtime: 128 ms 
- 内存消耗/Mem Usage: 13 MB
- 通过日期/Accept Datetime: 2019-04-28 12:02
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def Loop(self,grid: list,r0: int, c0: int,color: int,now,D,time,X):
        D[r0][c0]=1
        time[0]+=1
        if grid[r0][c0]==now:
            if(r0==0 or c0==0 or r0==len(grid)-1 or c0==len(grid[0])-1):
                X[r0][c0] = 1
                grid[r0][c0]=color
            if(r0+1<len(grid) and time[0]<(len(grid)*len(grid[0]))):
                if(grid[r0+1][c0]!=now and X[r0+1][c0]!=1):
                    X[r0][c0]=1
                    grid[r0][c0] = color
                elif (D[r0+1][c0] != 1):
                    self.Loop(grid, r0+1, c0, color, now,D,time,X)
            if(r0-1>=0 and time[0]<(len(grid)*len(grid[0]))):
                if(grid[r0-1][c0]!=now and X[r0-1][c0]!=1):
                    X[r0][c0]=1
                    grid[r0][c0] = color
                elif (D[r0-1][c0] != 1):
                    self.Loop(grid, r0-1, c0, color, now,D,time,X)
            if(c0+1<len(grid[0]) and time[0]<(len(grid)*len(grid[0]))):
                if(grid[r0][c0+1]!=now and X[r0][c0+1]!=1):
                    X[r0][c0]=1
                    grid[r0][c0] = color
                elif (D[r0][c0 + 1] != 1):
                    self.Loop(grid, r0, c0+1, color, now,D,time,X)
            if(c0-1>=0 and time[0]<(len(grid)*len(grid[0]))):
                if(grid[r0][c0-1]!=now and X[r0][c0-1]!=1):
                    X[r0][c0]=1
                    grid[r0][c0] = color
                elif(D[r0][c0-1]!=1):
                    self.Loop(grid, r0, c0-1, color, now,D,time,X)
        else:
            return 0
    def colorBorder(self, grid: list, r0: int, c0: int, color: int) -> list:
        now=grid[r0][c0]
        time=[0]
        D=[[0 for i in range(len(grid[0]))] for i in range(len(grid))]
        X = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
        if(now==color):
            return grid
        self.Loop(grid,r0,c0,color,now,D,time,X)
        return grid

```
