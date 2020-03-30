/*
 * @lc app=leetcode id=1091 lang=cpp
 *
 * [1091] Shortest Path in Binary Matrix
 */
#include <vector>
#include <queue>
using namespace std;

// @lc code=start
class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        if (grid.size() == 0)
            return -1;
        int r = grid.size(), c = grid[0].size();
        int directions[8][2] = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
        
        queue<pair<int, int>> q;
        q.push({0, 0});
        int pathLength = 0;
        while (!q.empty()) {
            ++pathLength;
            int size = q.size();
            while (size-- > 0) {
                int x = q.front().first, y = q.front().second;
                q.pop();
                if (grid[x][y] == 1)
                    continue;
                if (x == r-1 && y == c-1)
                    return pathLength;

                grid[x][y] = 1; // 标记
                for (auto d: directions) {
                    int nr = x + d[0], nc = y + d[1];
                    if (nr < 0 || nr >= r || nc < 0 || nc >= c) {
                        continue;
                    }
                    q.push(make_pair(nr, nc));
                }
            }
        }
        return -1;
    }

    // 优化版本
    int shortestPathBinaryMatrix1(vector<vector<int>>& g, int steps=0) {
        queue<pair<int, int>> q;
        q.push({ 0, 0 });
        while (!q.empty()) {
            ++steps;
            queue<pair<int, int>> q1;
            while (!q.empty()) {
              auto c = q.front();
              q.pop();
              if (exchange(g[c.first][c.second], 1) == 1) continue;
              if (c.first == g.size() - 1 && c.second == g.size() - 1) return steps;
              for (auto i = c.first - 1; i <= c.first + 1; ++i)
                for (auto j = c.second - 1; j <= c.second + 1; ++j)
                  if (i != c.first || j != c.second) {
                    if (i >= 0 && j >= 0 && i < g.size() && j < g.size() && !g[i][j]) {
                      q1.push({ i, j });
                    }
                  }
            }
            swap(q, q1);
        }
        return -1;
    }
};
// @lc code=end

