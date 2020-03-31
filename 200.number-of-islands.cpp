/*
 * @lc app=leetcode id=200 lang=cpp
 *
 * [200] Number of Islands
 */
#include <queue>
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    // dfs, 比bfs快
    int numIslands1(vector<vector<char>>& grid) {
        int count = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == '1') {
                    count++;
                    dfs(grid, i, j);
                }
            }
        }
        return count;
    }

    void dfs(vector<vector<char>>& grid, int i, int j) {
        if (i<0||i>=grid.size()||j<0||j>=grid[0].size()||grid[i][j]=='0')
            return;
        grid[i][j] = '0';
        dfs(grid, i - 1, j);
        dfs(grid, i + 1, j);
        dfs(grid, i, j - 1);
        dfs(grid, i, j + 1);
    }

    // bfs with queue
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size(), n = m ? grid[0].size() : 0;
        int count = 0;
        int offset[] = {0, 1, 0, -1, 0};
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '0') {
                    continue;
                }
                grid[i][j] = '0';
                count++;
                queue<pair<int, int>> todo;
                todo.push(make_pair(i, j));
                while (!todo.empty()) {
                    auto p = todo.front();
                    todo.pop();
                    for (int k = 0; k < 4; k++) {
                        int r = p.first + offset[k], c = p.second + offset[k + 1];
                        if (r<0||r>=m||c<0||c>=n||grid[r][c]=='0')
                            continue;
                        grid[r][c] = '0';
                        todo.push(make_pair(r, c));
                    }
                }
            }
        }
        return count;
    }
};
// @lc code=end

