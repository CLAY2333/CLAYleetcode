// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def singleNumber(self, nums:list) -> int:
        hash={}
        for i in nums:
            if i not in hash:
                hash[i]=1
            else:
                hash.pop(i)
        return hash.popitem()[0]
