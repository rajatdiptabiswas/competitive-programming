#!/usr/bin/env python3


# def sort_closest_points(point: tuple, points_arr: list) -> list:
#     return sorted(points_arr, key=lambda p: ((p[0]-point[0])**2 + (p[1]-point[1])**2)**0.5)


def euclidean_dist(point1: tuple, point2: tuple) -> float:
    return ((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)**0.5


def main():
    t = int(input())

    for testcase in range(t):
        x, y = map(int, input().split())
        sc = (x,y)
        n, m, k = map(int, input().split())
        n_input = [int(a) for a in input().split()]
        n_arr = []
        for p in range(0, 2*n, 2):
            n_arr.append((n_input[p], n_input[p+1]))
        m_input = [int(b) for b in input().split()]
        m_arr = []
        for q in range(0, 2*m, 2):
            m_arr.append((m_input[q], m_input[q+1]))
        k_arr = []
        k_input = [int(c) for c in input().split()]
        for r in range(0, 2*k, 2):
            k_arr.append((k_input[r], k_input[r+1]))

        # case 1
        # sc = (1,4)
        # n,m,k = 3,2,2
        # n_arr = [(4, 4), (2, 0), (8, 1)]
        # m_arr = [(10, 1), (3, 1)]
        # k_arr = [(1, 3), (9, 5)]

        # print(sc)
        # print(n,m,k)

        # case 2
        # sc = (6,4)
        # n,m,k = 2,2,3
        # n_arr = [(7, 10), (5, 7)]
        # m_arr = [(1, 6), (2, 3)]
        # k_arr = [(1, 8), (0, 7), (0, 2)]

        # make euclidean distance table of n x m
        dist_nm_table = [[0 for col in range(m)] for row in range(n)]
        for row in range(n):
            for col in range(m):
                dist_nm_table[row][col] = euclidean_dist(n_arr[row], m_arr[col])

        dist_nm = float('inf')

        # sc -> n -> m -> k
        for p in range(n):
            dist_nm_temp = euclidean_dist(sc, n_arr[p])
            if dist_nm < dist_nm_temp:
                continue
            for q in range(m):
                dist_nm_temp = euclidean_dist(sc, n_arr[p])
                dist_nm_temp += dist_nm_table[p][q]
                if dist_nm < dist_nm_temp:
                    continue
                for r in range(k):
                    dist_nm_temp = euclidean_dist(sc, n_arr[p]) + dist_nm_table[p][q]
                    dist_nm_temp += euclidean_dist(m_arr[q], k_arr[r])
                    dist_nm = min(dist_nm_temp, dist_nm)

        dist_mn = float('inf')

        # sc -> m -> n -> k
        for p in range(m):
            dist_mn_temp = euclidean_dist(sc, m_arr[p])
            if dist_mn < dist_mn_temp:
                continue
            for q in range(n):
                dist_mn_temp = euclidean_dist(sc, m_arr[p])
                dist_mn_temp += dist_nm_table[q][p]
                if dist_mn < dist_mn_temp:
                    continue
                for r in range(k):
                    dist_mn_temp = euclidean_dist(sc, m_arr[p]) + dist_nm_table[q][p]
                    dist_mn_temp += euclidean_dist(n_arr[q], k_arr[r])
                    dist_mn = min(dist_mn_temp, dist_mn)

        print(min(dist_nm, dist_mn))


if __name__ == '__main__':
    main()
