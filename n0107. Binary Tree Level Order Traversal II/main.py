// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #思路为，将每一层的节点从左到右依次存入，然后在继续下一个节点的时候，再依次放出继续存入
        if(root==None):
            return []
        Node_list=[]
        temp_int=[]
        temp=[]
        temp.append(root)
        while_temp=[]
        while temp:
            for i in temp:
                temp_int.append(i.val)
                if(i.left!=None):
                    while_temp.append(i.left)
                if (i.right != None):
                    while_temp.append(i.right)
            temp=while_temp
            while_temp=[]
            Node_list.insert(0,temp_int)
            temp_int=[]
        return Node_list
        
