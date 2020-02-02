#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = 0
        for num in nums:
            diff ^= num
        diff &= -diff # 得到组右侧不为0的一位
        ret = [0, 0]
        for num in nums:
            if num & diff == 0:
                ret[0] ^= num
            else:
                ret[1] ^= num
        return ret
# @lc code=end

