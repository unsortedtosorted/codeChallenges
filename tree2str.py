class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        
        def preOrder(root):
            
            s=""
            
            if root:
                s=str(root.val)
                l="()"
                r="()"
                
                if not root.left and not root.right:
                    return s
                
                if root.left:
                    l="("+preOrder(root.left)+")"
                
                if root.right:
                    r="("+preOrder(root.right)+")"
                
                if r=="()":
                    s=s+l
                else:
                     s=s+l+r
                    
                return s
            else:
                return ""
        
        return (preOrder(t))
