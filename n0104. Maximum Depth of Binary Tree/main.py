// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def DLR(self,root,now_floor,max):
        if(root==None):
            return 0
        if (now_floor>max[0]):
            max[0]=now_floor
        self.DLR(root.left,now_floor+1,max)
        self.DLR(root.right,now_floor+1,max)
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root==None):
            return 0
        max=[0]
        now_floor=0
        self.DLR(root,now_floor,max)
        return max[0]+1
