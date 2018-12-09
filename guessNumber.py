class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low=1
        up=n
        while True:
            num=(low+up+1)//2
            k=(guess(num))
            if k==-1:
                up=num-1
                continue
                  
            elif k==1:
                low=num+1
                continue
            elif k==0:
                return num
            

"""
2 2

low=1
up=2
num=1

low=1+1
up=2
num=2 return

2 1

low=1
up=2
num=1 return 1

10 6
low=1
up=10
num=5

low=6,
up=10
num=8

low=6
up=7
num6

10 7
low=6
up=10
num=8

"""
        
