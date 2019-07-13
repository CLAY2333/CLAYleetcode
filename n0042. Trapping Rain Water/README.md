
### Trapping Rain Water :star::star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/trapping-rain-water](https://leetcode-cn.com/problems/trapping-rain-water)
- 执行时间/Runtime: 48 ms 
- 内存消耗/Mem Usage: 13.5 MB
- 通过日期/Accept Datetime: 2019-07-13 16:43
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def trap(self, height: list) -> int:
        if(len(height)==0):
            return 0
        left=0
        right=len(height)-1
        left_max=height[left]
        right_max=height[right]
        res=0
        while(left!=right):
            if(height[left]<height[right]):
                if(left_max<height[left]):
                    left_max=height[left]
                else:
                    res+=left_max-height[left]
                left+=1
            else:
                if (right_max < height[right]):
                    right_max = height[right]
                else:
                    res += right_max - height[right]
                right -= 1

        return res

```
