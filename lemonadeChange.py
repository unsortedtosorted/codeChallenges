class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        bill={}
        bill[5]=0
        bill[10]=0
        bill[20]=0
        
        for x in bills:
            if x==5:
                bill[x]+=1
            elif x==10:
                if bill[5]>0:
                    bill[x]+=1
                    bill[5]-=1
                else:
                    return False
            elif x==20:
                if bill[10]>0 and bill[5]>0:
                    bill[10]-=1
                    bill[5]-=1
                elif bill[5]>2:
                    bill[5]-=3
                else:
                    return False
    
        return True
