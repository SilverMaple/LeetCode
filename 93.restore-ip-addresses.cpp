/*
 * @lc app=leetcode id=93 lang=cpp
 *
 * [93] Restore IP Addresses
 */
#include <vector>
#include <string>
#include <cstring>
using namespace std;

// @lc code=start
class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> ret;
        string ans;

        for (int a = 1; a <= 3; a++)
        for (int b = 1; b <= 3; b++)
        for (int c = 1; c <= 3; c++)
        for (int d = 1; d <= 3; d++)
            if ((a+b+c+d) == s.size()) {
                int A = stoi(s.substr(0, a));
                int B = stoi(s.substr(a, b));
                int C = stoi(s.substr(a+b, c));
                int D = stoi(s.substr(a+b+c, d));
                if (A<=255 && B<=255 && C<=255 && D<=255)
                    if ( (ans=to_string(A)+"."+to_string(B)+"."+to_string(C)+"."+to_string(D)).length() == s.length()+3)
                        ret.push_back(ans);
            }
        return ret;
    }

    vector<string> restoreIpAddresses1(string s) {
        vector<string> result;
        string ip;
        dfs(s, 0, 0, ip, result);
        return result;
    }

    void dfs(string s, int start, int step, string ip, vector<string>& result) {
        // 符合条件的结果
        if (start==s.size() && step==4) {
            ip.erase(ip.end() - 1); // 去除最后的'.'
            result.push_back(ip);
            return;
        }
        // 过滤不符合规则的情况
        if (s.size()-start > (4-step)*3)
            return;
        if (s.size()-start < (4-step))
            return;

        int num = 0;
        for (int i = start; i < start + 3; i++) {
            num = num * 10 + (s[i] - '0');
            if (num<=255) {
                ip += s[i];
                dfs(s, i + 1, step + 1, ip + '.', result);
            }
            // '0'开头不用继续取2位或3位
            if (num==0)
                break;
        }
    }
};
// @lc code=end

