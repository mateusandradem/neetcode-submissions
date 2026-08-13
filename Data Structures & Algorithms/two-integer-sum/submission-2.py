class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_idxs = [(i, nums[i]) for i in range(len(nums))]
        nums_sorted = sorted(nums_idxs, key=lambda num: num[1])
        i = 0
        j = len(nums) - 1

        while True:
            sum_nums = nums_sorted[i][1] + nums_sorted[j][1]
            if sum_nums == target:
                break
            elif sum_nums > target:
                j -= 1
            else:
                i += 1

        return [min(nums_sorted[i][0], nums_sorted[j][0]),
                max(nums_sorted[i][0], nums_sorted[j][0])]