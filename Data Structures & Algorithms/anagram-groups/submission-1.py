class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict=defaultdict(list)
        for s in strs:
            sSorted=tuple(sorted(s))
            mydict[sSorted].append(s)
        return list(mydict.values())    
        