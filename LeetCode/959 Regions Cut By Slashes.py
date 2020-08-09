#!/usr/bin/env python3

from typing import List


class UF:
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, p: int) -> int:
        while p != self.parent[p]:
            p = self.parent[self.parent[p]]
        return p

    def union(self, p: int, q: int) -> None:
        root_p = self.find(p)
        root_q = self.find(q)

        if root_p == root_q:
            return

        if self.size[root_p] <= self.size[root_q]:
            self.parent[root_p] = root_q
            self.size[root_q] += self.size[root_p]
        else:
            self.parent[root_q] = root_p
            self.size[root_p] += self.size[root_q]

    def connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)

    def components(self) -> int:
        return len(set([self.find(x) for x in self.parent]))


class Solution:
    def _get_root(self, row: int, col: int, n: int) -> int:
        return ((n * row) + col) * 4

    def _left_index(self, root: int) -> int:
        return root

    def _up_index(self, root: int) -> int:
        return root + 1

    def _right_index(self, root: int) -> int:
        return root + 2

    def _down_index(self, root: int) -> int:
        return root + 3

    def regionsBySlashes(self, grid: List[str]) -> int:
        """
        divide each block in the grid into 4 regions
                1
            0       2
                3

        for a 2 x 2 grid
                1           5
            0       2   4       6
                3           7
                9           13
            8       10  12      14
                11          15

        for each block
        if '/' or ' ' encountered
            connect 0,1; 2,3
        if '\' or ' ' encountered
            connect 1,2; 0,3

        connect the grid blocks using
        3,9; 2,4; 7,13; 10,12
        only connect the right block and the bottom block for each block
        (also check if right and bottom block not out of bound)

        return the number of components
        """
        n = len(grid)
        uf = UF(n * n * 4)

        for row in range(n):
            for col in range(n):
                root = self._get_root(row, col, n)

                # connect regions inside the grid block
                if grid[row][col] == '/' or grid[row][col] == ' ':
                    uf.union(self._up_index(root), self._left_index(root))
                    uf.union(self._right_index(root), self._down_index(root))
                if grid[row][col] == '\\' or grid[row][col] == ' ':
                    uf.union(self._up_index(root), self._right_index(root))
                    uf.union(self._left_index(root), self._down_index(root))

                # connect regions of different grid blocks
                # (only blocks to the right and bottom)
                # check if the block has blocks to the right of it
                # i.e. not the right-most row
                if col % n != n - 1:
                    right_root = root + 4
                    uf.union(self._right_index(root), self._left_index(right_root))
                # check if the block has blocks below it
                # i.e. not the bottom-most row
                if row % n != n - 1:
                    down_root = root + (4 * n)
                    uf.union(self._down_index(root), self._up_index(down_root))

        return uf.components()


def main():
    solve = Solution()
    grid = ["\\/", "/\\"]
    print(solve.regionsBySlashes(grid))


if __name__ == '__main__':
    main()
