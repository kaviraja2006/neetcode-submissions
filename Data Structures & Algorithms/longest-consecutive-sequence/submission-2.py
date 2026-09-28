class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=sorted(set(nums))
        if not res:
            return 0
        
        maxlong=1
        longest=1
        for i in range(1,len(res)):
            if res[i]==res[i-1]+1:
                longest+=1
            else:
                longest=1
            maxlong=max(maxlong,longest)    
        return maxlong        

        