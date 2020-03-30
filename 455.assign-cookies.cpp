/*
 * @lc app=leetcode id=455 lang=cpp
 *
 * [455] Assign Cookies
 */
#include <vector>
#include <algorithm>
using namespace std;

// @lc code=start
class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());

        int result = 0;
        for (int i = 0, j = 0; i < g.size() && j < s.size(); j++)
        {
            if (g[i]<=s[j]) {
                i++;
                result++;
            }
        }
        return result;
    }
};
// @lc code=end

