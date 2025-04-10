#include <iostream>
#include <math.h>
#include <vector>
#include <algorithm>

using namespace std;

const long double error_range = 0.0001;

int main() {
    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        long double a, b, c, d;
        cin >> a >> b >> c >> d;

        auto f = [&](long double x) {
            return a * pow(x, 3) + b * pow(x, 2) + c * x + d;
        };

        long double alpha;
        for (int x = -1000000; x <= 1000000; x++) {
            if (f(x) == 0) {
                alpha = x;
                break;
            }
        }

        vector<long double> roots;
        long double p = a * alpha + b;
        long double q = p * alpha + c;

        long double D = (p * p) - 4 * a * q;

        if (D > 0) {
            long double beta = ((long double) -p + sqrt(D)) / (2 * a);
            long double gamma = ((long double) -p - sqrt(D)) / (2 * a);
            roots.push_back((long double)alpha);
            roots.push_back(beta);
            roots.push_back(gamma);
        }
        else if (D == 0) {
            long double beta = (long double) -p / (2 * a);
            roots.push_back((long double)alpha);
            roots.push_back(beta);
        }
        else {
            roots.push_back((long double)alpha);
        }

        sort(roots.begin(), roots.end());

        vector<long double> answer;
        answer.push_back(roots.front());
        for (int i = 1; i < roots.size(); i++) {
            if (roots[i] - answer.back() > error_range) answer.push_back(roots[i]);
        }

        cout.precision(9);
        for (int i = 0; i < answer.size(); i++) {
            cout << fixed << answer[i] << " ";
        }
        cout << endl;
    }
}