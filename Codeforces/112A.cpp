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


int main(int argc, char const *argv[]) {
    FASTIO;

    string str1, str2;
    cin >> str1;
    cin >> str2;

    int weight = 0;
    REP(i, str1.size()) {
        if (tolower(str1[i]) < tolower(str2[i])) {
            weight--;
            break;
        } else if (tolower(str1[i]) > tolower(str2[i])) {
            weight++;
            break;
        } else if (tolower(str1[i]) == tolower(str2[i])) {
            continue;
        }
    }

    cout << weight << endl;

    return 0;
}