#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<long long> list(N);
    for (int i = 0; i < N; i++) cin >> list[i];

    long long count = 1;
    long long max = 1;
    for (int i = 1; i < N; i++) {
        if (list[i - 1] <= list[i]) count++;
        else {
            if (count > max) max = count;
            count = 1;
        }
    }
    if (count > max) max = count;
    count = 1;
    for (int i = 1; i < N; i++) {
        if (list[i - 1] >= list[i]) count++;
        else {
            if (count > max) max = count;
            count = 1;
        }
    }
    if (count > max) max = count;
    cout << max;
}