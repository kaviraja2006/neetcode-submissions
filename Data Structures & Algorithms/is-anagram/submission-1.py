class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mydict={}
        for i in range (len(t)):
            if t[i] in mydict:
                mydict[t[i]]+=1
            else:
                mydict[t[i]]=1
        for i in range(len(s)):
            if s[i] in mydict and mydict[s[i]] > 0:
                mydict[s[i]]-=1
            else:
                return False
        return True
