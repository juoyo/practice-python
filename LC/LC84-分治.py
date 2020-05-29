from typing import List


class Solution:
    def calculate_area(self, heights, left, right):  # [left, right]为计算区间
        print(left, right)
        if left == right:
            return heights[left]
        if left > right or left < 0 or right < 0:
            return 0
        temp_min = min(heights[left: right + 1])
        temp_min_index = heights.index(temp_min)

        cur_aera = temp_min * (right - left + 1)
        left_area = self.calculate_area(heights, left, temp_min_index - 1)
        right_area = self.calculate_area(heights, temp_min_index + 1, right)
        print(cur_aera, left_area, right_area)
        return max(cur_aera, left_area, right_area)

    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]
        return self.calculate_area(heights, 0, len(heights) - 1)


s = Solution()
print(s.largestRectangleArea( [2,1,5,6,2,3]))