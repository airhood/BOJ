#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <sstream>

using namespace std;

string horizontal_add(string a, string b) {
    istringstream streamA(a);
    istringstream streamB(b);
    string lineA, lineB, result;

    while (getline(streamA, lineA) && getline(streamB, lineB)) {
        result += lineA + lineB + '\n';
    }

    if (!result.empty()) result.pop_back();

    return result;
}

string empty_square(int n) {
    string result;
    for (int i = 0; i < n; ++i) {
        result += string(n, ' ');
        if (i != n - 1) result += '\n';
    }
    return result;
}

int main() {
    int N;
    cin >> N;

    int cnt = 0;
    while (N > 0) {
        N /= 3;
        cnt++;
    }

    vector<string> dp(cnt);
    dp[0] = "*";

    for (int i = 1; i < cnt; i++) {
        string p = dp[i-1];
        string head = horizontal_add(horizontal_add(p, p), p);
        string body = horizontal_add(horizontal_add(p, empty_square(pow(3, i - 1))), p);
        dp[i] = head + "\n" + body + "\n" + head;
    }

    cout << dp.back();
}