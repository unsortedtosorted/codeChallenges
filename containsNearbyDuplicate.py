"""
1 -->0
2 -->1
3 -->2
1 --> 0,3 -->3 true

1 -->0
0-->1
1-->0,2 -->not 1
1 -->0,2,3 --> yes

1-->0
2-->1
3-->2
1-->0,3
2-->1,4
3-->2,5

"""


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d={}
        
        for i,x in enumerate(nums):
            
            if x in d.keys():
                temp=d[x]
                temp.append(i)
                d[x]=temp
            else:
                d[x]=[i]
    
        for x in d:
            temp=d[x]
            if len(temp)>1:
                for y in range(0,len(temp)):
                    for z in range(y,len(temp)): 
                        if temp[y]==temp[z]:
                            continue
                        else:
                            if temp[z]-temp[y]<=k:
                                return True
                
            
        
        return False
        
