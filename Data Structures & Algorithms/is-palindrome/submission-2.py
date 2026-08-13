class Solution:
    def isPalindrome(self, s: str) -> bool:
        sl = [si for si in s.lower() if si.isalnum() is True]
        if len(sl) in (0, 1):
            return True
        len_2 = len(s) // 2
        for i in range(len_2):
            if sl[i] != sl[-(i+1)]:
                return False
        return True