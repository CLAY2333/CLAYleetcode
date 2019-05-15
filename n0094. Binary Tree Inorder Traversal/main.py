// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def Loop(self,root,re):
        if(root==None):
            return 0
        self.Loop(root.left,re)
        re.append(root.val)
        self.Loop(root.right,re)
    def inorderTraversal(self, root: TreeNode) -> list:
        re=[]
        self.Loop(root,re)
        return re
