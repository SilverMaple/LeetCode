/*
 * @lc app=leetcode id=279 lang=cpp
 *
 * [279] Perfect Squares
 */
#include <queue>
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    int numSquares(int n) {
        // 平方数据
        vector<int> squares;
        int square = 1, diff = 3;
        while(square <= n) {
            squares.push_back(square);
            square += diff;
            diff += 2;
        }
        queue<int> q;
        vector<bool> marked(n+1, false);
        q.push(n);
        marked[n] = true;
        int level = 0;
        while (!q.empty()) {
            int size = q.size();
            level++;
            while (size-- > 0) {
                int cur = q.front();
                q.pop();
                for (int s: squares) {
                    int next = cur - s;
                    if (next < 0)
                        break;
                    if (next == 0)
                        return level;
                    if (marked[next])
                        continue;
                    marked[next] = true;
                    q.push(next);
                }
            }
        }
        return n;
    }
};
// @lc code=end

