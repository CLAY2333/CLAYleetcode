// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def majorityElement(self, nums: list) -> int:
        if len(nums)==0:
            return 0
        maxtimes=1
        maxnum=nums[0]
        hash={}
        for value in nums:
            if value not in hash:
                hash[value]=1
            else:
                hash[value]+=1
                if hash[value]>maxtimes:
                    maxtimes=hash[value]
                    maxnum=value
        return maxnum
