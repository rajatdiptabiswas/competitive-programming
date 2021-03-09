#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
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


uint32 dimension2to1(int i, int j, int n, int m) {
    return (uint32)(i - 1) * m + (j - 1);
}

int main(int argc, char const *argv[]) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, m, k, t;
    cin >> n >> m >> k >> t;

    vector<uint32> wastes(k);
    REP(x, k) {
        int i, j;
        cin >> i >> j;
        
        wastes[x] = dimension2to1(i, j, n, m);
    }
    sort(all(wastes));
    
    vector<string> fruits = {"Carrots", "Kiwis", "Grapes"};

    REP(x, t) {
        int i, j;
        cin >> i >> j;
        
        uint32 dimension1Index = dimension2to1(i, j, n, m);
        int wastesIndex = lower_bound(all(wastes), dimension1Index) - wastes.begin();
        
        if (wastes[wastesIndex] == dimension1Index) {
            cout << "Waste" << endl;
        } else {
            cout << fruits[(dimension1Index - wastesIndex) % 3] << endl;
        }
    }

    return 0;
}