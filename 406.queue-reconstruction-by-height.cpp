/*
 * @lc app=leetcode id=406 lang=cpp
 *
 * [406] Queue Reconstruction by Height
 */
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

// @lc code=start
class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end(), compare);
        vector<vector<int>> res;
        for (vector<int>& p : people) {
            res.insert(res.begin() + p[1], p);
        }
        return res;

        // vector<int> indices;
        // int index;
        // for (int i = 0; i < people.size(); i++)
        //     indices.push_back(i);
        // for (int i = 0; i < people.size(); i++) {
        //     res[indices[people[i][1]]] = people[i];
        //     indices.erase(indices.begin() + people[i][1]);
        // }
        // return res;
    }

    static bool compare(const vector<int>& a, const vector<int>& b) {
        return (a[0] == b[0]) ? a[1] > b[1] : a[0] < b[0];
    }
};
// @lc code=end
