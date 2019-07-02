
### Path Sum :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/path-sum](https://leetcode-cn.com/problems/path-sum)
- 执行时间/Runtime: 72 ms 
- 内存消耗/Mem Usage: 15.2 MB
- 通过日期/Accept Datetime: 2019-07-02 15:26
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        now_sum=0
        Bool=[False]
        def loop(root,sum,now_sum)-> bool:
            if(root==None):
                return None
            now_sum+=root.val
            if now_sum==sum and root.right==None and root.left==None:
                Bool[0]=True
                return True
            else:
                loop(root.left,sum,now_sum)
                loop(root.right,sum,now_sum)
        loop(root,sum,now_sum)
        return Bool[0]

```
