/*
 * @lc app=leetcode id=79 lang=cpp
 *
 * [79] Word Search
 */
#include <vector>
#include <string>
using namespace std;

// @lc code=start
class Solution {
public:
    int m, n;
    int directions[5] = {0, 1, 0, -1, 0};
    bool exist(vector<vector<char>>& board, string word) {
        m = board.size();
        n = m ? board[0].size() : 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (dfs(board, word, i, j, 0))
                    return true;
        return false;
    }

    bool dfs(vector<vector<char>>& board, string word, int x, int y, int depth) {
        if (depth==word.size())
            return true;
        if (x<0||x>=m||y<0||y>=n||board[x][y]=='*'||board[x][y]!=word[depth])
            return false;

        board[x][y] = '*';
        for (int i = 0; i < 4; i++) {
            if (dfs(board, word, x + directions[i], y + directions[i + 1], depth + 1))
                return true;
        }
        board[x][y] = word[depth];
        return false;
    }
};
// @lc code=end

