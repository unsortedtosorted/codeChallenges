"""
Faster than 99% online submissions

"""
class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        l=[None,None]
        r=[]
        def inOrder(root):
            if root:
                inOrder(root.left)
                r.append(root.val)
                if l[0]==None:
                    l[0]=(root.val)
                else:
                    temp=abs(root.val-l[0])
                    if l[1]==None:
                        l[1]=temp
                    else:
                        l[1]=min(temp,l[1])
                    l[0]=root.val
                    
                inOrder(root.right)
           
        
        inOrder(root)
