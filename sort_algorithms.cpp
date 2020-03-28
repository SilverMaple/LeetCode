#include <iostream>
#include <vector>
#include <string>
using namespace std;

class SortAlgorithms {
    public:
        vector<int> nums;

    public:
        SortAlgorithms()
        {
            generateNumbers();
        }

        void generateNumbers(int size=10) {
            nums.clear();
            for (int i = 0; i < size; i++)
            {
                nums.push_back(rand() % size);
            }
        }
        
        void swap(vector<int>& nums, int a, int b) {
            int temp = nums[a];
            nums[a] = nums[b];
            nums[b] = temp;
        }

        void printVector() {
            for (int i = 0; i < nums.size(); i++) {
                cout << nums[i] << " ";
            }
            cout << endl;
        }

        // 冒泡排序 O(n**2)
        void bubbleSort(vector<int>& nums) {
            bool isSorted = false;
            for (int i = nums.size() - 1; i > 0; i--)
            {
                if (isSorted)
                    break;
                isSorted = true;
                for (int j = 0; j < i; j++) {
                    if (nums[j+1] < nums[j]) {
                        swap(nums, j, j + 1);
                        isSorted = false;
                    }
                }
            }
        }

        // 选择排序 O(n**2)
        void selectionSort(vector<int>& nums) {
            int minIndex = -1;
            for (int i = 0; i < nums.size(); i++)
            {
                minIndex = i;
                for (int j = i+1; j < nums.size(); j++) {
                    if (nums[j] < nums[minIndex]) {
                        minIndex = j;
                    }
                }
                swap(nums, i, minIndex);
            }
        }
};

int main(void) {
    SortAlgorithms s;
    string splitString = "--------------------------------------------------";
    s.generateNumbers();
    s.printVector();
    s.bubbleSort(s.nums);
    s.printVector();
}