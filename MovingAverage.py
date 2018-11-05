"""
No looping required, faster than 99.87% python solutions

1, sum=1,[1], return 1
10 sum=11, [1,10] return (11/2)
3 sum=14 [1,10,3] return 14/3
5 sum=19 [1,10,3,5] d[4-3-1]=1 19-1, sum 18, return 18/3
4 sum=22 [1,10,3,5,4] d[5-3-1]=d[1]=10 22-10=12 return 12/3=4


"""  


class MovingAverage(object):

    size=0
    d=[]
    sum=0
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size=size
        self.d=[]
        self.sum=0

    def next(self, val):
        self.sum=self.sum+val
        self.d.append(val)
        
        if(len(self.d)<=self.size):
            return float(self.sum)/len(self.d)
        else:
            self.sum=self.sum-self.d[len(self.d)-self.size-1]
            return float(self.sum)/self.size
