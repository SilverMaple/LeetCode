#
# @lc app=leetcode id=345 lang=python
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v = set("aeiouAEIOU")
        i = 0
        j = len(s) - 1
        a = list(s)
        while i<j:
            if a[i] in v and a[j] in v: 
                a[i],a[j],i,j = a[j],a[i],i+1,j-1 
            elif a[j] in v: 
                i+=1 
            else: 
                j-=1
        return "".join(a)
        
# @lc code=end

