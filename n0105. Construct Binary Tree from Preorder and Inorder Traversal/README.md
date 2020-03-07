
### Construct Binary Tree from Preorder and Inorder Traversal :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal)
- 执行时间/Runtime: 172 ms 
- 内存消耗/Mem Usage: 88.2 MB
- 通过日期/Accept Datetime: 2020-02-24 15:51
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def buildleftTree(preorder: List[int], inorder: List[int],nowhead):
            if len(preorder)==0:
                return
            if len(preorder)==1:
                nowhead.left=TreeNode(preorder[0])
            else:
                nexthead=TreeNode(preorder[0])
                nowhead.left=nexthead
                index_nexthead = inorder.index(preorder[0])
                buildleftTree(preorder[1:index_nexthead+1], inorder[0:index_nexthead], nexthead)
                buildrightTree(preorder[index_nexthead + 1:], inorder[index_nexthead + 1:], nexthead)
        def buildrightTree(preorder: List[int], inorder: List[int],nowhead):
            if len(preorder)==0:
                return
            if len(preorder)==1:
                nowhead.right=TreeNode(preorder[0])
            else:
                nexthead=TreeNode(preorder[0])
                nowhead.right=nexthead
                index_nexthead = inorder.index(preorder[0])
                buildleftTree(preorder[1:index_nexthead+1], inorder[0:index_nexthead], nexthead)
                buildrightTree(preorder[index_nexthead + 1:], inorder[index_nexthead + 1:], nexthead)
        if len(preorder)==0:
            return None
        head=TreeNode(preorder[0])
        index_head=inorder.index(preorder[0])
        # if preorder[1] in inorder[0:index_head-1]:
        buildleftTree(preorder[1:index_head-0+0+1],inorder[0:index_head],head)
        # elif preorder[1] in inorder[index_head+1:-1]:
        buildrightTree(preorder[index_head-0+0+1:],inorder[index_head+1:],head)
        # else:
        return head

```
