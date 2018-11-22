# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.invert(root)
        
        return root
        
    def invert(self,root):
        if root:
            r=root.right
            l=root.left
            root.left=r
            root.right=l
            self.invert(root.left)
            self.invert(root.right)
