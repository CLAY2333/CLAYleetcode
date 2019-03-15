// Author: Netcan @ https://github.com/netcan/Leetcode-Rust
class Solution:
    def twoSum(self, num, target):
        dict = {}
        for i in xrange(len(num)):
            x = num[i]
            if target-x in dict:
                return (dict[target-x], i)
            dict[x] = i
