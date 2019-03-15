// Author: Netcan @ https://github.com/netcan/Leetcode-Rust
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<2:
            return x
        left=0
        right=x
        while(left<right):
            mid=(left+right)/2
            if((mid*mid)>x):
                right=mid
            else:
                left=mid+1
        return right-1
