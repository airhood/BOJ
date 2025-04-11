#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<string> list(N);
    for (int i = 0; i < N; i++) cin >> list[i];

    auto cmp = [](string a, string b) -> bool {
        return (a + b) > (b + a);
    };

    sort(list.begin(), list.end(), cmp);

    if (list[0] == "0") {
        cout << "0";
        return 0;
    }

    for (int i = 0; i < N; i++) cout << list[i];
}