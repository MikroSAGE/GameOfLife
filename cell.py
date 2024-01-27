

class Cell:
    x: int
    y: int
    alive: bool

    def __init__(self, x: int, y: int, alive: bool) -> None:
        self.x = x
        self.y = y
        self.alive = alive

    def update(self, n_count: int, stack: list[tuple]) -> None:
        # any living cell with less than 2 or more than 3 neighbours die
        if self.alive:
            if n_count < 2 or n_count > 3:
                stack.append((self.x, self.y))
        # any dead cell with exactly 3 neighbours comes to life
        else:
            if n_count == 3:
                stack.append((self.x, self.y))