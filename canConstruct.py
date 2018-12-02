class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        rn={}
        
        for x in ransomNote:
            if x in rn.keys():
                rn[x]+=1
            else:
                rn[x]=1

        for y in magazine:
            if y in rn.keys():
                rn[y]-=1
        

        return all(value <= 0 for value in rn.values())
