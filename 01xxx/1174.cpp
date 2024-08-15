#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<long long> increasing_num;
    for (int a = 0; a <= 9; a++) {
        bool nil_a;
        if (a == 0) nil_a = true;
        else nil_a = false;
        for (int b = 0; ((b < a) || nil_a) && (b <= 9); b++) {
            bool nil_b;
            if (nil_a && (b == 0)) nil_b = true;
            else nil_b = false;
            for (int c = 0; ((c < b) || nil_b) && (c <= 9); c++) {
                bool nil_c;
                if (nil_b && (c == 0)) nil_c = true;
                else nil_c = false;
                for (int d = 0; ((d < c) || nil_c) && (d <= 9); d++) {
                    bool nil_d;
                    if (nil_c && (d == 0)) nil_d = true;
                    else nil_d = false;
                    for (int e = 0; ((e < d) || nil_d) && (e <= 9); e++) {
                        bool nil_e;
                        if (nil_d && (e == 0)) nil_e = true;
                        else nil_e = false;
                        for (int f = 0; ((f < e) || nil_e) && (f <= 9); f++) {
                            bool nil_f;
                            if (nil_e && (f == 0)) nil_f = true;
                            else nil_f = false;
                            for (int g = 0; ((g < f) || nil_f) && (g <= 9); g++) {
                                bool nil_g;
                                if (nil_f && (g == 0)) nil_g = true;
                                else nil_g = false;
                                for (int h = 0; ((h < g) || nil_g) && (h <= 9); h++) {
                                    bool nil_h;
                                    if (nil_g && (h == 0)) nil_h = true;
                                    else nil_h = false;
                                    for (int i = 0; ((i < h) || nil_h) && (i <= 9); i++) {
                                        bool nil_i;
                                        if (nil_h && (i == 0)) nil_i = true;
                                        else nil_i = false;
                                        for (int j = 0; ((j < i) || nil_i) && (j <= 9); j++) {
                                            long long num = (1000000000L * a) + (100000000 * b) + (10000000 * c) + (1000000 * d) + (100000 * e) + (10000 * f) + (1000 * g) + (100 * h) + (10 * i) + (1 * j);
                                            increasing_num.push_back(num);
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    if (increasing_num.size() < N) cout << "-1";
    else cout << increasing_num[N-1];
}