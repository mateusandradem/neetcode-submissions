from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = defaultdict(int)
        td = defaultdict(int)

        for si in s:
            sd[si] += 1
        for ti in t:
            td[ti] += 1

        return sd == td