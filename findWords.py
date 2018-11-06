class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        l1=['q','w','e','r','t','y','u','i','o','p']
        l2=['a','s','d','f','g','h','j','k','l']
        l3=['z','x','c','v','b','n','m']
        
        l=[]
        for x in words:
            prev=None
            l.append(x)
            for y in x:
                temp=y.lower()
                if prev==None:
                    if temp in l1:
                        prev=1
                    elif temp in l2:
                        prev=2
                    else:
                        prev=3
                else:
                    if temp in l1 and prev==1:
                        continue
                    elif temp in l2 and prev==2:
                        continue
                    elif temp in l3 and prev==3:
                        continue
                    else:
                        l.pop()
                        break         
        return l 
