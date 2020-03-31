/*
 * @lc app=leetcode id=257 lang=cpp
 *
 * [257] Binary Tree Paths
 */

#include <vector>
#include <string>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> res;
        vector<int> path;
        if (root == NULL)
            return res;
        dfs(root, res, path);
        return res;
    }

    void dfs(TreeNode* node, vector<string>& res, vector<int>& path) {
        if (node == NULL)
            return;
        path.push_back(node->val);
        if (isLeaf(node))
            res.push_back(buildPath(path));
        else {
            dfs(node->left, res, path);
            dfs(node->right, res, path);
        }
        path.pop_back();
    }

    bool isLeaf(TreeNode* node) {
        return node->left == NULL && node->right == NULL;
    }

    string buildPath(vector<int>& path) {
        string pathString = "";
        for (int i = 0; i < path.size(); i++) {
            pathString += to_string(path[i]);
            if (i!=path.size()-1)
                pathString += "->";
        }
        return pathString;
    }
};
// @lc code=end

