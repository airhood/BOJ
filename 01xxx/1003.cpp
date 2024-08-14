#include <iostream>
#include <vector>

using namespace std;

int main() {
    int test_cases;
    cin >> test_cases;
    vector<pair<int, int>> list(41);
    list[0] = make_pair(1, 0);
    list[1] = make_pair(0, 1);
    
    for (int i = 2; i < 41; i++) {
        list[i].first = list[i-1].first + list[i-2].first;
        list[i].second = list[i-1].second + list[i-2].second;
    }

    for (int i = 0; i < test_cases; i++) {
        int N;
        cin >> N;
        cout << list[N].first << " " << list[N].second << endl;
    }
}

/*
N: zero one
0: 1 0
1: 0 1
2: 1 1
3: 1 2
4: 2 3
...
*/