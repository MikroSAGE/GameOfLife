from grid import Grid


class Cell:

    x: int
    y: int
    alive: bool

    def __init__(self, x: int, y: int, alive: bool) -> None:
        self.x = x
        self.y = y
        self.alive = alive

    def get_neighbour_count(self, grid: Grid) -> int:
        n_count = 0
        x, y = self.x, self.y
        configs = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y),
                   (x-1, y+1), (x, y+1), (x+1, y+1), (x+1, y)]
        for j, i in configs:
            if (0 <= i < grid.h and 0 <= j < grid.w) and grid.board[i][j].alive:
                n_count += 1
        return n_count

    def update_stack(self, grid: Grid) -> None:
        n_count = self.get_neighbour_count(grid)
        if self.alive:  # any living cell with less than 2 or more than 3 neighbours die
            if n_count < 2 or n_count > 3:
                grid.stack.append((self.x, self.y))
        else:  # any dead cell with exactly 3 neighbours comes to life
            if n_count == 3:
                grid.stack.append((self.x, self.y))