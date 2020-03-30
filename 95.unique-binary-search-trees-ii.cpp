/*
 * @lc app=leetcode id=95 lang=cpp
 *
 * [95] Unique Binary Search Trees II
 */
#include <vector>
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
    vector<TreeNode*> generateTrees(int n) {
        if (n<1)
            return vector<TreeNode *>();
        return generateTrees(1, n);
    }

    vector<TreeNode*> generateTrees(int s, int e) {
        vector<TreeNode *> res;
        if (s > e) {
            res.push_back(NULL);
            return res;
        }

        for (int i = s; i <= e; ++i) {
            vector<TreeNode *> leftSubtrees = generateTrees(s, i - 1);
            vector<TreeNode *> rightSubtrees = generateTrees(i + 1, e);
            for (TreeNode* left: leftSubtrees) {
                for (TreeNode* right: rightSubtrees) {
                    TreeNode *root = new TreeNode(i);
                    root->left = left;
                    root->right = right;
                    res.push_back(root);
                }
            }
        }
        return res;
    }

};
// @lc code=end

