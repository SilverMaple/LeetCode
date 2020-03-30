/*
 * @lc app=leetcode id=540 lang=cpp
 *
 * [540] Single Element in a Sorted Array
 */
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int l = 0, h = nums.size() - 1;
        while (l<h) {
            int m = l + (h - l) / 2;
            if (m %2 == 1)
                m--;
            if (nums[m] == nums[m+1])
                l = m + 2;
            else
                h = m;
        }
        return nums[l];
    }
};
// @lc code=end

