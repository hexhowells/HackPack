#include <bits/stdc++.h>
using namespace std;

// Types
using ll = long long;

// Constants
const int INF = 1e9;
const ll LINF = 1e18;
const int MOD = 1e9 + 7;

// Macros
#define all(v) (v).begin(), (v).end()
#define sza(x) ((int)(x).size())

// Debug macro
#ifndef ONLINE_JUDGE
#define debug(x) cerr << #x << " = " << x << '\n';
#else
#define debug(x)
#endif

void solve() {
    int n;
    cin >> n;
    vector<int> a(n);
    for(int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    sort(all(a));
    for(int x : a) {
        cout << x << " ";
    }
    cout << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
    return 0;

    int t = 1;
    cin >> t;
    while(t--) {
        solve();
    }
    
    return 0;
}