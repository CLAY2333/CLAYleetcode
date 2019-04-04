// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def search(self, nums: list, target: int) -> int:
        if(len(nums)==0):
            return -1
        left=0
        right=len(nums)-1
        while(1):
            mid = (left + right) // 2
            print(left,mid,right)
            if(target==nums[left]):
                return left
            if (target == nums[right]):
                return right
            if (target == nums[mid]):
                return mid
            if left==right or abs(left-right)==1:
                return -1
            if(nums[left]<nums[mid]):
                if(target>nums[left] and target<nums[mid]):
                    left+=1
                    right=mid-1
                else:
                    left=mid+1
            else:
                if(target<nums[right] and target>nums[mid]):
                    left=mid+1
                    right-=1
                else:
                    right=mid-1

