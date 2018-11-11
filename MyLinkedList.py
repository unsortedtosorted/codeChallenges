class ll(object):
    
    def __init__(self,val,point):
        self.val=val
        self.next=point
        
class MyLinkedList(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.home=None
        
    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        temp=0
        curr=self.home
        if curr==None:
            return -1
        
        while curr.next:
            if(temp==index):
                return curr.val
            curr=curr.next
            temp+=1
       
        if temp!=index:
            return -1
        return curr.val
        
            
    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        if self.home==None:
            self.home=ll(val,None)
            return
        temp=ll(val,None)
        temp.next=self.home
        self.home=temp
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        
        curr=self.home
        while curr.next:
            curr=curr.next
        temp=ll(val,None)
        curr.next=temp
        
    
    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        
        

        curr=self.home
        if index==0:
            self.addAtHead(val)
            return
        
        temp=1
        if curr==None:
            return
        
        while curr.next:
            if(temp==index):
                break;
            curr=curr.next
            temp+=1
            
        
        if(temp!=index):
                return;
                
        iNode=curr
        toAdd=ll(val,None)
        iNoneNeigh=None
        
        if iNode.next:
            iNoneNeigh=iNode.next
        
        iNode.next=toAdd
        toAdd.next=iNoneNeigh
        
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        
        if self.home==None:
            return
        
        
        if index==0:
            if self.home.next:
                newHead=self.home.next
                self.home=newHead
              
            
    
        
        curr=self.home  
        temp=0
        while curr.next:
            if(temp==index-1):
                break;
            curr=curr.next
            temp+=1
       
        
        if(temp!=index-1):
            return;
        
        
        iNode=curr
        if iNode.next==None:
            return
        toDelete=None

        toDelete=iNode.next
        newineig=None
        if toDelete.next:
            newineig=toDelete.next
        iNode.next=newineig
            
       
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
