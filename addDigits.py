"""
 Runs faster than 99.88%,
 
 if num=1234
 output =1+2+3+4=3+7=10=1+0=1
 

keep subtracting by 9 until output is less than 10 or 
divide by 9 ,multiply output by 9, subtract by number.

e.g  17
int(17/9) = 1
17-9*1=8

output=8
"""



class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num<10: 
            return num
        
        if num%9==0:
            return 9
        else:
            return num-int(num/9)*9
