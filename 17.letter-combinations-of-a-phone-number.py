#
# @lc app=leetcode id=17 lang=python
#
# [17] Letter Combinations of a Phone Number
#
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        # √ 25/25 cases passed (12 ms)
        # √ Your runtime beats 93.81 % of python submissions
        # √ Your memory usage beats 19.05 % of python submissions (11.9 MB)

        # s = {i: [chr((i-2)*3+97+j) for j in range(3)] for i in range(2, 10)}
        s = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 
        5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 
        8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}

        result = ['']
        for c in digits:
            tmp = []
            for letter in s[int(c)]:
                tmp.extend([pre + letter for pre in result])
            result = tmp
        return sorted(result) if result != [''] else []


print(Solution().letterCombinations(""))
