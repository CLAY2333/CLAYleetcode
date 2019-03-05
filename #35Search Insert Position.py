class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count=nums.count(target)
        if(count!=0):
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
if __name__=='__main__':
    s=Solution()
    nums=[1,1]
    target=1
    print(s.searchInsert(nums,target))
