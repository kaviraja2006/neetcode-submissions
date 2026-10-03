class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mydict={}
        res=0
        left=0
        for r in range(len(s)):
            if s[r] in mydict:
                mydict[s[r]]+=1
            else:
                mydict[s[r]]=1
            while (((r-left+1)-max(mydict.values()))>k):
                mydict[s[left]]-=1
                left+=1
            res=max(res,r-left+1)    
        return res                 
        