class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if(len(digits)==1 and digits[0]==9):
            return [1,0]
        lens=len(digits)
        digits[lens-1]=digits[lens-1]+1
        if(digits[lens-1]<10):
            return digits
        for i in range(lens):
            digits[lens-1-i]-=10
            digits[lens-2-i]+=1
            if (digits[lens-2-i] < 10):
                return digits
            if(digits[0]==10):
                digits[0]=0
                digits.insert(0,1)
                return digits
if __name__=='__main__':
    s=Solution()
    print(s.plusOne([9]))