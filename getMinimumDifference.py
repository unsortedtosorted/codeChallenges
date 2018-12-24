class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        l=[]
        
        def inOrder(root):
            if root:
                inOrder(root.left)
                l.append(root.val)
                inOrder(root.right)
                
        inOrder(root)
        
        prev=l[0]
        m=sys.maxsize-1
        
        for x in range(1,len(l)):
            temp=abs(l[x]-prev)
            
            if temp<m:
                m=temp
            prev=l[x]
        
        return (m)
