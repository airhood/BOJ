#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

constexpr long long INF = (long long)(1e18) + 7;

long long SafeAdd(long long a, long long b) {
    a += b;
    if (a > INF) a = INF;
    return a;
}

struct LisSegmentTree {
    int size;
    vector<pair<int, long long>> tree;

    LisSegmentTree(int N) {
        size = 1;
        while (size < N)
            size <<= 1;
        tree.assign(2 * size, { 0, 0 });
    }

    pair<int, long long> add_size(const pair<int, long long>& a, const pair<int, long long>& b) {
        if (a.first > b.first)
            return a;
        if (b.first > a.first)
            return b;
        return { a.first, SafeAdd(a.second, b.second) };
    }

    pair<int, long long> query(int start, int end, int left, int right, int i = 1) {
        if (end < left || start > right) return { 0, 0 };
        if (left <= start && end <= right) return tree[i];
        int mid = (start + end) / 2;
        return add_size(query(start, mid, left, right, i * 2), query(mid + 1, end, left, right, i * 2 + 1));
    }

    pair<int, long long> update(int start, int end, int idx, pair<int, long long> val, int i = 1) {
        if (idx < start || idx > end) return tree[i];
        if (start == end) {
            tree[i] = add_size(tree[i], val);
            return tree[i];
        }
        int mid = (start + end) / 2;
        tree[i] = add_size(update(start, mid, idx, val, i * 2), update(mid + 1, end, idx, val, i * 2 + 1));
        return tree[i];
    }

    pair<int, long long> getRoot() {
        return tree[1];
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N, K;
    cin >> N >> K;
    vector<int> arr(N + 1);
    for (int i = 1; i <= N; i++) cin >> arr[i];

    LisSegmentTree segment_tree(N);

    vector<int> lis(N + 1, 0);
    vector<long long> dp(N + 1, 0);

    for (int i = N; i > 0; i--) {
        int val = arr[i];
        pair<int, long long> result = segment_tree.query(1, N, val, N);
        if (result.first == 0) result.second = 1;
        lis[i] = result.first + 1;
        dp[i] = (result.second == 0 ? 1 : result.second);
        segment_tree.update(1, N, val, pair<int, long long>{ lis[i], dp[i] });
    }

    int max_length = segment_tree.getRoot().first;

    vector<vector<int>> track(max_length + 1, vector<int>(0, 0));
    for (int i = 1; i <= N; i++) track[lis[i]].push_back(i);
    for (int i = 1; i <= max_length; i++) {
        auto cmp = [&](int a, int b) {
            return arr[a] < arr[b];
        };
        sort(track[i].begin(), track[i].end(), cmp);
    }

    long long sum = 0;
    for (int i = 0; i < track[max_length].size(); i++) {
        sum = SafeAdd(sum, dp[track[max_length][i]]);
    }
    if (sum < K) {
        cout << -1 << endl;
        return 0;
    }

    int prev = 0;
    for (int i = max_length; i > 0; i--) {
        for (int j = 0; j < track[i].size(); j++) {
            if (prev < track[i][j] && arr[prev] < arr[track[i][j]]) {
                if (K > dp[track[i][j]]) K -= dp[track[i][j]];
                else {
                    prev = track[i][j];
                    cout << arr[prev] << ' ';
                    break;
                }
            }
        }
    }

    cout << endl;

    return 0;
}