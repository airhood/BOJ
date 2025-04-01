#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> list(N);
    for (int i = 0; i < N; i++) {
        cin >> list[i];
    }

    sort(list.begin(), list.end());

    int result = 0;

    for (int i = 0; i < N; i++) {
        int target = list[i];
        int l = 0;
        int r = N - 1;

        while (l < r) {
            int sum = list[l] + list[r];
            if (sum == target) {
                if (l != i && r != i) {
                    result++;
                    break;
                }
                else if (l == i) l++;
                else if (r == i) r--;
            }
            else if (sum < target) l++;
            else if (sum > target) r--;
        }
    }

    cout << result;
}