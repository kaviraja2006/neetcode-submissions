class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mymap={}
        for i in range(len(s)):
            if s[i] in mymap:
                mymap[s[i]]+=1
            else:
                mymap[s[i]]=1
        for i in range(len(s)):
            if t[i] in mymap:
                mymap[t[i]]-=1
            else:
                return False
        for value in mymap.values():
            if value!=0:
                return False
        return True            


        