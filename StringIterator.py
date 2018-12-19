"""
100% faster
"""

class StringIterator:

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.str=compressedString
        self.curr=0
        self.num,self.n= self.getNum(self.curr)

        
        

    def next(self):
        """
        :rtype: str
        """

        if self.num>0:
            self.num-=1
            return self.str[self.curr]
        elif self.num==0:
            self.curr=self.n
            self.num,self.n= self.getNum(self.curr)
            if self.num>0:
                self.num-=1
                return self.str[self.curr]
            elif self.num==-1:
                return " "
                
        elif self.num==-1:
            return " "
            
            

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.num==0:
            self.curr=self.n
            self.num,self.n= self.getNum(self.curr)
        if self.num>0:
            return True
        elif self.num==-1:
            return False
        
    def getNum(self,ind):
        temp=""
        i=ind+1
        
        while i<len(self.str):
            if not self.str[i].isalpha():
                temp=temp+self.str[i]
            else:
                break
            i+=1

        if temp=="":
            return -1,-1
        else:
            return int(temp),i

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
