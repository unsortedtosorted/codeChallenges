class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l=[]
        for i in range(1,n+1):
            temp=str(i)
            if i%3==0:
                temp="Fizz"
                if i%5==0:
                    temp=temp+"Buzz"
            if i%5==0 and i%3!=0:
                temp="Buzz"
            l.append(temp)
        return l
