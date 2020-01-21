#
# @lc app=leetcode id=215 lang=python
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.quickSelect(nums, 0, len(nums)-1, k)

    def quickSelect(self, nums, start, n, k):
        pos = self.partition(nums, start, n)
        if pos == k-1:
            return nums[pos]
        elif pos >= k:
            return self.quickSelect(nums, start, pos-1, k)
        else:
            return self.quickSelect(nums, pos+1, n, k)

    def partition(self, nums, left, right):
        pivot = nums[right]
        i = left
        for j in range(left, right):
            if nums[j] > pivot:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        nums[right], nums[i] = nums[i], nums[right]
        return i
        
# @lc code=end

