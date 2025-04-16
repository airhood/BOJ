#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<int> list(M);
    for (int i = 0; i < M; i++) cin >> list[i];

    vector<int> dp(50);
    dp[0] = 1;
    dp[1] = 1;
    dp[2] = 2;
    for (int i = 3; i <= N; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    
    long long count;
    if (M == 0) {
        count = dp[N];
    }
    else {
        count = dp[list[0] - 1];
        for (int i = 1; i < M; i++) {
            count *= dp[list[i] - list[i - 1] - 1];
        }
        count *= dp[N - list.back()];
    }

    cout << count;
}