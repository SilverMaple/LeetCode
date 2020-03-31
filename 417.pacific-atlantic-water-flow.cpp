/*
 * @lc app=leetcode id=417 lang=cpp
 *
 * [417] Pacific Atlantic Water Flow
 */
#include <vector>
#include <string>
using namespace std;

// @lc code=start
class Solution {
public:
    vector<vector<int>> res;
    vector<vector<int>> visited;

    // dfs+bit manipulation
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {
        if (matrix.empty())
            return res;
        int m = matrix.size(), n = m ? matrix[0].size() : 0;
        visited.resize(m, vector<int>(n, 0));
        for (int i = 0; i < m; i++) {
            dfs(matrix, i, 0, INT_MIN, 1);    // pacific
            dfs(matrix, i, n - 1, INT_MIN, 2); // atlantic
        }
        for (int i = 0; i < n; i++) {
            dfs(matrix, 0, i, INT_MIN, 1);
            dfs(matrix, m-1, i, INT_MIN, 2);
        }
        return res;
    }

    void dfs(vector<vector<int>>& matrix, int x, int y, int pre, int preval) {
        // 判断边界条件、逻辑条件（可到达、已从一边遍历、已满足结果条件）
        if(x<0||x>=matrix.size()||y<0||y>=matrix[0].size()|| 
            matrix[x][y] < pre || visited[x][y]==3 || visited[x][y]==preval)
            return;
        visited[x][y] |= preval;
        if (visited[x][y] == 3)
            res.push_back({x, y});
        dfs(matrix, x+1, y, matrix[x][y], visited[x][y]);
        dfs(matrix, x-1, y, matrix[x][y], visited[x][y]);
        dfs(matrix, x, y+1, matrix[x][y], visited[x][y]);
        dfs(matrix, x, y-1, matrix[x][y], visited[x][y]);
    }
};
// @lc code=end

