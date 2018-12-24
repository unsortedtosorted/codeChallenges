class Solution(object):
    def convertBST(self, root1):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        l=[0]
        
        if not root1:
            return []
        
        def inOrder2(root):
            if root:
                inOrder2(root.right)
                l[0]+=(root.val)
                root.val=l[0]
                inOrder2(root.left)
        
        
        inOrder2(root1)
        return root1
