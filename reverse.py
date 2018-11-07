class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        max=int(math.pow(2,31))-1
        min=int(math.pow(2,31)*(-1))

        y=str(x)
        temp=0
        
        if "-" in y:
            y=y[1:len(y)]
            temp=int(y[::-1])*(-1)
        else:
            temp=int(y[::-1])
        
        if temp<min:
            return 0
        if temp >max:
            return 0
        return temp
