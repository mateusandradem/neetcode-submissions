class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = {}

        for s in strs:
            key = ''.join(sorted(s))
            if key in anag:
                anag[key].append(s)
            else:
                anag[key] = [s]

        return [[s for s in anag[k]] for k in anag]