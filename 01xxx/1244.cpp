#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> state(N+1);

    for (int i = 1; i <= N; i++) cin >> state[i];

    int S;
    cin >> S;

    for (int i = 0; i < S; i++) {
        int gender, num;
        cin >> gender >> num;

        if (gender == 1) {
            for (int j = 1; j <= N; j++) {
                if (j % num == 0) state[j] = !state[j];
            }
        }
        else if (gender == 2) {
            state[num] = !state[num];
            for (int j = 1; (state[num + j] == state[num - j]) && ((num + j <= N) && (num - j > 0)); j++) {
                state[num + j] = !state[num + j];
                state[num - j] = !state[num - j];
            }
        }
    }

    for (int i = 1; i <= N; i++) {
        cout << state[i] << " ";
        if (i % 20 == 0) cout << endl;
    }
}