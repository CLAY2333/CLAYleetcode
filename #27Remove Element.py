class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        num=nums.count(val)
        for i in range(num):
            nums.remove(val)

        return len(nums)
if __name__=="__main__":
    s=Solution()
    nums=[]
    num=s.removeElement(nums,3)
    print(num)
    for i in range(num):
        print(nums[i])