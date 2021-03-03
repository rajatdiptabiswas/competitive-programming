#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <limits>
#include <string>
#include <iterator>
#include <vector>
#include <queue>
#include <deque>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#define MP make_pair
#define PB push_back
#define INF (int)1e9
#define EPS 1e-9
#define PI 3.1415926535897932384626433832795
#define MOD 1000000007
typedef long int int32;
typedef unsigned long int uint32;
typedef long long int int64;
typedef unsigned long long int uint64;
using namespace std;


int main(int argc, char const *argv[]) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int64 n, m, a, b;
    cin >> n >> m;
    vector<pair<int64, int64>> v(m);
    for (int i = 0; i < v.size(); i++) {
        cin >> a >> b;
        v[i] = {a, b};
    }

    sort(v.begin(), v.end(), [](const pair<int64, int64>& p1, const pair<int64, int64>& p2) {
        return p2.second < p1.second;
    });

    int64 total = 0;
    for (pair<uint64, uint64> p : v) {
        if (n <= 0) {
            break;
        }
        int64 boxes = p.first, matches = p.second;
        total += min(n, boxes) * matches;
        n -= boxes;
    }

    cout << total << endl;
    
    return 0;
}