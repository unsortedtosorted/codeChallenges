# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        
        def fun(x):
            return x.start
        
        k=sorted(intervals,key=fun)
        
        
        if len(k)<1:
            return True
        
        prev=k[0]
        
        
        for x in range(1,len(k)):
            if k[x].start>=prev.end:
                prev=k[x]
                continue
            else:
                return False
            
            
        return True
