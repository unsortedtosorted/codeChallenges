class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        l=[]
        
        
        q=[(root,0)]
        
        while len(q)>0:
            n=q.pop()

            if n[0]:
                ind=n[1]
                val=n[0].val
                if ind>=len(l):
                    l.append([val])
                else:
                    temp=l[ind]
                    temp.append(val)
                    l[ind]=temp
                q.insert(0,(n[0].left,n[1]+1))
                q.insert(0,(n[0].right,n[1]+1))
        
        return (l[::-1])
