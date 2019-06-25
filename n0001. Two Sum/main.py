// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def twoSum(self, num, target):
        dict = {}
        for i in xrange(len(num)):
            x = num[i]
            if target-x in dict:
                return (dict[target-x], i)
            dict[x] = i
