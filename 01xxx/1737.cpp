#include <iostream>

using namespace std;

constexpr long double PI = 3.14159265358979323846;
constexpr long long L = 1000000000000000000;

long long dp[1001][1001];

long long pb(int p, int q) {// p - q(pi)
    if (dp[p][q]) return dp[p][q];
    long double k = p - q * PI;
    if (0 <= k && k <= PI) return 1;
    else if (k < 0) return 0;

    dp[p][q] = (pb(p - 1, q) + pb(p, q + 1)) % L;
    return dp[p][q];
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    cout << pb(n, 0);
}