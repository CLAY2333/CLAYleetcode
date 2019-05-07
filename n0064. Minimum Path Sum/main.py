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
