#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> arr(N);

    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    sort(arr.begin(), arr.end());

    int left = 0;
    int right = N - 1;

    int min = abs(arr[left] + arr[right]);
    int result_A = arr[left];
    int result_B = arr[right];


    while (left < right) {
        int current = arr[left] + arr[right];
        int current_abs = abs(current);
        if (min >= current_abs) {
            min = current_abs;
            result_A = arr[left];
            result_B = arr[right];
        }

        if (current < 0) left++;
        else if (current > 0) right--;
        else break;
    }   

    cout << result_A << " " << result_B;
}