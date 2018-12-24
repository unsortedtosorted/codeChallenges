class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        l=[]
        m=[sys.maxsize]

        def travel(root):
            if root:
                l.append(root.val)
                if root.val<m[0]:
                    m[0]=root.val
                travel(root.left)
                travel(root.right)
        
        
        travel(root)
        small= m[0]
        secsmall=sys.maxsize
        
        for x in l:
            if x<secsmall and x!=small:
                secsmall=x
        
        if secsmall==sys.maxsize:
            return -1
        return (secsmall)
