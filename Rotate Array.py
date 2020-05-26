class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        last = nums[len(nums)-1]
        while i<k:
            nums.insert(0, last)
            nums.pop()
            last = nums[len(nums)-1]
            i += 1
            