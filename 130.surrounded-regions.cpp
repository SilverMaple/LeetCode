/*
 * @lc app=leetcode id=130 lang=cpp
 *
 * [130] Surrounded Regions
 */
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    void solve(vector<vector<char>>& board) {
        int m = board.size(), n = m ? board[0].size() : 0;
        for (int i = 0; i < m; i++) {
            dfs(board, i, 0);
            dfs(board, i, n - 1);
        }
        for (int j = 0; j < n; j++) {
            dfs(board, 0, j);
            dfs(board, m - 1, j);
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == '.')
                    board[i][j] = 'O';
                else if (board[i][j] == 'O')
                    board[i][j] = 'X';
            }
        }
    }

    void dfs(vector<vector<char>>& board, int i, int j) {
        if (i<0||i>=board.size()||j<0||j>=board[0].size()||board[i][j]!='O')
            return;
        board[i][j] = '.';
        dfs(board, i + 1, j);
        dfs(board, i - 1, j);
        dfs(board, i, j + 1);
        dfs(board, i, j - 1);
    }
};
// @lc code=end

