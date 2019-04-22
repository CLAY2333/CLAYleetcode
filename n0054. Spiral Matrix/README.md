
### Spiral Matrix :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/spiral-matrix](https://leetcode-cn.com/problems/spiral-matrix)
- 执行时间/Runtime: 52 ms 
- 内存消耗/Mem Usage: 13.1 MB
- 通过日期/Accept Datetime: 2019-04-19 12:13
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def spiralOrder(self, matrix: list) -> list:
        n_x=len(matrix)
        if(n_x==0):
            return []
        n_y=len(matrix[0])
        su=0
        re=[]
        index_x=0
        index_y=0
        num_index=0
        walker=[[0 for i in range(n_y)] for i in range(n_x)]
        while(num_index<n_x*n_y):
            if(index_x<n_x and index_y<n_y and walker[index_x][index_y]!=1):
                num_index+=1
                re.append(matrix[index_x][index_y])
                walker[index_x][index_y]=1
            else:
                if (su == 0):
                    index_y -= 1
                elif (su == 1):
                    index_x -= 1
                elif (su == 2):
                    index_y += 1
                elif (su == 3):
                    index_x += 1
                su=(su+1)%4
            if(su==0):
                index_y+=1
            elif(su==1):
                index_x+=1
            elif(su==2):
                index_y-=1
            elif(su==3):
                index_x-=1
        return re

```
