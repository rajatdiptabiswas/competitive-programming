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


int main(int argc, char const *argv[]) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    vector<vector<int>> graph(3, vector<int>());

    REP(i, 3) {
        string s;
        cin >> s;
        if (s[1] == '<') {
            graph[s[0] - 'A'].PB(s[2] - 'A');
        } else if (s[1] == '>') {
            graph[s[2] - 'A'].PB(s[0] - 'A');
        }
    }

    vector<int> indegree(3);

    for (vector<int> u : graph) {
        for (int v : u) {
            indegree[v]++;
        }
    }

    deque<char> q;

    REP(i, 3) {
        if (indegree[i] == 0) {
            q.push_back(i);
        }
    }

    stringstream resultStream;

    while (!q.empty()) {
        int u = q.front();
        q.pop_front();
        resultStream << (char)(u + 'A');
        for (int v : graph[u]) {
            indegree[v]--;
            if (indegree[v] == 0) {
                q.push_back(v);
            }
        }
    }

    string result = resultStream.str();

    if (result.size() != 3) {
        cout << "Impossible" << endl;
    } else {
        cout << result << endl;
    }

    return 0;
}