from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        MIN = -10**9
        nums_set = set(nums)
        min_n = min(nums_set)
        max_seq = -1

        while len(nums_set) > max_seq:
            max_n = max(nums_set)
            seq = 1
            for i in range (max_n-1, min_n-1, -1):
                if i not in nums_set:
                    break
                seq += 1
            max_seq = max(max_seq, seq)
            nums_set.remove(max_n)
            
        return max_seq