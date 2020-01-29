#
# @lc app=leetcode id=739 lang=python
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        n = len(T)
        dist = [0]*n
        indexs = []
        for curIndex in range(n):
            while indexs and T[curIndex] > T[indexs[-1]]:
                preIndex = indexs.pop()
                dist[preIndex] = curIndex - preIndex
            indexs.append(curIndex)
        return dist
# @lc code=end

