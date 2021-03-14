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

    int x0, y0, x1, y1;
    cin >> x0 >> y0 >> x1 >> y1;
    
    int n;
    cin >> n;
    
    unordered_map<int, vector<pair<int, int>>> allowed; // row -> col ranges
    REP(i, n) {
        int r, a, b;
        cin >> r >> a >> b;
        allowed[r].PB({a, b});
    }

    vector<int> dirX = {0, 1, 1,  1,  0, -1, -1, -1};
    vector<int> dirY = {1, 1, 0, -1, -1, -1,  0,  1};

    pair<int, int> start = {x0, y0}, end = {x1, y1};

    bool pathPresent = false;
    int steps = 0;
    set<pair<int, int>> visited;

    queue<pair<int, int>> q;
    q.push(start);
    visited.insert(start);

    while (!q.empty()) {
        int size = q.size();

        while (size--) {
            pair<int, int> pos = q.front(); q.pop();

            if (pos == end) {
                pathPresent = true;
                break;
            }

            REP(i, 8) {
                pair<int, int> nextPos = {pos.F + dirX[i], pos.S + dirY[i]};

                if (!(1 <= nextPos.F && nextPos.F <= (int)1e9 &&
                    1 <= nextPos.S && nextPos.S <= (int)1e9)) {
                    continue;
                }

                if (CONTAINS(visited, nextPos)) {
                    continue;
                }

                for (pair<int, int> range : allowed[nextPos.F]) {
                    if (range.F <= nextPos.S && nextPos.S <= range.S) {
                        q.push(nextPos);
                        visited.insert(nextPos);
                        break;
                    }
                }
            }
        }

        if (pathPresent) {
            break;
        }

        steps++;
    }

    if (pathPresent) {
        cout << steps << endl;
    } else {
        cout << -1 << endl;
    }

    return 0;
}