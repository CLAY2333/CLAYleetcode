// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        D={}
        temp_suburl=[]
        for i in cpdomains:
            str_int=i[0:i.find(' ')]
            str_url=i[i.find(' ')+1:len(i)]
            temp=str_url.split(".",str_url.count("."))
            T=[]
            if(str_url.count(".")==1):
                T.append(str_url)
                T.append(temp[-1])
            if(str_url.count(".")==2):
                T.append(str_url)
                T.append(temp[-2]+"."+temp[-1])
                T.append(temp[-1])
            for j in T:
                if j not in temp_suburl:
                    temp_suburl.append(j)
                if j not in D:
                    D[j]=int(str_int)
                else:
                    D[j]+=int(str_int)
        result=[]
        for i in temp_suburl:
            result.append(str(D[i])+" "+i)
        return result
