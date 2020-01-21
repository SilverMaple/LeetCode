#
# @lc app=leetcode id=406 lang=python
#
# [406] Queue Reconstruction by Height
#

# @lc code=start
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = [[]]*len(people)
        people.sort(key = lambda x: (x[0],-x[1])) 
        indices = [i for i in range(len(people))]
        for j,(_,pk) in enumerate(people):
            i = indices.pop(pk)
            ret[i] = people[j]
        return ret
        
# @lc code=end

