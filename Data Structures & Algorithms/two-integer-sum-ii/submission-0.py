class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        di = {numbers[i]: i for i in range(len(numbers))}
        for ni in range(len(numbers)):
            if target - numbers[ni] in di:
                return [min(di[target - numbers[ni]], ni) + 1,
                        max(di[target - numbers[ni]], ni) + 1]
