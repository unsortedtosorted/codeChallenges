class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        def fun(a):
            i,word=a.split(" ",1)
            temp=ord(word[0])
            if temp>=ord('a') and temp<=ord('z'):
                return (0,word,i)
            else:
                return (1,)
            
        return (sorted(logs,key=fun))
