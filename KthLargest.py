class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.l=nums
        self.n=k
        self.last=-sys.maxsize-1
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        
        k=self.n
        self.l.append(val)
        
        
        def quickSelect(arr,k):
            
            big=[]
            small=[]
            
            piv=random.randint(0,len(arr)-1)
            temp=arr[piv]
            for i,x in enumerate(arr):
                if i==piv:
                    continue
                if x>temp:
                    big.append(x)
                else:
                    small.append(x)
            
            big.append(temp)
            
            if len(big)==k:
                return big[-1]
            
            elif len(big)>k:
                return quickSelect(big,k)
            else:
                return quickSelect(small,k-len(big))
        if val>self.last:
            self.last=quickSelect(self.l,k)
        
        return self.last
