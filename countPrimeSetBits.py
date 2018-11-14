class Solution(object):
    result={}
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        temp=0
        for x in range(L,R+1):
            
            if self.checkPrime(self.getNumOfOnes(x)):
                temp+=1
        
        return temp
        
    
    
    def getNumOfOnes(self,num):
        temp=0
        while num!=0:
            if num&1==1:
                temp+=1
            num=num>>1
        
        return temp
    
    def checkPrime(self,num):
        
        if num in self.result.keys():
            return self.result[num]
        
        if num<2:
            self.result[num]=False
            return False
        if num==2 or num==3:
            self.result[num]=True
            return True
        
        for x in range(2,int(math.sqrt(num))+1):
            if num%x==0:
                self.result[num]=False
                return False
        self.result[num]=True
        
        return True
