class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        s=set()
        t=set()
        def preOrder(root):
            if root:

                if root.val in s:
                    t.add(True)
                else:
                    s.add(k-root.val)
                    preOrder(root.left)
                    preOrder(root.right)
                    
                
            else:
                return
        r=preOrder(root)
        return True in t
