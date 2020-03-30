/*
 * @lc app=leetcode id=452 lang=cpp
 *
 * [452] Minimum Number of Arrows to Burst Balloons
 */
#include <vector>
#include <algorithm>
using namespace std;

// @lc code=start
class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        if (points.size() == 0)
            return 0;
        sort(points.begin(), points.end(), [](const vector<int> &a, const vector<int> &b) {
            return a[1] < b[1];
        });

        int count = 1, end = points[0][1];
        for (int i = 1; i < points.size(); i++) {
            // 注意重叠区间跟合并区间的区别
            if (points[i][0] <= end)
                continue;
            count++;
            end = points[i][1];
        }
        return count;
    }
};
// @lc code=end

