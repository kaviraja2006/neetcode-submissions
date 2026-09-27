class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        postfix=[]
        res=[]
        pre=1
        for i in nums:
            pre=i*pre
            prefix.append(pre)
        pos=1   
        for i in reversed(nums):
            pos=i*pos
            postfix.append(pos)
        postfix.reverse()    
        left=0
        while left<len(nums):
            if left==0:
                pro1=1
            else:
                pro1=prefix[left-1]    
            if left==len(nums)-1:
                pro2=1
            else:
                pro2=postfix[left+1]    
            product=pro1*pro2
            res.append(product)
            left+=1
        return res       
        