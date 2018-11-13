class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
      
        while node.next is not None:
            #copy value
            node.val=node.next.val
            prev=node
            node=node.next
        
        prev.next=None
        
