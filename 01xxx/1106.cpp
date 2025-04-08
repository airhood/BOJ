#include <iostream>
#include <vector>

#define LONG_MAX 2147483647

using namespace std;

long min(long a, long b) {
    if (a >= b) return b;
    else return a;
}

int main() {
    int C, N;
    cin >> C >> N;

    vector<pair<int, int>> list(N);
    for (int i = 0; i < N; i++) {
        cin >> list[i].first; // 비용
        cin >> list[i].second; // 고객 수
    }

    vector<long> dp(C + 101);
    for (int i = 0; i < C + 101; i++) {
        dp[i] = LONG_MAX;
    }

    dp[0] = 0;
    for (int i = 0; i < N; i++) {
        int cost = list[i].first;
        int amount = list[i].second;

        for (int j = amount; j <= C + 100; j++) {
            if (dp[j - amount] != LONG_MAX) {
                dp[j] = min(dp[j], dp[j - amount] + cost);
            }
        }
    }

    long min_cost = dp[C];
    for (int i = C + 1; i < C + 101; i++) {
        if (min_cost > dp[i]) min_cost = dp[i];
    }

    cout << min_cost;
}