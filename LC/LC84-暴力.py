from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]
        maxs = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                templ = min(heights[i:j+1])
                s = templ * (j - i + 1)
                maxs = max(maxs, s)
        return maxs


s = Solution()
print(s.largestRectangleArea([0, 9]))