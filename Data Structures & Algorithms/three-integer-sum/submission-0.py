class Solution:
    def two_sum(self, nums, target, start):
        seen = set()
        pairs = []

        for j in range(start, len(nums)):
            need = target - nums[j]

            if need in seen:
                pairs.append((need, nums[j]))

            seen.add(nums[j])

        return pairs

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
    
        for i in range(len(nums) - 2):
            pairs = self.two_sum(nums, -nums[i], i + 1)
    
            for a, b in pairs:
                triplet = tuple(sorted((nums[i], a, b)))
                res.add(triplet)

        return [list(t) for t in res]