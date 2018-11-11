class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        t=""
        flag=0
        
        while flag<32:
            if n&1==1:
                t=t+"1"
            else: t=t+"0"
            n=n>>1
            flag=flag+1

        return int(t,2)
