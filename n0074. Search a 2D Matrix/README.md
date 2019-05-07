
### Search a 2D Matrix :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/search-a-2d-matrix](https://leetcode-cn.com/problems/search-a-2d-matrix)
- 执行时间/Runtime: 56 ms 
- 内存消耗/Mem Usage: 13.8 MB
- 通过日期/Accept Datetime: 2019-05-07 15:16
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        if(len(matrix)==0 or len(matrix[0])==0):
            return False
        if (target > matrix[-1][-1]):
            return False
        matrix.append([-999])
        for index,value in enumerate(matrix):
            if target<value[0]:
                break
        now_list=matrix[index-1]
        if(len(now_list)==0):
            return False
        left=0
        right=len(now_list)-1
        while(left<=right):
            mid=(left+right)//2
            if(target>now_list[mid]):
                left=mid+1
            elif(target<now_list[mid]):
                right=mid-1
            else:
                return True
        return False

```
