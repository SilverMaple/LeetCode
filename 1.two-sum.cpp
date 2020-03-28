/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 */

// @lc code=start
using namespace std;
#include <vector>
#include <unordered_map>
#include <iostream>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> record;

        for (auto i = 0; i < nums.size(); ++i) {
            auto item = record.find(target - nums[i]);
            if (item != record.end()) {
                return {item->second, i};
            }

            record[nums[i]] = i;
        }
        return {0, 0};
    }
};

int main(void) {
    Solution s;
    vector<int> arr = {1,2,3,4,5,6,7,8};
    vector<int> result = s.twoSum(arr, 13);
    for (auto i = 0; i < result.size(); ++i) {
        cout << result[i];
    }
}
// @lc code=end

