// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        temp=nums1+nums2
        temp=sorted(temp)
        L=len(temp)
        if(L%2==0 or L==2):
            return (temp[int(L/2)]+temp[int(L/2)-1])*0.5
        else:
            return (temp[int(L/2)])
