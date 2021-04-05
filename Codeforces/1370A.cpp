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
#define FASTIO ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define DEBUG(x) cout << #x << " = " << x << endl;
#define MEM(a, b) memset(a, (b), sizeof(a))
#define FOR(i, j, k, in) for (int i = j; i < k; i += in)
#define RFOR(i, j, k, in) for (int i = j; i >= k; i -= in)
#define REP(i, j) FOR(i, 0, j, 1)
#define RREP(i, j) RFOR(i, j, 0, 1)
#define ALL(container) container.begin(), container.end()
#define RALL(container) container.end(), container.begin()
#define FOREACH(it, l) for (auto it = l.begin(); it != l.end(); it++)
#define CONTAINS(container, x) (container.find(x) != container.end())
#define MAX(a, b) a = max(a, b) 
#define MIN(a, b) a = min(a, b)
#define F first
#define S second
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


// int gcd(int a, int b) {
//     if (b > a) {
//         return gcd(b, a);
//     }
//     if (b == 0) {
//         return a;
//     }
//     return gcd(b, a % b);
// }

int main(int argc, char const *argv[]) {
    FASTIO;

    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        // int maxGCD = 0;
        // for (int i = 1; i <= n - 1; i++) {
        //     for (int j = i + 1; j <= n; j++) {
        //         MAX(maxGCD, gcd(i, j));
        //     }
        // }

        int maxGCD = n / 2;

        cout << maxGCD << endl;
    }

    return 0;
}