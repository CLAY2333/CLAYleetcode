// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        chars.append("Nooo")
        temp=''
        index=0
        num=1
        while(index<len(chars)-1):
            if(chars[index]==chars[index+1]):
                num+=1
                index+=1
            else:
                temp+=chars[index]
                if(num>1):
                    temp += (str(num))
                num=1
                index+=1
        temp_index=0
        for i in temp:
            chars[temp_index]=i
            temp_index+=1
        return(len(temp))
