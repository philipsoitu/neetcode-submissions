class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # if k == 0 or len(nums) == 0: return []

        groups = {}
        counts = {}

        for x in nums:
            old_count = -1
            if x in counts:
                old_count = counts[x]
                counts[x] += 1 
            else:
                old_count = 0
                counts[x] = 1

            if old_count in groups:
                groups[old_count].remove(x) 

                new_count = old_count + 1
                if new_count in groups:
                    groups[new_count].append(x)
                else:
                    groups[new_count] = [x]
            else:
                new_count = old_count + 1
                if new_count in groups:
                    groups[new_count].append(x)
                else:
                    groups[new_count] = [x]

        keys = sorted(groups.keys(), reverse=True)
        ans = []

        for count in range(len(nums), 0, -1):
            if count in groups:
                for num in groups[count]:
                    ans.append(num)
                    if len(ans) == k:
                        return ans
