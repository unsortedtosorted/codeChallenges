"""
Runs Faster than 100% online python submissions

"""

class RecentCounter(object):
    l=[]
    lastStart=0
    def __init__(self):
        self.l=[]
        self.lastStart=0
    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.l.append(t)
        end=t
        start=t-3000
        if start<0:
            return len(self.l)
        else:
            for x in range(self.lastStart,len(self.l)):
                if self.l[x]>=start:
                    self.lastStart=x
                    return len(self.l[self.lastStart:])
        
