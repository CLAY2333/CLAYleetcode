// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        left=0
        right=len(nums)-1
        if(len(nums)==0 or target<nums[left] or target>nums[right] ):
            return [-1,-1]
        while(left<=right):
            mid=(left+right)//2
            if(target==nums[mid]):
                temp_left=mid
                temp_right=mid
                while(temp_left>=0 and nums[temp_left]==target ):
                    temp_left-=1
                while( temp_right<len(nums) and nums[temp_right]==target):
                    temp_right+=1
                return [temp_left+1,temp_right-1]
            if(target<nums[mid]):
                right=mid-1
            elif(target>nums[mid]):
                left=mid+1
        return [-1,-1]
