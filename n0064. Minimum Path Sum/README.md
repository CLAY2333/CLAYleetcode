
### Minimum Path Sum :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/minimum-path-sum](https://leetcode-cn.com/problems/minimum-path-sum)
- 执行时间/Runtime: 76 ms 
- 内存消耗/Mem Usage: 14.5 MB
- 通过日期/Accept Datetime: 2019-05-06 20:05
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def minPathSum(self, grid: list) -> int:
        dis=[[0 for i in range(len(grid[0]))] for i in range(len(grid))]
        dis[0][0]=grid[0][0]
        for i in range(1,len(grid[0])):
            dis[0][i]=dis[0][i-1]+grid[0][i]
        for i in range(1,len(grid)):
            dis[i][0]=dis[i-1][0]+grid[i][0]
        for i in range(1, len(grid[0])):
            for j in range(1, len(grid)):
                dis[j][i]=min(dis[j-1][i],dis[j][i-1])+grid[j][i]
        return dis[-1][-1]

```
