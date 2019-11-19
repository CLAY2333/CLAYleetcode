// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def missingNumber(self, nums: list) -> int:
        S=sum(nums)
        L=len(nums)
        return int((L*(L+1)/2))-S
