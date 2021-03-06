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

    int n, m;
    char presidentColor;
    cin >> n >> m >> presidentColor;
    vector<vector<char>> room(n, vector<char>(m));
    REP(i, n) {
        REP(j, m) {
            cin >> room[i][j];
        }
    }

    set<char> deputyColors;
    vector<int> directionY = {1, 0, -1, 0};
    vector<int> directionX = {0, 1, 0, -1};

    REP(i, n) {
        REP(j, m) {
            if (room[i][j] == presidentColor) {
                REP(d, 4) {
                    int nextY = i + directionY[d];
                    int nextX = j + directionX[d];
                    if (0 <= nextY && nextY < n && 
                        0 <= nextX && nextX < m) {
                        if (room[nextY][nextX] != '.' &&
                            room[nextY][nextX] != presidentColor) {
                            deputyColors.insert(room[nextY][nextX]);
                        }
                    }
                }
            }
        }
    }

    cout << deputyColors.size() << endl;

    return 0;
}