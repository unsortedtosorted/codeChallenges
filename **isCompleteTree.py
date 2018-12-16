# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import *
class Solution:
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = Queue(maxsize=100)
        
        q.put(root)
        d={}
        l={}
        l[root]=0
        while not q.empty():
            
            
            temp=q.get()
            level=l[temp]
            

            v=temp.val
            
            
            if level in d.keys():
                l1=d[level]
                l1.append(v)
                d[level]=l1
            else:
                d[level]=[v]
            
            
            if temp==None:
                continue
                
            
            if v=='a':
                continue
            
            if temp.left==None:
                temp.left=TreeNode('a')
                
            l[temp.left]=level+1
            q.put(temp.left)
            if temp.right==None:
                temp.right=TreeNode('a')
            
            l[temp.right]=level+1
            q.put(temp.right)

        
        
        s= set( d[level] )
        
        if len(s)==1 and 'a' in s:
            level=level-1
        
        
        for x in range(0,level):
            
            temp=d[x]
            it=len(d[x])
            
            for i,y in enumerate(temp):
                prev=False
                if y=='a' and x<level:
                    return False

                   
        prev=False
        
        for i,x in enumerate(d[level]):
            
            if x!='a':
                if prev==False:
                    continue
                else:
                    return False
            
            if x=='a':
                prev=True
                
        return True
