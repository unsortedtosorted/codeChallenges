# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    l=[]
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.l=[]
        self.inorder(root)
        
        if len(self.l)>1:
            r=TreeNode(self.l[1])
            temp=r
            for x in range(2,len(self.l)):
                if self.l[x] is not None: 
                    temp.right=TreeNode(self.l[x])
                    temp=temp.right
                
       
        return r
    def inorder(self,root):
        
        if root.left:
            self.inorder(root.left)
        else:
            self.l.append(None)
        
        self.l.append(root.val)
        
        if root.right:
            self.inorder(root.right)
        else:
             self.l.append(None)
