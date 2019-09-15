#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (25.64%)
# Total Accepted:    391.3K
# Total Submissions: 1.5M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
# 
# You may assume nums1 and nums2 cannot be both empty.
# 
# Example 1:
# 
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# 
# 
# Example 2:
# 
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5
# 
# 
#
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)
        length = len(nums)
        if length % 2 == 1:
            return nums[length//2]
        else:
            return (nums[length//2-1] + nums[length//2]) / 2.0

        # sorted_joined = sorted(nums1 + nums2)
        # if len(sorted_joined) % 2 == 0:
        #     index = int(len(sorted_joined) / 2)
        #     return (sorted_joined[index] + sorted_joined[index-1])/2
        # else:
        #     index = (int(len(sorted_joined)/2))
        #     return sorted_joined[index]
        
# l1 = [1, 3, 4, 5, 8]
# l2 = [2, 1, 4]
l1 = [1, 2]
l2 = [3, 4]
s = Solution()
print(s.findMedianSortedArrays(l1, l2))
