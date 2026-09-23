class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        left=1
        while left<len(nums):
            if nums[left]==nums[left-1]:
                return True
            else:
                left+=1
        return False          
        