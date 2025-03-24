#include <iostream>
#include <vector>
#include <string>
#include <functional>
#include <algorithm>

using namespace std;

vector<vector<int>> movements = { { 0, -1 }, { -1, 0 }, { 0, 1 }, { 1, 0 } };

int main() {
    int N;
    cin >> N;

    vector<vector<int>> map;
    vector<vector<int>> visit_map;
    for (int i = 0; i < N; i++) {
        vector<int> element;
        vector<int> visit_map_element;

        string line_state;
        cin >> line_state;

        for (auto& state : line_state) {
            element.push_back(state - '0');
            visit_map_element.push_back(0);
        }

        map.push_back(element);
        visit_map.push_back(visit_map_element);
    }

    function<int(int, int)> find; // 재귀를 위해 먼저 선언 후 람다 정의
    find = [&map, &visit_map, &N, &find](int x, int y) -> int {
        int count = 0;
        // 위쪽 왼쪽 아래쪽 오른족 순서대로 이동을 계산
        for (auto& movement : movements) {
            // 이동 후 위치
            int move_x = x + movement[0];
            int move_y = y + movement[1];

            // 잘못된 범위
            if (move_x >= N || move_x < 0 || move_y >= N || move_y < 0) continue;
            
            // 방문하지 않은 곳이면서 집이 존재하는지
            if ((visit_map[move_x][move_y] == 0) && (map[move_x][move_y] == 1)) {
                count++;
                visit_map[move_x][move_y] = 1;
                int sub_count = find(move_x, move_y); // 움직인 위치를 기준으로 다시 계산 (재귀적으로 탐색)
                count += sub_count;
            }
        }
        
        return count;
    };

    vector<int> house_counts;

    for (int x = 0; x < N; x++) {
        for (int y = 0; y < N; y++) {
            if ((visit_map[x][y] == 0) && (map[x][y] == 1)) {
                visit_map[x][y] = 1;
                int count = find(x, y) + 1;
                house_counts.push_back(count);
            }
        }
    }

    sort(house_counts.begin(), house_counts.end());

    cout << house_counts.size() << endl;

    for (auto& count : house_counts) {
        cout << count << endl;
    }
}