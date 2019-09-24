// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def rob(self, nums: list) -> int:
        D={}
        preMax=0
        nowMax=0
        for index,value in enumerate(nums):
            temp=nowMax
            nowMax=max(preMax+value,nowMax)
            preMax=temp
        return max(preMax,nowMax)
