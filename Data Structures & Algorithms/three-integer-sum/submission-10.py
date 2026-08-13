from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        d = defaultdict(int)
        for n in nums:
            d[n] +=1
        print(d)
        for i in range(len(nums)):
            d[nums[i]] -= 1
            for j in range(i + 1, len(nums) - 1):
                d[nums[j]] -= 1
                t = -(nums[i] + nums[j])
                if t in d and d[t] > 0:
                    res.add(','.join(str(ns) for ns in sorted([nums[i], nums[j], t])))
            for x in range(i + 1, len(nums)):
                d[nums[x]] += 1
    
        resl = list(r.split(',') for r in res)
        for ri in range(len(resl)):
            resl[ri] = [int(resli) for resli in resl[ri]]

        return resl