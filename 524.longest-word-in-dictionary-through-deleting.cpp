/*
 * @lc app=leetcode id=524 lang=cpp
 *
 * [524] Longest Word in Dictionary through Deleting
 */
#include <string>
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    string findLongestWord(string s, vector<string>& d) {
        string ans = "";
        for (string& word: d) {
            if (word.size() < ans.size() || word.size()== ans.size()&&word>=ans)
                continue;
            int j = 0, k =0;
            while (j<s.size() && k<word.size()) {
                if (s[j]==word[k])
                    k++;
                j++;
            }
            int n = word.size();
            if (k==n && ((ans.size()==n&&ans>word) || ans.size()<n))
                ans = word;
        }
        return ans;
    }
};
// @lc code=end

