#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 1'000'000'007;

struct LisSegmentTree {
    int size;
    vector<pair<int, int>> tree;

    LisSegmentTree(int N) {
        size = 1;
        while (size < N)
            size <<= 1;
        tree.assign(2 * size, {0, 0});
    }

    pair<int, int> add_size(const pair<int, int> &a, const pair<int, int> &b) {
        if (a.first > b.first)
            return a;
        if (b.first > a.first)
            return b;
        return {a.first, (a.second + b.second) % MOD};
    }

    pair<int, int> query(int start, int end, int left, int right, int i = 1) {
        if (end < left || start > right) return {0, 0};
        if (left <= start && end <= right) return tree[i];
        int mid = (start + end) / 2;
        return add_size(query(start, mid, left, right, i * 2), query(mid + 1, end, left, right, i * 2 + 1));
    }

    pair<int, int> update(int start, int end, int idx, pair<int, int> val, int i = 1) {
        if (idx < start || idx > end) return tree[i];
        if (start == end) {
            tree[i] = add_size(tree[i], val);
            return tree[i];
        }
        int mid = (start + end) / 2;
        tree[i] = add_size(update(start, mid, idx, val, i * 2), update(mid + 1, end, idx, val, i * 2 + 1));
        return tree[i];
    }

    pair<int, int> getRoot() {
        return tree[1];
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<int> arr(N);
    for (int i = 0; i < N; i++) cin >> arr[i];

    vector<int> unique_arr = arr;
    sort(unique_arr.begin(), unique_arr.end());
    unique_arr.erase(unique(unique_arr.begin(), unique_arr.end()), unique_arr.end());
    vector<int> compressed;
    for (int i = 0; i < N; i++) {
        compressed.push_back((int)(lower_bound(unique_arr.begin(), unique_arr.end(), arr[i]) - unique_arr.begin()) + 1);
    }

    LisSegmentTree segment_tree(unique_arr.size());

    for (int i = 0; i < N; i++) {
        int val = compressed[i];
        pair<int, int> result = segment_tree.query(1, unique_arr.size(), 1, val - 1);
        if (result.first == 0) result.second = 1;
        segment_tree.update(1, unique_arr.size(), val, {result.first + 1, result.second});
    }

    pair<int, int> result = segment_tree.getRoot();
    cout << result.first << " " << result.second;

    return 0;
}
