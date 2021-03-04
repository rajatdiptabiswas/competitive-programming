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

    unordered_map<char, int> heavy;
    unordered_map<char, int> light;

    REP(i, 3) {
        string s;
        cin >> s;
        if (s[1] == '<') {
            heavy[s[2]]++;
            light[s[0]]++;
        } else if (s[1] == '>') {
            heavy[s[0]]++;
            light[s[2]]++;
        }
    }

    if (light['A'] == 1 && light['B'] == 1 && light['C'] == 1) {
        cout << "Impossible" << endl;
        return 0;
    }

    char lightest, heaviest;
    for (pair<char, int> p : light) {
        if (p.second == 2) {
            lightest = p.first;
        }
    }
    for (pair<char, int> p : heavy) {
        if (p.second == 2) {
            heaviest = p.first;
        }
    }

    unordered_set<char> abc = {'A', 'B', 'C'};
    abc.erase(lightest);
    abc.erase(heaviest);

    char middle = *abc.begin();

    stringstream ss;
    ss << lightest << middle << heaviest;

    cout << ss.str() << endl;

    return 0;
}