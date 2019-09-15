#
# @lc app=leetcode id=18 lang=python
#
# [18] 4Sum
#
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        if len(nums) <= 0:
            return []
        length = len(nums)

        max_num = nums[-1]
        num_dict = {j:i for i, j in enumerate(nums)}
        s = []
        for i in range(length - 3):
            a = nums[i]
            if a + 3 * max_num < target:
                continue
            if a * 4 > target:
                break
            for j in range(i+1, length-2):
                b = nums[j]
                if a + b + 2 * max_num < target:
                    continue
                if a + b * 3 > target:
                    break
                for k in range(j+1, length-1):
                    c = nums[k]
                    d = target - (a+b+c)
                    if d > max_num:
                        continue
                    if d < c:
                        break
                    if d in num_dict and num_dict[d] > k and (a,b,c,d) not in s:
                        s.append((a,b,c,d))
        return s

