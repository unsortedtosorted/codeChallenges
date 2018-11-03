
class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        map={}
        counter=0
        toReturn=[]
        
        for i in B: 
            if i not in map:
                map[i]=[]
            map[i].append(counter)
            counter+=1
        
        for i in A:
            temp=map[i]
            toReturn.append(temp[0])
            if len(temp)>1:
                map[i]=temp[1:]
        
        return toReturn
        
