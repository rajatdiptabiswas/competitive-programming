#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <limits>
#include <string>
#include <sstream>
#include <iterator>
#include <vector>
#include <queue>
#include <deque>
#include <list>
#include <stack>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <bitset>
#define MEM(a, b) memset(a, (b), sizeof(a))
#define FOR(i, j, k, in) for (int i = j; i < k; i += in)
#define RFOR(i, j, k, in) for (int i = j; i >= k; i -= in)
#define REP(i, j) FOR(i, 0, j, 1)
#define RREP(i, j) RFOR(i, j, 0, 1)
#define all(cont) cont.begin(), cont.end()
#define rall(cont) cont.end(), cont.begin()
#define FOREACH(it, l) for (auto it = l.begin(); it != l.end(); it++)
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


int binarySearchIndex(int64 target, vector<pair<int64, int>>& array) {
    int l = 0, r = array.size() - 1, mid;
    while (l <= r) {
        mid = l + (r - l) / 2;
        if (target == array[mid].first) {
            return array[mid].second;
        } else if (target > array[mid].first) {
            l = mid + 1;
        } else if (target < array[mid].first) {
            r = mid - 1;
        }
    }
    return -1;
}

int main(int argc, char const *argv[]) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int64 vasya = 0, petya = 0;

    int64 n;
    cin >> n;
    vector<pair<int64, int>> array(n);
    REP(i, n) {
        int64 a;
        cin >> a;
        array[i] = {a, i};
    }
    int64 m;
    cin >> m;
    vector<int64> queries(m);
    REP(i, m) {
        cin >> queries[i];
    }

    sort(array.begin(), array.end());

    for (int64 q : queries) {
        int index = binarySearchIndex(q, array);
        vasya += index + 1;
        petya += array.size() - index;
    }

    cout << vasya << " " << petya << endl;
    
    return 0;
}