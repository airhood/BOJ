#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

enum Type {
    START = 1,
    END = -1,
};

struct Line {
    int x;
    int y1, y2;
    Type type;

    Line(int x, int y1, int y2, Type type) {
        this->x = x;
        this->y1 = y1;
        this->y2 = y2;
        this->type = type;
    }

    bool operator < (const Line& line) const {
        if (x == line.x) return type < line.type;
        return x < line.x;
    }    
};

int main() {
    int N;

    cin >> N;

    vector<Line> list;
    for (int i = 0; i < N; i++) {
        double a, b, c, d;
        cin >> a >> b >> c >> d;
        a *= 10;
        b *= 10;
        c *= 10;
        d *= 10;
        list.push_back(Line((int)a, (int)b, (int)(b + d), Type::START));
        list.push_back(Line((int)(a + c), (int)b, (int)(b + d), Type::END));
    }

    sort(list.begin(), list.end());

    vector<int> check(20001);
    for (int i = 0; i < 20001; i++) check[i] = 0;

    long long answer = 0;
    int last_x = 0;
    for (auto& line : list) {
        int current_line = 0;
        for (int i = 0; i < check.size(); i++) {
            if (check[i] > 0) current_line++;
        }
        answer += current_line * (line.x - last_x);
        for (int i = line.y1 + 1; i <= line.y2; i++) {
            if (line.type == Type::START) check[i]++;
            else if (line.type == Type::END) check[i]--;
        }
        last_x = line.x;
    }
    if (answer % 100 == 0) cout << answer / 100;
    else {
        cout.precision(2);
        cout << fixed << answer / 100.0;
    }
}