#
# @lc app=leetcode id=451 lang=python
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # dictionary to store count of character appearing in the string
        dic = {}
        
        # final result
        result = ""
        
        # loop through each char, and add the count to the dic
        for char in s:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1
                
        # sort the dic on values in reverse order
        sorted_dic = sorted(dic, key=dic.get, reverse=True)
        
        # loop through, and create final string
        for count in sorted_dic:
            result += count * (dic[count])

        return result
# @lc code=end

