/*
 * @lc app=leetcode id=69 lang=cpp
 *
 * [69] Sqrt(x)
 */

// @lc code=start
class Solution {
public:
    int mySqrt(int x) {
        if (x<=1)
            return x;

        int l = 1, h = x;
        while (l<=h) {
            int mid = l + (h - l) / 2;
            int sqrt = x / mid;
            if (sqrt == mid)
                return mid;
            else if (mid > sqrt)
                h = mid - 1;
            else
                l = mid + 1;
        }
        return h;
    }
};
// @lc code=end

