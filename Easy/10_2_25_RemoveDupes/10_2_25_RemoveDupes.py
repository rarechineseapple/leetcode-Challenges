class Solution(object):
    def removeDuplicates(self, nums):
        """
        #Remove Duplicates from Sorted Array
        # takes in nums list and removes duplicates
        # returns number of unique elements
        :type nums: List[int]
        :rtype: int
        """
        # nums = list(dict.fromkeys(nums))

        i = 0  # pointer for unique elements

        for j in range(1, len(nums)):  # start from the second element
            if nums[j] != nums[i]:  # if a new unique element is found
                i += 1  # move pointer forward
                nums[i] = nums[j]  # overwrite duplicate value

        for k in range(i + 1, len(nums)): # fills up nums with underscores
            nums[k] = "_"

        return i + 1



rd = Solution()

nums = [0,0,1,1,1,2,2,3,3,4]
expectedNums = [2] # expected answer with correct length

k = rd.removeDuplicates(nums)
print(nums)
print(k)

