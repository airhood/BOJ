#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<int> list(30);
    for (int i = 0; i < 28; i++) {
        int n;
        cin >> n;
        list[n - 1] = 1;
    }

    vector<int> answer;

    for (int i = 0; i < 30; i++) {
        if (list[i] == 0) answer.push_back(i + 1);
    }

    sort(answer.begin(), answer.end());
    
    cout << answer[0] << endl << answer[1];
}