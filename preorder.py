"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    
    r=[]
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.r=[]
        self.pre(root)
        return self.r
        
        
    def pre(self,root):
        if root==None:
            return []
        if root:
            self.r.append(root.val)
            for x in root.children:
                self.pre(x)
