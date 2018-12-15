"""
nums1=[1,2,3,0,0,0]
nums2=[2,5,6]

i=0
j=0

nums1[i]<nums2[j] --> [1,2,3,0,0,0]
i=1,j=0
nums1[i]==nums2[j]--> [1,2,3,0,0,0]
i=2,j=0

nums1[i]!<nums2[j]

move all forwards [1,2,2,3,0,0]
i=+1=3,j=1

nums1[i]<nums[j]
i=4,j=1

if i>m:
[1,2,2,3,5]


"""



class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        i=0
        j=0
        
        def moveForward(arr,ind,val):
            temp=ind+1
            last=arr[ind]
            arr[ind]=val
            while temp<len(arr):
                curr=arr[temp]
                arr[temp]=last
                last=curr
                temp+=1
        l=0
        
        while l<m+n:
            
            if i<m and j<n:
                if nums1[i]<=nums2[j]:
                    i+=1
                else:
                    moveForward(nums1,i,nums2[j])
                    i+=1
                    j+=1
                    m+=1
            elif i>=m and j<n:
                    nums1[i]=nums2[j]
                    i+=1
                    j+=1
            l+=1
