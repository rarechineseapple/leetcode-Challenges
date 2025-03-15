class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)): # eg. starts with 2, ends on 15
            for j in range(i + 1, len(nums)): # prevents duplicate numbers, e.g. starts with 7, ends on 15
                if nums[i] + nums[j] == target:
                    return [i, j]

        #if nums = [2,7,11,15]
        #i = 0, j = 1, 2, 3
        #i = 1, j = 2, 3
        #i = 2, j = 3
        #i = 3, j = no value, loop exits.
        #Brute forced
