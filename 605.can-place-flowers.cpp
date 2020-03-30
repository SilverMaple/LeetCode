/*
 * @lc app=leetcode id=605 lang=cpp
 *
 * [605] Can Place Flowers
 */
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int length = flowerbed.size();
        int count = 0;
        for (int i = 0; i < length & count < n; i++) {
            if (flowerbed[i] == 1)
                continue;
            int pre = i == 0 ? 0 : flowerbed[i - 1];
            int next = i == length - 1 ? 0 : flowerbed[i + 1];
            if (pre == 0 && next==0) {
                count++;
                flowerbed[i] = 1;
            }
        }
        return count >= n;
    }
};
// @lc code=end

