class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l=[None]*541
        

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        v=key%5
        
        if self.contains(key):
            return
        if self.l[v]==None:
            self.l[v]=[key]
        else:
            self.l[v].append(key)

        

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if  not self.contains(key):
            return
        
        else:
            self.l[key%5].remove(key)
            return

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        temp=self.l[key%5]
        
        if temp==None or key not in temp:
            return False
        else:
            return True
            
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
