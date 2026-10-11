class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mydict={}
        for i,n in enumerate(nums):
            mydict[n]=i
        if target in mydict:
            return mydict[target] 
        else:
            return -1        
        