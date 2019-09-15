#
# @lc app=leetcode id=6 lang=python
#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (30.87%)
# Total Accepted:    292.9K
# Total Submissions: 948.9K
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
# 
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# 
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a
# number of rows:
# 
# 
# string convert(string s, int numRows);
# 
# Example 1:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# 
# 
# Example 2:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# 
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# 
#
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        '''
        0 2 4 6 8
        1 3 5 7 9

        0   4   8     12
        1 3 5 7 9  11 13
        2   6   10
        
        0     6      12
        1   5 7   11 13
        2 4   8 10
        3     9
        '''
        # if numRows == 1:
        #     print(s)
        #     return s
        # result = ''
        # for i in range(numRows):
        #     if i == 0 or i == numRows - 1:
        #         result += ''.join([s[i] for i in range(i, len(s), (numRows-1)*2)])
        #     else:
        #         result += ''.join([s[i] for i in range(numRows-1, len(s), (numRows-1)*2)])
        # print(result)

        # Runtime: 68 ms, faster than 59.40% of Python online submissions.
        # Memory Usage: 10.7 MB, less than 82.98% of Python online submissions.
        ''' visit by row '''
        ''' start faster than the solution in discussion 2333 '''
        if numRows == 1:
            # print(s)
            return s
        result = ''
        span = (numRows-1)*2
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                result += ''.join([s[i] for i in range(i, len(s), span)])
            else:
                for j in range(i, len(s), span):
                    result += s[j]
                    if j + span - 2*i< len(s):
                        result += s[j + span - 2*i]
        # print(result)
        return(result)
        
s = Solution()
s.convert('PAYPALISHIRING', 4)
s.convert('0123456789', 4)
s.convert('0123456789', 3)
s.convert('0123456789', 2)
s.convert('0123456789', 1)

