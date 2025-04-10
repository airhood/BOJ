#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> map;
vector<vector<int>> visited;

vector<pair<int, int>> movement = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}}; // 북 동 남 서

int clean = 0;

int N, M;
int r, c, d;

void dfs() {
    for (int i = 0; i < 4; i++) {
        int next_d = (d + 3 - i) % 4;
        int next_r = r + movement[next_d].first;
        int next_c = c + movement[next_d].second;

        if (next_r < 0 || next_r >= N || next_c < 0 || next_c >= M) continue;
        if (map[next_r][next_c] == 1) continue;

        if (visited[next_r][next_c] == 0) {
            visited[next_r][next_c] = 1;
            r = next_r;
            c = next_c;
            d = next_d;
            clean++;
            dfs();
        }
    }

    int back_move = (d + 2) % 4;
    int back_r = r + movement[back_move].first;
    int back_c = c + movement[back_move].second;

    if (back_r < 0 || back_r >= N || back_c < 0 || back_c >= M) return;
    if (map[back_r][back_c] == 1) return;
    
    r = back_r;
    c = back_c;
    if (visited[r][c] == 0) {
        visited[r][c] = 1;
        clean++;
    }
    dfs();
}

int main() {
    cin >> N >> M;
    cin >> r >> c >> d;

    map = vector<vector<int>>(N);
    visited = vector<vector<int>>(N);

    for (int x = 0; x < N; x++) {
        map[x] = vector<int>(M);
        visited[x] = vector<int>(M);
        for (int y = 0; y < M; y++) {
            cin >> map[x][y];
            visited[x][y] = 0;
        }
    }

    visited[r][c] = 1;
    clean++;

    dfs();

    cout << clean;
}