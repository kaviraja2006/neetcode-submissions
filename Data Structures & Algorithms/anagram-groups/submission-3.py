class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)
        for s in strs:
            sSorted=tuple(sorted(s))
            hashmap[sSorted].append(s)
        return list(hashmap.values())    
        