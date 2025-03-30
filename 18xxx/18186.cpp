#include <iostream>
#include <vector>
#include <functional>
#include <algorithm>

using namespace std;

long long min(long long a, long long b) {
    if (a >= b) return b;
    else return a;
}

long long min(long long a, long long b, long long c) {
    return min(min(a, b), c);
}

int main() {
    long long N, B, C;
    cin >> N >> B >> C;

    vector<long long> list(N);
    for (long long i = 0; i < N; i++) {
        cin >> list[i];
    }
    list.push_back(0);
    list.push_back(0);

    long long money = 0;

    long long A_cost = B;
    long long B_cost = B + C;
    long long C_cost = B + 2 * C;
    
    if (B <= C) {
        for (long long i = 0; i < N; i++) {
            money += list[i] * B;
        }
        cout << money;
        return 0;
    }
    
    auto buy_A = [&list](long long i, long long k) {
        list[i] -= k;
    };

    auto buy_B = [&list](long long i, long long k) {
        list[i] -= k;
        list[i + 1] -= k;
    };

    auto buy_C = [&list](long long i, long long k) {
        list[i] -= k;
        list[i + 1] -= k;
        list[i + 2] -= k;
    };

    long long i = 0;
    while (i < N) {
        if ((list[i] != 0) && (list[i + 1] != 0) && (list[i + 2] != 0)) {
            if (list[i + 1] > list[i + 2]) {
                long long buy_amount = min(list[i + 1] - list[i + 2], list[i]);
                buy_B(i, buy_amount);
                money += buy_amount * B_cost;
            }
            else {
                long long buy_amount = min(list[i], list[i + 1], list[i + 2]);
                buy_C(i, buy_amount);
                money += buy_amount * C_cost;
            }
        }
        else if ((list[i] != 0) && (list[i + 1] != 0)) {
            long long buy_amount = min(list[i], list[i + 1]);
            buy_B(i, buy_amount);
            money += buy_amount * B_cost;
        }
        else if (list[i] != 0) {
            long long buy_amount = list[i];
            buy_A(i, buy_amount);   
            money += buy_amount * A_cost;
        }

        if (list[i] == 0) i++;
    }

    cout << money;
}