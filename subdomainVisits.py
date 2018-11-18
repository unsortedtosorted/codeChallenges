class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        
        d={}
        r=[]
        for x in cpdomains:
            l=x.split(" ")
            c=l[0]
            s=l[1]
            
            w=s.split(".")
            temp=""
            
            for x in w[::-1]:
                temp= x+"."+temp
                
                if temp[0:len(temp)-1] in d.keys():
                    d[temp[0:len(temp)-1]]+=int(c)
                else:
                     d[temp[0:len(temp)-1]]=int(c)
                
        for x in d.keys():
            r.append(str(d[x])+" "+x)
        
        return r
