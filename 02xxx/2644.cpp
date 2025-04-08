#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    int n, a, b, m;
    cin >> n;
    cin >> a >> b;
    cin >> m;

    vector<vector<int>> list(n + 1);

    for (int i = 0; i < m; i++) {
        int x, y;
        cin >> x >> y;

        list[x].push_back(y);
        list[y].push_back(x);
    }

    vector<bool> visited(n + 1);
    queue<pair<int, int>> queue;
    queue.push(make_pair(a, 0));

    while (!queue.empty()) {
        int pos = queue.front().first;
        int dist = queue.front().second;
        queue.pop();

        if (pos == b) {
            cout << dist;
            return 0;
        }

        for (auto& next : list[pos]) {
            if (!visited[next]) {
                visited[next] = true;
                queue.push(make_pair(next, dist + 1));
            }
        }
    }

    cout << -1;
}