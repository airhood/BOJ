#include <iostream>
#include <vector>

using namespace std;

int min(int a, int b) {
    if (a >= b) return b;
    else return a;
}

int main() {
    int N, S;
    cin >> N >> S;

    vector<int> list(N);
    for (int i = 0; i < N; i++) {
        cin >> list[i];
    }

    int l = 0;
    int r = 0;
    int sum = list[0];
    bool b = false;
    int answer;
    while(l <= r && r < N) {
        if (sum >= S) {
            if (b) {
                answer = min(answer, r - l + 1);
            }
            else {
                answer = r - l + 1;
            }
            b = true;
            sum -= list[l];
            l++;
        }
        else {
            r++;
            sum += list[r];
        }
    }

    if (!b) {
        cout << 0;
        return 0;
    }

    cout << answer;
}