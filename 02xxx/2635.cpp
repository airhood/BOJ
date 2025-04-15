#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;


    vector<int> result;
    for (int i = 1; i <= N; i++) {
        vector<int> list;
        list.push_back(N);
        list.push_back(i);

        int j = 0;
        while (true) {
            if (list[j] - list[j + 1] < 0) break;
            list.push_back(list[j] - list[j + 1]);
            j++;
        }
        if (list.size() > result.size()) result = list;
    }

    cout << result.size() << endl;
    for (auto& element : result) cout << element << " ";
}