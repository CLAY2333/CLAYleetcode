// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list=path.split('/')
        re=[]
        for index,value in enumerate(path_list):
            if value=='' or value=='.':
                continue
            if(value!='..'):
                P='/'+value
                re.append(P)
            else:
                if(len(re)==0):
                    continue
                re.pop(-1)
        re=''.join(re)
        if re=='':
            return '/'
        return re
