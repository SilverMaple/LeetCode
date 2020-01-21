#
# @lc app=leetcode id=744 lang=python
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        n = len(letters)
        l = 0
        h = n -1
        while l <= h:
            m = l + (h-l)//2
            if letters[m] <= target:
                l = m+1
            else:
                h = m-1
        return letters[l] if l < n else letters[0]
# @lc code=end

