/*
 * @lc app=leetcode id=17 lang=cpp
 *
 * [17] Letter Combinations of a Phone Number
 */
#include <vector>
#include <string>
#include <iostream>
using namespace std;

// @lc code=start
class Solution {
public:
    // 迭代法
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        if (digits.empty())
            return res;

        static const vector<string> v = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        res.push_back("");
        for (int i = 0; i < digits.size(); ++i) {
            int num = digits[i] - '0';
            if (num<0 || num>9)
                break;
            const string &candidate = v[num];
            if (candidate.empty())
                continue;
            vector<string> tmp;
            for (int j = 0; j < candidate.size(); ++j) {
                for (int k = 0; k < res.size(); ++k) {
                    tmp.push_back(res[k] + candidate[j]);
                }
            }
            res.swap(tmp);
        }
        return res;
    }

    // 递归法
    vector<string> letterCombinations1(string digits) {
        vector<string> res;
        if (digits.empty())
            return res;
        bfs("", res, digits);
        return res;
    }

    void bfs(string prefix, vector<string>& res, const string digits) {
        if (prefix.size() == digits.size()) {
            res.push_back(prefix);
            return;
        }
        static const vector<string> v = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        int curDigits = digits[prefix.size()] - '0';
        string candidate = v[curDigits];
        for (int j = 0; j < candidate.size(); ++j) {
            bfs(prefix+candidate[j], res, digits);
        }
    }
};
// @lc code=end

int main() {
    auto v = Solution().letterCombinations1("23");
    // auto v = Solution().letterCombinations("23");
    printf("%d", v.size());
    // cout << v.size();
}