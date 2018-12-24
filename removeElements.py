class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        prev=head
        
        if not prev:
            return head
        
        curr=prev.next
        
        while curr!=None:
            
            if curr.val==val:
                prev.next=curr.next
                
            else:
                prev=curr
            curr=curr.next
        
        if head.val==val:
            return head.next
        return head
