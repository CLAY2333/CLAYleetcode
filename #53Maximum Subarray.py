class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len=len(nums)
        index=0
        sum=0
        maxsum=0
        for i in range(nums_len):
            for j in range(nums_len):
                for k in range(i):
                    sum+=nums[index+k]
                if(maxsum<sum):
                    maxsum=sum
                sum=0
                index=0
        print(maxsum)
if __name__=='__main__':
    s=Solution()
    s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
