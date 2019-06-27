// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def fourSum(self, nums: list, target: int) -> list:
        nums.sort()
        res=[]
        L=len(nums)
        for i in range(L-3):
            if nums[i]+nums[L-1]+nums[L-1] + nums[L - 2]<target:
                continue
            if nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target:
                break
            for j in range(i+1,L-2):
                if nums[i] + nums[j] + nums[L-1] + nums[L - 2] < target:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                left=j+1
                right=L-1
                while left!=right:
                    if nums[i]+nums[j]+nums[left]+nums[right]==target:
                        temp=[]
                        temp.append(nums[i])
                        temp.append(nums[j])
                        temp.append(nums[left])
                        temp.append(nums[right])
                        if not temp in res:
                            res.append(temp.copy())
                        left+=1
                    elif nums[i]+nums[j]+nums[left]+nums[right]>target:
                        right-=1
                    elif nums[i]+nums[j]+nums[left]+nums[right]<target:
                        left+=1
        return res
