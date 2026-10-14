class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i,n in enumerate(nums):
            compli=target-n
            if compli in hashmap:
                return [hashmap[compli],i]
            else:
                hashmap[n]=i
                    
        