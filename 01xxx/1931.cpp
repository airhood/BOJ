#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define ITERATE(var, init, N) for (int var = init; var < N; var++)

int main() {
    int N;
    cin >> N;

    vector<pair<int, int>> list;

    ITERATE(i, 0, N) {
        int tmp1, tmp2;
        cin >> tmp1 >> tmp2;
        list.push_back(make_pair(tmp1, tmp2));
    }

    sort(list.begin(), list.end(), [](auto& element1, auto& element2) -> bool {
        if (element1.second == element2.second) {
            return element1.first < element2.first;
        }
        return element1.second < element2.second;
    });

    int num = 0;

    int last_time = 0;
    ITERATE(i, 0, N) {
        if (list[i].first >= last_time) {
            num++;
            last_time = list[i].second;
        }
    }

    cout << num;
}