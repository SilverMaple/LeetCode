/*
 * @lc app=leetcode id=695 lang=cpp
 *
 * [695] Max Area of Island
 */
#include <vector>
#include <iostream>
using namespace std;

// @lc code=start
class Solution {
public:
    // 查找最大连通面积，dfs搜索
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int maxSize = 0;
        // 遍历
        for (int i = 0; i < grid.size(); i++)
            for (int j = 0; j < grid[0].size(); j++)
                if (grid[i][j] == 1)
                    maxSize = max(maxSize, dfs(grid, i, j));

        return maxSize;
    }

    int dfs(vector<vector<int>>& grid, int i, int j) {
        if (i<0 || i>=grid.size() || j<0 || j>=grid[0].size() || grid[i][j]==0)
            return 0;
        grid[i][j] = 0;
        return 1 + dfs(grid, i+1, j) + dfs(grid, i-1, j) + dfs(grid, i, j+1) + dfs(grid, i, j-1);
    }
};
// @lc code=end
int main() {
    vector<vector<int>> v = {{0, 1}};
    int iv = Solution().maxAreaOfIsland(v);
    cout << iv;
}
