class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        l=[0]
        
        def order(root):
            if root:
                left=root.left
                if left:
                    if left.left==None and left.right==None:
                        l[0]+=root.left.val
                order(root.left)
                order(root.right)
        
        order(root)
        return (l[0])
