#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        cnt = 0
        while z!=0:
            z &= (z-1) # 去除z最低位的1
            cnt += 1
            # if z&1 == 1:
            #     cnt+=1
            # z >>= 1
        return cnt
# @lc code=end

