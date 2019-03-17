
### Same Tree :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/same-tree](https://leetcode-cn.com/problems/same-tree)
- 执行时间/Runtime: 24 ms 
- 内存消耗/Mem Usage: 10.8 MB
- 通过日期/Accept Datetime: 2019-03-17 16:01
```python
// Author: Netcan @ https://github.com/netcan/Leetcode-Rust
class Solution(object):
    def DLR(self,tree1,tree2,bool):
        if(tree1==tree2==None):
            return 0
        if(tree1==None and tree2!=None):
            bool[0]=1
            return 0
        if(tree2==None and tree1!=None):

            bool[0] = 1
            return 0
        if(tree1.val!=tree2.val):
            bool[0] = 1
        self.DLR(tree1.left, tree2.left, bool)
        self.DLR(tree1.right,tree2.right,bool)
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        bool=[0]
        self.DLR(p, q, bool)
        if(bool[0]==0):
            return True
        else:
            return False

```
