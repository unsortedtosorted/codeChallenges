# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        
        curr=head
        
        if head.next is not None:
            nex=head.next
        else:
            return head
        
        while nex is not None:
            if curr.val==nex.val:
                curr.next=nex.next
                nex=curr.next
                
            else:
                curr=curr.next
                nex=nex.next
        
        
        return head
                
            
