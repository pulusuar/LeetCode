class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length_max = 0
        for i in range(0, len(nums)):
            if nums[i] != None:
                nums[length_max] = nums[i]
                length_max += 1
                for j in range(i+1, len(nums)):
                    if nums[i] == nums[j]:
                        nums[j] = None
        return length_max;
                        
