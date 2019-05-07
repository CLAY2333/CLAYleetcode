// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        if(obstacleGrid[0][0]==1):
            return 0
        rouline=[[0 for i in range(len(obstacleGrid[0]))] for i in range(len(obstacleGrid))]
        rouline[0][0]=1
        for i in range(len(obstacleGrid[0])):
            if(obstacleGrid[0][i]==1):
                break
            rouline[0][i]=1
        k=i
        for i in range(len(obstacleGrid)):
            if (obstacleGrid[i][0] == 1):
                break
            rouline[i][0] = 1
        h=i
        for j in range(1,len(obstacleGrid)):
            for i in range(1,len(obstacleGrid[0])):
                if(obstacleGrid[j][i]!=1):
                    rouline[j][i]=rouline[j-1][i]+rouline[j][i-1]
                else:
                    continue
        return rouline[-1][-1]
