class MyHashMap:

    l=[]
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l=[None]*5
        
    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        hKey=self.mHash(key)
        if self.l[hKey]==None:
            self.l[hKey]=[[key,value]]
        else:
            temp=self.l[hKey]
            for x in temp:
                if x[0]==key:
                    x[1]=value
                    return
            temp.append([key,value])
        
    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hKey=self.mHash(key)
        temp=self.l[hKey]
        if temp==None:
            return -1
        else:
            for x in temp:
                if x[0]==key:
                    return x[1]
        return -1
        
        
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        hKey=self.mHash(key)
        temp=self.l[hKey]
        if temp==None:
            return
        for i,v in enumerate(temp):
            if v[0]==key:
                temp.pop(i)
        
    def mHash(self,key):
        return key%5


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
