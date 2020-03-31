/*
 * @lc app=leetcode id=547 lang=cpp
 *
 * [547] Friend Circles
 */
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    // dfs，标记是否访问
    int findCircleNum1(vector<vector<int>>& M) {
        if (M.empty())
            return 0;
        vector<bool> visited(M.size(), false);
        int groups = 0;
        for (int i = 0; i < visited.size(); i++)
            groups += !visited[i] ? dfs(i, M, visited), 1 : 0;
        return groups;
    }

    void dfs(int i, vector<vector<int>>& M, vector<bool>& visited) {
        visited[i] = true;
        for (int j = 0; j < visited.size(); j++)
            if (i!=j && M[i][j] && !visited[j])
                dfs(j, M, visited);
    }

    // 并查集
    int findCircleNum(vector<vector<int>>& M) {
        if (M.empty())
            return 0;
        int n = M.size();

        vector<int> leads(n, 0);
        for (int i = 0; i < n; i++)
            leads[i] = i;

        int groups = n;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j<n; j++) {
                if (M[i][j]) {
                    int lead1 = find(i, leads);
                    int lead2 = find(j, leads);
                    if (lead1 != lead2) {
                        leads[lead1] = lead2;
                        groups--;
                    }
                }
            }
        }
        return groups;
    }

    int find(int x, vector<int>& parents) {
        return parents[x] == x ? x : find(parents[x], parents);
    }

    // 并查集
    int findCircleNum(vector<vector<int>>& M) {
        int n = M.size();
        vector<int> leads(n, 0);
        for (int i = 0; i < n; i++)
            leads[i] = i;
        int groups = n;
        for (int i = 0; i < n; i++)
            for (int j = i+1; j < n; j++)
                if (M[i][j]) {
                    int lead1 = findLeader(i, leads);
                    int lead2 = findLeader(j, leads);
                    if (lead1 != lead2) {
                        leads[lead1] = lead2;
                        groups--;
                    }
                }
        return groups;
    }

    int findLeader(int i, vector<int>& leads) {
        return leads[i] == i ? i : findLeader(leads[i], leads);
    }
};
// @lc code=end

