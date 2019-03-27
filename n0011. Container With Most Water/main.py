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
