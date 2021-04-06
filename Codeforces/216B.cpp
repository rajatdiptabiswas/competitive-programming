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


// -1 -> no cycle
int findCycleLength(int u, int parent, int length, vector<bool>& visited, vector<vector<int>>& graph) {
    visited[u] = true;
    for (int v : graph[u]) {
        if (v == parent) {
            continue;
        }
        if (visited[v]) {
            return length;
        }
        int cycleLength = findCycleLength(v, u, length + 1, visited, graph);
        if (cycleLength != -1) {
            return cycleLength;
        }
        // continue if no cycle found
    }
    return -1;
}

int main(int argc, char const *argv[]) {
    FASTIO;

    int n, m;
    cin >> n >> m;

    vector<vector<int>> graph(n + 1, vector<int>());

    REP(i, m) {
        int u, v;
        cin >> u >> v;

        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    vector<bool> visited(n + 1, false);

    int playersToRemove = 0;

    for (int i = 1; i <= n; i++) {
        if (visited[i]) {
            continue;
        }
        int cycleLength = findCycleLength(i, 0, 1, visited, graph);
        if (cycleLength != -1 && cycleLength % 2 == 1) {
            playersToRemove++;
        }
    }

    if ((n - playersToRemove) % 2 == 1) {
        playersToRemove++;
    }
    
    cout << playersToRemove << endl;

    return 0;
}