#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define ITERATE(var, N) for (int var = 0; var < N; var++)

int main() {
    int N;
    cin >> N;

    vector<pair<int, int>> list;

    ITERATE(i, N) {
        int tmp1, tmp2;
        cin >> tmp1 >> tmp2;
        list.push_back(make_pair(tmp1, tmp2));
    }

    sort(list.begin(), list.end(), [](auto element1, auto element2) {
        return element1.first < element2.first;
    });

    vector<int> dp(N);
    ITERATE(i, N) {
        ITERATE(j, i) {
            if ((list[j].second < list[i].second) && (dp[i] < dp[j])) {
                dp[i] = dp[j];
            }
        }
        dp[i]++;
    }

    int max = 0;
    ITERATE(i, N) {
        if (dp[i] > max) {
            max = dp[i];
        }
    }

    cout << N - max;
}