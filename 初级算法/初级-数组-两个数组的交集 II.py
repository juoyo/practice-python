class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            temp = nums1
            nums1 = nums2
            nums2 = temp
        nums1_dict = {}
        for i in nums1:
            nums1_dict[i] = nums1_dict.get(i, 0) + 1
        res = []
        for j in nums2:
            if nums1_dict.get(j) > 0:
                res.append(j)
                nums1_dict[j] = nums1_dict[j] - 1
        return res


