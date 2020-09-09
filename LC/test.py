from typing import List



ls1 = [[1, 2], [2]]
t = []
print(t.append(3))
print(t[:].append(3))

test = [['1', '2', '3'], ['3', '4', '5'], ['5', '6', '7']]
test = [['.'] * 3] * 3
def test_ls(test):
    test[0][0] = '0'
test_ls(test)
print(test)

ls = [1,4]
ls2 = [2]
ls2.append(ls[:])
ls[0] = 3
print(ls)
print(ls2)


class Solution:
    def calculate_area(self, heights, left, right):  # [left, right]为计算区间
        # print(left, right)
        if left > right:
            return 0
        temp_min_index = left
        for i in range(left + 1, right + 1):
            if heights[i] < heights[temp_min_index]:
                temp_min_index = i
        left_bigger_index = temp_min_index - 1
        right_bigger_index = temp_min_index + 1
        while left_bigger_index > 0 and heights[left_bigger_index] <= heights[temp_min_index]:
            left_bigger_index = left_bigger_index - 1
        while right_bigger_index < len(heights) and heights[right_bigger_index] <= heights[temp_min_index]:
            right_bigger_index = right_bigger_index + 1
        cur_aera = heights[temp_min_index] * (right - left + 1)
        left_area = self.calculate_area(heights, left, left_bigger_index)
        right_area = self.calculate_area(heights, right_bigger_index, right)
        # print(cur_aera, left_area, right_area)
        return max(cur_aera, left_area, right_area)

    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]
        return self.calculate_area(heights, 0, len(heights) - 1)


s = Solution()
print(s.largestRectangleArea( [2,1,5,6,2,3]))