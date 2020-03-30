/*
 * @lc app=leetcode id=665 lang=cpp
 *
 * [665] Non-decreasing Array
 */
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int count = 0;
        for (int i = 1; i < nums.size() && count < 2; i++) {
            if (nums[i] >= nums[i-1])
                continue;
            count++;
            if (i-2 >=0&&nums[i-2] > nums[i]) {
                nums[i] = nums[i - 1];
            } else {
                nums[i - 1] = nums[i];
            }
        }
        return count <= 1;
    }
};
// @lc code=end

