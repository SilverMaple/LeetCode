/*
 * @lc app=leetcode id=347 lang=cpp
 *
 * [347] Top K Frequent Elements
 */
#include <vector>
#include <unordered_map>
#include <queue>
using namespace std;

// @lc code=start
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> map;
        for (int num: nums) {
            map[num]++;
        }

        vector<int> res;
        priority_queue<pair<int, int>> pq;
        for (auto it = map.begin(); it != map.end(); it++) {
            pq.push(make_pair(it->second, it->first));
            if (pq.size() > (int)map.size()-k) {
                res.push_back(pq.top().second);
                pq.pop();
            }
        }
        return res;
    }
};
// @lc code=end

