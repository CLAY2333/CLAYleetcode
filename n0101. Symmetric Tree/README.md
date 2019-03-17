
### Symmetric Tree :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/symmetric-tree](https://leetcode-cn.com/problems/symmetric-tree)
- 执行时间/Runtime: 36 ms 
- 内存消耗/Mem Usage: 11 MB
- 通过日期/Accept Datetime: 2019-03-17 17:41
```python
// Author: Netcan @ https://github.com/netcan/Leetcode-Rust
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def DLR(self,tree, num):
        if(tree==None):
            num.append('a')
            return 0
        if(tree.val=='null'):
            tree.val=-9999
        num.append(tree.val)
        self.DLR(tree.left, num)
        self.DLR(tree.right, num)

    def DLR_s(self,tree, num):
        if(tree==None):
            num.append('a')
            return 0
        if(tree.val=='null'):
            tree.val=-9999
        num.append(tree.val)
        self.DLR_s(tree.right, num)
        self.DLR_s(tree.left, num)


    def LDR(self,tree, num):
        if(tree==None):
            num.append('a')
            return 0
        if(tree.val=='null'):
            tree.val=-9999
        self.LDR(tree.left, num)
        num.append(tree.val)
        self.LDR(tree.right, num)

    def LDR_s(self, tree, num):
            if (tree == None):
                num.append('a')
                return 0
            if (tree.val == 'null'):
                tree.val = -9999
            self.LDR_s(tree.right, num)
            num.append(tree.val)
            self.LDR_s(tree.left, num)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if(root==None):
            return True
        if(root.left==None and root.right==None):
            return True
        if(root.left==None or root.right==None):
            return False
        root_DLR_l=[]
        root_DLR_r=[]
        root_LRD_l=[]
        root_LRD_r=[]
        self.DLR(root.left,root_DLR_l)
        self.DLR_s(root.right,root_DLR_r)
        self.LDR(root.left,root_LRD_l)
        self.LDR_s(root.right,root_LRD_r)
        
        if(root_DLR_l!=root_DLR_r):
            return False
        if(root_LRD_l!=root_LRD_r):
            return False
        return True

```
