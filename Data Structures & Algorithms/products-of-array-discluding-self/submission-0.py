class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        has_zero = False
        zero_idx = -1
        for n in nums:
            if n == 0:
                if has_zero is False:
                    has_zero = True
                    continue
                p = 0
                break
            p *= n

        if p == 0:
            return [0] * len(nums)

        if has_zero is True:
            return [p if n == 0 else 0 for n in nums]

        return [p//n for n in nums]
        