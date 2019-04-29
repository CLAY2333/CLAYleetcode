// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        nums=0
        for i in S:
            if i in J:
                nums+=1
        return nums
