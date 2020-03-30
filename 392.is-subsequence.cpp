/*
 * @lc app=leetcode id=392 lang=cpp
 *
 * [392] Is Subsequence
 */
#include <string>
using namespace std;

// @lc code=start
class Solution {
public:
    bool isSubsequence(string s, string t) {
        int index = -1;
        for (int i = 0; i < s.size(); i++) {
            index = t.find(s[i], index+1);
            if (index == string::npos)
                return false;
        }
        return true;
    }
};
// @lc code=end

