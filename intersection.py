class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        s1=set()
        s2=set()
        common=set()
        x=0
        while x <(max(len(nums1),len(nums2))):
            
            if x<len(nums1):
                s1.add(nums1[x])
            if x<len(nums2):
                s2.add(nums2[x])
            
            if x<len(nums1) and nums1[x] in s2:
                common.add(nums1[x])
            if x<len(nums2) and nums2[x] in s1:
                common.add(nums2[x])
            x=x+1
        print (s1)
        return list(common)
