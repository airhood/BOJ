#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

// 그리디
int main() {
    int N;
    cin >> N;

    deque<int> list(N);

    for (int i = 0; i < N; i++) {
        cin >> list[i];
    }

    sort(list.begin(), list.end());

    vector<int> answer;
    while (!list.empty()) {
        if (list.back() - list.front() <= 1) {
            while (!list.empty()) {
                answer.push_back(list.back());
                list.pop_back();
            }
        }
        else {
            if (answer.empty()) {
                answer.push_back(list.front());
                list.pop_front();
            }
            else {
                if (answer.back() == list.front()) {
                    answer.push_back(list.front());
                    list.pop_front();
                } else if (answer.back() + 1 == list.front()) {
                    int i;
                    for (i = 0; list[i] <= answer.back() + 1; i++);
                    int count = 0;
                    answer.push_back(list[i]);
                    list.erase(list.begin() + i);
                    answer.push_back(list.front());
                    list.pop_front();
                }
                else {
                    answer.push_back(list.front());
                    list.pop_front();
                }
            }
        }
    }

    for (int i = 0; i < N; i++) {
        cout << answer[i] << " ";   
    }
}