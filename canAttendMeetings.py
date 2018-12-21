"""


"""


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
        s=set()
        for x in intervals:
            for y in range(x.start+1,x.end+1):
                if y in s:
                    return False
                else:
                    s.add(y)

        return True
