class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x==0):
            return 0
        i=1
        while(i):
            if((i*i)>x):
                return i-1
            i+=1
    def mySqrt_plus(self,x):
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
if __name__=='__main__':
    s=Solution()
    print(s.mySqrt_plus(8))