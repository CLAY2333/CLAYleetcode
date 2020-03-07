// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
from typing import List
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        H={}
        for i in nums:
            if i in H:
                return i
            H[i]=1
        return -1
