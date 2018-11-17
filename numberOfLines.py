class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        nw=0
        nl=0
        
        for x in S:
            nw=nw+widths[ord(x)-ord('a')]
            if nw==100:
                nw=0
                nl+=1
            if nw>100 and nw%100!=0:
                nw=widths[ord(x)-ord('a')]
                nl+=1
        if nw!=0:
            nl+=1
        return [nl,nw]
