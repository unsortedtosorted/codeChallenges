class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        
        r=[]
        n=[]
        if not root:
            return r
        n.append((root,0))
        
        while len(n)>0:
            ind=len(n)-1
            temp=n[ind]
            del n[ind]
            index=temp[1]
            for x in temp[0].children:
                
                n.insert(0,(x,index+1))
            
            if len(r)-1>=index:
                r[index].append(temp[0].val)
            else:
                r.append([temp[0].val])
        return (r)
