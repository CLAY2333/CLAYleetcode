
### Binary Tree Inorder Traversal :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/binary-tree-inorder-traversal](https://leetcode-cn.com/problems/binary-tree-inorder-traversal)
- 执行时间/Runtime: 40 ms 
- 内存消耗/Mem Usage: 13.2 MB
- 通过日期/Accept Datetime: 2019-05-14 11:29
```python
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

```
