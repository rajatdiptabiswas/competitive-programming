class Solution:
    ans = []

    def get_ans_grid(self, grid: List[str]) -> List[str]:
        n = len(grid)
        grid_string = []
        for y in range(n):
            string = ''
            for x in range(n):
                if grid[y][x]:
                    string += 'Q'
                else:
                    string += '.'
            grid_string.append(string)
        return grid_string


    def in_grid(self, x: int, y: int, grid: List[str]) -> bool:
        return 0 <= x < len(grid) and 0 <= y < len(grid)


    def is_safe(self, x: int, y: int, grid: List[str]) -> bool:
        for i in range(1, y + 1):
            if self.in_grid(x - i, y - i, grid) and grid[y - i][x - i] or \
               self.in_grid(x + i, y - i, grid) and grid[y - i][x + i] or \
               self.in_grid(x, y - i, grid) and grid[y - i][x]:
                return False
        return True


    def n_queens(self, grid: List[str], y=0) -> None:
        n = len(grid)

        if y == n:
            self.ans.append(self.get_ans_grid(grid))
            return

        for x in range(n):
            if self.is_safe(x, y, grid):
                grid[y][x] = True
                self.n_queens(grid, y + 1)
                grid[y][x] = False
        return
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ans = []
        
        grid = [[False for i in range(n)] for j in range(n)]
        self.n_queens(grid)

        return self.ans