class Solution(object):
    def reverse(self, x):
        if(x>0):
            x=str(x)
            y = list(x)
            for i in range(len(x)):
                y[i]=x[len(x)-i-1]
            s=''.join(y)
            s=int(s)
            if(s>2147483648):
                return 0
            return s
        else:
            x=x*(-1)
            x = str(x)
            y = list(x)
            for i in range(len(x)):
                y[i]=x[len(x)-i-1]
            s = ''.join(y)
            s = int(s)
            s=s*(-1)
            if(s<-2147483648):
                return 0
            return s
if __name__ == '__main__':
    s=Solution()
    num= 123
    print(s.reverse(num))