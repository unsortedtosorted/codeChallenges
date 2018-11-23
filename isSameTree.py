# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        return self.checkSame(p,q)
    
    def checkSame(self,r1,r2):
        
        if r1 and r2:
            if r1.val==r2.val:
                if self.checkSame(r1.left,r2.left):
                    if self.checkSame(r1.right,r2.right):
                        return True
                    else:
                        return False
                else:
                    return False
                
            else:
                return False
        
        elif r1==None and r2==None:
            return True
        
        else:
            return False
