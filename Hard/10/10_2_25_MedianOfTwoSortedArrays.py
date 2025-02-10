class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # The code below works BUT does not achieve O(log (m+n)) complexity
        #
        # nums3 = nums1 + nums2 # this is O(m + n) where (nums1 of size m and nums2 of size n)
        # nums3.sort() # comparison-based sorting algorithm takes O(N log N)) where N = (m + n)
        #
        # length = len(nums3)
        # mid = length // 2
        #
        # if length % 2 == 0:
        #     #print("Even")
        #     median = (nums3[mid - 1] + nums3[mid]) / 2.0
        #     #print(median)
        #
        # else:
        #     #print("Odd")
        #     median = nums3[mid]
        #     #print(median)
        #
        # #print(nums3)
        # return median

        #
        # binary search is always performed on the smaller array
        # if nums1 is larger it swaps the two so we search smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # m and n are lengths of the lists
        # the left partition will contain the median
        # in the event that the result is odd, +1 ensures we have the extra element in the left partition
        m, n = len(nums1), len(nums2)
        left_half_size = (m + n + 1) // 2

        # low is the starting point of the list, high is the length of list
        low, high = 0, m

        # Binary Search
        while low <= high:
            i = (low + high) // 2  # partition index for nums1
            j = left_half_size - i  # partition index for nums2

            # handling out of bounds
            left1 = float('-inf') if i == 0 else nums1[i - 1] # largest numbers in left
            right1 = float('inf') if i == m else nums1[i] # smallest numbers in right
            left2 = float('-inf') if j == 0 else nums2[j - 1] # largest numbers in left
            right2 = float('inf') if j == n else nums2[j] # smallest numbers in right

            # if largest number on left <= smallest number of right,
            if left1 <= right2 and left2 <= right1:
                # found correct partition
                if (m + n) % 2 == 0: # even length list
                    return (max(left1, left2) + min(right1, right2)) / 2.0
                else: # odd length list
                    return max(left1, left2)
            elif left1 > right2:
                high = i - 1  # move partition left / reduce high
            else:
                low = i + 1  # move partition right / increase low

        # nums1, nums2 = [1, 3], [2], ensure nums1 is smaller with swap
        # nums1, nums2 = [2], [1, 3]
        # Step 1: Calculate left_half_size
        # left_half_size = (1 + 2 + 1) // 2 = 2
        # Step 2: Binary search on nums1
        # low = 0, high = 1
        # step 3: Calculate i and j
        # i = (0 + 1) // 2 = 0
        # j = left_half_size - i - 1 = 2 - 0 - 1 = 1
        # step 4: Extract partition values
        # since i == 0 (meaning no left elements in nums1)
        # left1 = float('-inf')  # Nothing on the left of nums1
        # right1 = nums1[i] = 2  # First element of nums1
        # since j != 0
        # left2 = nums2[j] = 1  # First element of nums2
        # right2 = nums2[j + 1] = 3  # Second element of nums2
        # step 5: check partition conditions
        # left1 (-inf) <= right2 (3)
        # left2 (1) <= right1 (2)
        # step 6: median
        # since total length (m+n) = 3 (odd), median is max(left1, left2)
        # max(left1, left2) = max(-inf, 1) = 2.0


ini = Solution()

nums1, nums2 = [1,2], [3,4]
nums = ini.findMedianSortedArrays(nums1, nums2)
print (f"{nums}")


