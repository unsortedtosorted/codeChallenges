class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        temp=root
        
        while temp:
            if(temp.val==val):
                return temp
            elif temp.val>val:
                temp=temp.left
            else:
                temp=temp.right
         
        return None
        
