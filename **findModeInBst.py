# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        d={}
        
        
        def inorder(root):
            if not root:
                return
            temp=root.val
            if temp in d.keys():
                d[temp]+=1
            else:
                d[temp]=1
            inorder(root.left)
            inorder(root.right)
        
        inorder(root)
        
        m=-sys.maxsize-1
        r=[]
        for x in d:
            if d[x]>m:
                r=[]
                r.append(x)
                m=d[x]
            elif d[x]==m:
                 r.append(x)
        
        return (r)
                
            
            
                
        
