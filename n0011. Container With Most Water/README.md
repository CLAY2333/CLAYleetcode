
### Container With Most Water :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/container-with-most-water](https://leetcode-cn.com/problems/container-with-most-water)
- 执行时间/Runtime: 92 ms 
- 内存消耗/Mem Usage: 14.4 MB
- 通过日期/Accept Datetime: 2019-03-27 00:20
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def maxArea(self, height: list) -> int:
        maxarea=0
        left=0
        right=len(height)-1
        for i in range(len(height)):
            maxarea=max(maxarea,min(height[left],height[right])*(right-left))
            if(height[left]<height[right]):
                left+=1
            else:
                right-=1
        return maxarea

```
