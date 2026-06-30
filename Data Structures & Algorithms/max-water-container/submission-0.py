class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        l = 0
        r = len(heights) - 1

        while l <= r:
            area = (min(heights[l], heights[r])) * (r - l)
            best = max(best, area)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                # uhh 
                l += 1
        return best

            
