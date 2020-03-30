/*
 * @lc app=leetcode id=127 lang=cpp
 *
 * [127] Word Ladder
 */
#include <vector>
#include <queue>
#include <string>
#include <unordered_set>
using namespace std;

// @lc code=start
class Solution {
public:
    // one-end
    int ladderLength1(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> dict(wordList.begin(), wordList.end());
        queue<string> todo;      // 维护bfs队列
        todo.push(beginWord);    // 搜索起点
        int ladder = 1;          // 搜索深度
        while (!todo.empty()) {  // 队列不为空则继续搜索
            int n = todo.size(); // 当前层次宽度
            for (int i = 0; i < n; i++) {    // 广度遍历
                string word = todo.front();
                todo.pop();
                if (word == endWord)         // 遍历结束条件
                    return ladder;
                dict.erase(word);
                for (int j = 0; j < word.size(); j++) {
                    char c = word[j];
                    for (int k = 0; k < 26; k++) {
                        word[j] = 'a' + k;
                        if (dict.find(word)!=dict.end()) {
                            todo.push(word);
                        }
                    }
                    word[j] = c;
                }
            }
            ladder++;
        }
        return 0;
    }

    // two-end
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> dict(wordList.begin(), wordList.end()), head, tail, *phead, *ptail;
        if (dict.find(endWord) == dict.end()) {
            return 0;
        }
        head.insert(beginWord);
        tail.insert(endWord);
        int ladder = 2;
        while (!head.empty() && !tail.empty()) {
            if (head.size() < tail.size()) {
                phead = &head;
                ptail = &tail;
            } else {
                phead = &tail;
                ptail = &head;
            }
            unordered_set<string> temp;
            for (auto it = phead -> begin(); it != phead -> end(); it++) {    
                string word = *it;
                for (int i = 0; i < word.size(); i++) {
                    char t = word[i];
                    for (int j = 0; j < 26; j++) {
                        word[i] = 'a' + j;
                        if (ptail -> find(word) != ptail -> end()) {
                            return ladder;
                        }
                        if (dict.find(word) != dict.end()) {
                            temp.insert(word);
                            dict.erase(word);
                        }
                    }
                    word[i] = t;
                }
            }
            ladder++;
            phead -> swap(temp);
        }
        return 0;
    }
};
// @lc code=end

