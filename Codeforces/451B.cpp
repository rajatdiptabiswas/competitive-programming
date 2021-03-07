#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <iomanip>
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


int main(int argc, char const *argv[]) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // input
    int n;
    cin >> n;
    vector<int> a(n);
    REP(i, n) {
        cin >> a[i];
    }

    // 0-indexed
    int start = 0, end = 0;

    // find start index
    REP(i, n - 1) {
        if (a[i] > a[i + 1]) {
            start = i;
            break;
        }
    }

    // find end index
    RREP(i, n - 2) {
        if (a[i] > a[i + 1]) {
            end = i + 1;
            break;
        }
    }

    // reverse [start, end]
    reverse(a.begin() + start, a.begin() + end + 1);

    // check if sorted
    bool isSorted = true;
    REP(i, n - 1) {
        if (a[i] > a[i + 1]) {
            isSorted = false;
            break;
        }
    }

    if (isSorted) {
        cout << "yes" << endl;
        cout << start + 1 << " " << end + 1 << endl;
    } else {
        cout << "no" << endl;
    }

    return 0;
}