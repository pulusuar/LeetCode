class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for num in nums:
            if num == target:
                return nums.index(num)
        for i in range(0, len(nums)):
            if nums[i]>target:
                return i
        return len(nums)