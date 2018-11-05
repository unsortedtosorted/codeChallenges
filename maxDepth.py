class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root==None:
            return 0
        
        d={}
        d[root]=1
        r=[root]
        max=1
        temp2=1
        
        while len(r)>0: 
            temp=r.pop()
            
            for x in temp.children:
                r.insert(0,x)
                temp2=d[temp]+1
                d[x]=temp2
                if temp2>max:
                    max=temp2
        
        return temp2     
