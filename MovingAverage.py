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
