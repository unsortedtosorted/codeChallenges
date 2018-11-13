"""
Runs 100% faster than all python submission

maintain 2 pointer 
curr starts at head
next start from head.next

if list is: 

2 2 3 4 5 5 

Check curr.val and next.val, 2==2
        curr.next=next.next
        next=curr.next
list= 2 3 4 5 5

curr at 2, next at 3
curr.val!=next.val, 2!=3
    curr=curr.next
    next=next.next

curr at 3, next at 4
curr.val!=next.val, 3!=4
    curr=curr.next
    next=next.next

curr at 5, next at 5
curr.val!=next.val, 5==5
    curr.next=next.next=None
    next=curr.next=None
   
next is None:
  break 
return head

"""

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
                
            
