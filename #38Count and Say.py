class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        str='1'
        ans=''
        index=0
        for i in range(1,n):
            for j in range(len(str)):
                if((index+1)<len(str) and str[index]==str[index+1] ):
                    if ((index+2)<len(str) and str[index] == str[index + 2]):
                        if ((index+3)<len(str) and str[index] == str[index + 3]):
                            ans+='4'+str[index]
                            index+=4
                        else:
                            ans += '3' + str[index]
                            index += 3
                    else:
                        ans += '2' + str[index]
                        index += 2
                else:
                    if((index+1)>len(str)):
                        break
                    ans += '1' + str[index]
                    index += 1
            str=ans
            index=0
            ans=''
        return str



if __name__=='__main__':
    s=Solution()
    print(s.countAndSay(30))