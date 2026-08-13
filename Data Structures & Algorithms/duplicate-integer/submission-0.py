class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_count = set()
        for i in nums:
            if i in nums_count:
                return True
            nums_count.add(i)
        return False
