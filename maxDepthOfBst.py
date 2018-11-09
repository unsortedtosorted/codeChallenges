# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    tempLevel=0
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
    
        if not root:
            return 0
        self.tempLevel=1
        self.search(root,1)
    
        return self.tempLevel
    
    def search(self,temp,level):
        if temp: 
            if level>self.tempLevel:
                self.tempLevel=level
            self.search(temp.left,level+1)
            self.search(temp.right,level+1)
                

            
            
            
            
            
       
