# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        self.l=[]
        def getPaths(prev,root):
            
            if root:
                
                if not root.left and not root.right:
                    temp=(prev+"->"+str(root.val))
                    self.l.append(temp[2:])
                    return
                    
                getPaths(prev+"->"+str(root.val),root.left)
                getPaths(prev+"->"+str(root.val),root.right)
            
            
        
        
        getPaths("",root)
        
        return self.l
