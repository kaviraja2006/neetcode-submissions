class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict={}
        res=[]
        for key,values in enumerate(nums):
            if values in mydict:
                mydict[values]+=1
            else:
                mydict[values]=1
        sorteddict=dict(sorted(mydict.items(),key=lambda x:x[1], reverse=True))
        for i in sorteddict:
            res.append(i)
            if len(res)==k:
                break
        return res          
            


            
        