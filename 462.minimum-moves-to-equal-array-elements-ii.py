#
# @lc app=leetcode id=462 lang=python
#
# [462] Minimum Moves to Equal Array Elements II
#

# @lc code=start
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sorted(nums)
        # move = 0
        # l, h = 0, len(nums)-1
        # while l<=h:
        #     move += nums[h]-nums[l]
        #     l+=1
        #     h-=1
        # return move
        nums.sort()
        return sum(nums[~i] - nums[i] for i in range(len(nums) / 2))

# @lc code=end

