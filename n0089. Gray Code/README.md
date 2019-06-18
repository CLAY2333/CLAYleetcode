
### Gray Code :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/gray-code](https://leetcode-cn.com/problems/gray-code)
- 执行时间/Runtime: 92 ms 
- 内存消耗/Mem Usage: 13 MB
- 通过日期/Accept Datetime: 2019-06-18 14:52
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def grayCode(self, n: int) -> list:
        nums=['0' for i in range(n)]
        times=0
        relust=[0]
        for i in range(pow(2,n)-1):
            if times%2==0:
                if nums[-1]=='0':
                    nums.pop(-1)
                    nums.append('1')
                else:
                    nums.pop(-1)
                    nums.append('0')
            else:
                for i in range(len(nums)):
                    if nums[len(nums)-i-1]=='1':
                        if nums[len(nums)-i-2]=='1':
                            L=len(nums)
                            nums.pop(L-i-2)
                            nums.insert(L-i-2,'0')
                        else:
                            L = len(nums)
                            nums.pop(L-i-2)
                            nums.insert(L-i-2,'1')
                        break
                    else:
                        pass
            times+=1
            temp_nums=self.listtostr(nums)
            relust.append(int(temp_nums,2))
        return relust
    def listtostr(self,list):
        return ''.join(list)

```
