#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int lower_bound(const vector<pair<int, int>> arr, int x) {
    int left = 0; 
    int right = arr.size();
    while (left < right) {
        int mid = (left + right) / 2;
        if (arr[mid].second < x) {
            left = mid + 1;
        }
        else {
            right = mid;
        }
    }
    return left;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    vector<pair<int, int>> list(N);
    for (int i = 0; i < N; i++) {
        cin >> list[i].first >> list[i].second;
    }

    sort(list.begin(), list.end());

    vector<pair<int, int>> tail;
    vector<int> tail_idx;
    vector<int> prev_idx(N, -1);

    for (int i = 0; i < N; i++) {
        int idx = lower_bound(tail, list[i].second);

        if (idx == tail.size()) {
            tail.push_back(list[i]);
            tail_idx.push_back(i);
        }
        else {
            tail[idx] = list[i];
            tail_idx[idx] = i;
        }

        if (idx != 0) {
            prev_idx[i] = tail_idx[idx - 1];
        }
    }

    vector<int> lis;

    int track = tail_idx.back();
    while (track != -1) {
        lis.push_back(list[track].first);
        track = prev_idx[track];
    }

    reverse(lis.begin(), lis.end());

    vector<int> ans;
    int lis_idx = 0;
    for (int i = 0; i < N; i++) {
        if (lis_idx < lis.size() && list[i].first == lis[lis_idx]) {
            lis_idx++;
        }
        else {
            ans.push_back(list[i].first);
        }
    }

    cout << ans.size() << endl;
    for (auto& element : ans) {
        cout << element << '\n';
    }
}