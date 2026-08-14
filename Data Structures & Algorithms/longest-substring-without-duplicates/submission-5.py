class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        max_s = ''
        d = set()

        for i in range(len(s)):
            if s[i] in d:
                max_len = max(max_len, len(max_s))
                lc_idx = max_s.index(s[i])
                for j in range(lc_idx + 1):
                    d.discard(max_s[j])
                d.add(s[i])
                max_s = max_s[lc_idx + 1:] + s[i]
            else:
                d.add(s[i])
                max_s += s[i]
        max_len = max(max_len, len(d))

        return max_len
                