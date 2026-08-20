class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_s1 = sorted(s1)
        k = len(s1)

        for i in range(len(s2)):
            if sorted_s1 == sorted(s2[i:i+k]):
                return True

        return False