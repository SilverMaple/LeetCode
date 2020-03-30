/*
 * @lc app=leetcode id=53 lang=cpp
 *
 * [53] Maximum Subarray
 */
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if (nums.size()==0)
            return 0;
        int preSum = nums[0];
        int maxSum = preSum;
        for (int i = 1; i < nums.size(); i++) {
            preSum = preSum > 0 ? preSum + nums[i] : nums[i];
            maxSum = max(maxSum, preSum);
        }
        return maxSum;
    }
};
// @lc code=end

