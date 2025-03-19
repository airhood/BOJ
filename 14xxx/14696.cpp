#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

#define ITERATE(var, init, N) for (int var = init; var < N; var++)

int main() {
    int N;
    cin >> N;

    vector<pair<vector<int>, vector<int>>> list(N);

    ITERATE(i, 0, N) {
        list[i] = make_pair(vector<int>(4), vector<int>(4));
        ITERATE(j, 0, 4) {
            list[i].first[j] = 0;
            list[i].second[j] = 0;
        }
    }

    ITERATE(i, 0, N) {
        int k1;
        cin >> k1;
        ITERATE(j, 0, k1) {
            int tmp;
            cin >> tmp;

            list[i].first[tmp - 1]++;
        }

        int k2;
        cin >> k2;
        ITERATE(j, 0, k2) {
            int tmp;
            cin >> tmp;

            list[i].second[tmp - 1]++;
        }
    }

    ITERATE(i, 0, N) {
        function<void(int)> checkResult;
        checkResult = [&list, &i, &checkResult](int card) {
            if (list[i].first[card] > list[i].second[card]) {
                cout << "A" << endl;
            }
            else if (list[i].first[card] < list[i].second[card]) {
                cout << "B" << endl;
            }
            else {
                if (card == 0) {
                    cout << "D" << endl;
                    return;
                }
                checkResult(card - 1);
            }
        };

        checkResult(3);
    }
}