/*
 * @lc app=leetcode id=121 lang=cpp
 *
 * [121] Best Time to Buy and Sell Stock
 */
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if (n==0)
            return 0;
        int soFarMin = prices[0];
        int maxBenefit = 0;
        for (int i = 0; i < n; i++) {
            if (soFarMin > prices[i])
                soFarMin = prices[i];
            else
                maxBenefit = max(maxBenefit, prices[i] - soFarMin);
        }
        return maxBenefit;
    }
};
// @lc code=end

