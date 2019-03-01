class Solution:
    def twoSum(self, num, target):
        dict = {}
        for i in range(len(num)):
            x = num[i]
            if target-x in dict:
                return (dict[target-x], i)
            dict[x] = i
if __name__ == '__main__':
    s=Solution()
    num= [1,3,4]
    target=9
    print(s.twoSum(num,target))