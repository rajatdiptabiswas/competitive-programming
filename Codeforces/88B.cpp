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
 
 
// calculate euclidean distance
double euclideanDistance(pair<int, int> point1, pair<int, int> point2) {
    int x1 = point1.first, y1 = point1.second;
    int x2 = point2.first, y2 = point2.second;
    int x = x1 - x2, y = y1 - y2;
    return sqrt(pow(x, 2) + pow(y, 2));
}
 
// check if minimum distance between shift key and current key is within the allowed maximum distance
bool isWithinShiftDistance(char c, int distance, unordered_map<char, vector<pair<int, int>>>& keyboard) {
    double minDistance = numeric_limits<double>::max();
    for (pair<int, int> sCoordinate : keyboard['S']) {
        for (pair<int, int> cCoordinate : keyboard[c]) {
            MIN(minDistance, euclideanDistance(sCoordinate, cCoordinate));
            if (minDistance <= 1.0 * distance) {
                return true;
            }
        }
    }
    return false;
}
 
int main(int argc, char const *argv[]) {
    FASTIO;
 
    int n, m, x;
    cin >> n >> m >> x;
    unordered_map<char, vector<pair<int, int>>> keyboard;
    REP(i, n) {
        string row;
        cin >> row;
        REP(j, m) {
            char c = row[j];
            keyboard[c].PB(MP(i, j));
        }
    }

    // cache whether second hand required for capital key
    vector<bool> isSecondHandRequired(26, false);
    if (CONTAINS(keyboard, 'S')) {
        for (pair<char, vector<pair<int, int>>> keyboardEntry : keyboard) {
            char c = keyboardEntry.F;
            if (c != 'S') {
                isSecondHandRequired[c - 'a'] = !isWithinShiftDistance(c, x, keyboard);
            }
        }
    }

    int q;
    cin >> q;
    string input;
    cin >> input;
 
    bool canTypeText = true;
    int secondHandUseCount = 0;
    REP(i, q) {
        char c = input[i];
        if (islower(c)) {
            // check if current key present in keyboard
            if (!CONTAINS(keyboard, c)) {
                canTypeText = false;
                break;
            }
        } else {
            c = tolower(c);
            // check if both shift key and current key present in keyboard
            if (!CONTAINS(keyboard, 'S') || !CONTAINS(keyboard, c)) {
                canTypeText = false;
                break;
            } else {
                // use second hand if key outside maximum distance
                if (isSecondHandRequired[c - 'a']) {
                    secondHandUseCount++;
                }
            }
        }
    }
 
    if (canTypeText) {
        cout << secondHandUseCount << endl;
    } else {
        cout << -1 << endl;
    }
 
    return 0;
}