/*
 * @lc app=leetcode id=435 lang=cpp
 *
 * [435] Non-overlapping Intervals
 */
#include <vector>
#include <algorithm>
using namespace std;

// @lc code=start
class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if (intervals.size() == 0)
            return 0;
        // 匿名函数/lambda
        // auto compare = [](const vector<int> &a, const vector<int> &b) { return (a[1] < b[1]); };
        sort(intervals.begin(), intervals.end(), compare);
        int count = 1, end = intervals[0][1];
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i][0] < end)
                continue;
            end = intervals[i][1];
            count++;
        }
        return intervals.size() - count;
    }

    static bool compare(const vector<int> &x, const vector<int> &y) {
        return x[1] < y[1];
    }
};
// @lc code=end

