#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<pair<long long, long long>> list(N+1);
    for (int i = 0; i < N; i++) {
        cin >> list[i].first >> list[i].second;
    }
    list[N] = list[0];

    long long result = 0;
    for (int i = 0; i < N; i++) {
        result += list[i].first * list[i + 1].second;
        result -= list[i].second * list[i + 1].first;
    }

    result = abs(result);

    long double answer = result / 2.0;
    cout << fixed;
    cout.precision(1);
    cout << answer;
}