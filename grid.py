from cell import Cell


class Grid:

    width: int
    height: int
    board: list[list[Cell]]
    stack: list[tuple]

    def __init__(self, width: int, height: int) -> None:
        self.w = width
        self.h = height
        self.board = [[Cell(x, y, False) for x in range(width)] for y in range(height)]
        self.stack = []

    def set_configuration(self, loc: list[tuple]) -> None:
        for i, j in loc:
            self.board[j][i].alive = not self.board[j][i].alive

    def get_neighbour_count(self, cell: Cell) -> int:
        n_count = 0
        x, y = cell.x, cell.y
        configs = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y),
                   (x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x + 1, y)]
        for j, i in configs:
            if (0 <= i < self.h and 0 <= j < self.w) and self.board[i][j].alive:
                n_count += 1
        return n_count

    def update(self) -> None:
        for i in range(self.h):
            for j in range(self.w):
                cell = self.board[i][j]
                n_count = self.get_neighbour_count(cell)
                cell.update(n_count, self.stack)
        while self.stack:
            x, y = self.stack.pop(0)
            self.board[y][x].alive = not self.board[y][x].alive
