/*
 * @lc app=leetcode id=215 lang=cpp
 *
 * [215] Kth Largest Element in an Array
 */
#include <iostream>
#include <vector>
using namespace std;

// @lc code=start
class Solution
{
public:
    int findKthLargest(vector<int> &nums, int k)
    {
        k = nums.size() - k;
        int l = 0, h = nums.size() - 1;
        while (l < h)
        {
            int j = partition1(nums, l, h);
            if (j == k)
                break;
            else if (j < k)
                l = j + 1;
            else
                h = j - 1;
        }
        return nums[k];
    }

    int partition(vector<int> &nums, int l, int h)
    {
        int pivot = nums[l];
        int i = l, j = h + 1;
        while (i < j)
        {
            while (i < h && nums[++i] < pivot)
                ;
            while (j > l && nums[--j] > pivot)
                ;
            if (i >= j)
                break;
            swap(nums[i], nums[j]);
        }
        swap(nums[j], nums[l]);
        return j;
    }

    int partition1(vector<int> &nums, int l, int h)
    {
        int pivot = nums[h];
        int i = l - 1;
        for (int j = l; j < h; j++)
        {
            if (nums[j] < pivot)
            {
                swap(nums[++i], nums[j]);
            }
        }
        swap(nums[++i], nums[h]);
        return i;
    }
};
// @lc code=end
int main()
{
    vector<int> a = {3, 2, 1, 5, 6, 4};
    int r = Solution().findKthLargest(a, 2);
    cout << r << endl;
}
