class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res=[]
        for i in range(len(nums1)):
            res.append(nums1[i])
        for i in range(len(nums2)):
            res.append(nums2[i]) 
        l=0
        r=len(res)-1
        res.sort()
        mid=(l+r)//2
        if len(res)%2!=0:
            return res[mid]
        else:
            ans=(res[mid]+res[mid+1])/2
            return ans


        