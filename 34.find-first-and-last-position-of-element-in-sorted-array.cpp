/*
 * @lc app=leetcode id=34 lang=cpp
 *
 * [34] Find First and Last Position of Element in Sorted Array
 */
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int idx1 = lower_bound(nums, target);
        int idx2 = lower_bound(nums, target + 1)-1;
        if (idx1 < nums.size() && nums[idx1] == target)
            return {idx1, idx2};
        else
            return {-1, -1};
    }

    int lower_bound(vector<int>& nums, int target) {
        int l = 0, h = nums.size() - 1, m;
        // 以下判定若包含等于，则下面 h= m-1;
        // 不包含则下面 h= m;
        while (l<=h) {
            m = l + (h - l) / 2;
            if (nums[m] < target)
                l = m + 1;
            else
                h = m-1;
        }
        return l;
    }
};
// @lc code=end

