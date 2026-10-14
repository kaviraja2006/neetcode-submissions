class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        res=[]
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]]+=1
            else:
                hashmap[nums[i]]=1
        sortedkeys=sorted(hashmap.keys(),key=hashmap.get,reverse=True)        
        for i in range(k):
            res.append(sortedkeys[i])
        return res         

        