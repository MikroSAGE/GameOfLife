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

    def toggle_cells(self, loc: list[tuple]) -> None:
        for i, j in loc:
            self.board[j][i].alive = not self.board[j][i].alive

    def update(self) -> None:
        for i in range(self.h):
            for j in range(self.w):
                self.board[i][j].update_stack(self)
        while self.stack:
            x, y = self.stack.pop(0)
            self.board[y][x].alive = not self.board[y][x].alive
