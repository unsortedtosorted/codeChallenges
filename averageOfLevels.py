# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    l={}
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        self.l={}
        self.sum={}
        self.inorder(root,0)
        r=[]
        
        for x in self.l.keys():
            r.append(1.0*self.sum[x]/len(self.l[x]))
        return r
    
    def inorder(self,root,level):
        
        if root:
            if level in self.l.keys():
                temp=self.l[level]
                temp.append(root.val)
                self.l[level]=temp
                self.sum[level]+=root.val
            else:
                temp=[root.val]
                self.sum[level]=root.val
                self.l[level]=temp
            self.inorder(root.left,level+1)
            self.inorder(root.right,level+1)
