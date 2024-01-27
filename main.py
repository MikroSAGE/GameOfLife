import pygame
import random
from grid import Grid

GRID_SIZE = (128, 72)
INITIAL_CONFIG = []
GENERATIONS = 0


def display(screen: pygame.display, grid: Grid, cell_size: int) -> None:
    y = 0
    for i in range(grid.h):
        x = 0
        for j in range(grid.w):
            m_rect = pygame.Rect(x, y, cell_size, cell_size)
            s_rect = pygame.Rect(x + 0.5, y + 0.5, cell_size - 1, cell_size - 1)

            if grid.board[i][j].alive:
                pygame.draw.rect(screen, "white", m_rect)
            else:
                pygame.draw.rect(screen, "#051326", m_rect)
                pygame.draw.rect(screen, "#000d21", s_rect)
            x += cell_size
        y += cell_size


def shift_config(config: list[tuple], x_shift: int, y_shift: int):
    return [(x + x_shift, y + y_shift) for x, y in config]


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    width, height = GRID_SIZE
    random_config = [(random.randint(0, width-1), random.randint(0, height-1)) for _ in range(2000)]
    new_grid = Grid(width, height)
    new_grid.set_configuration(INITIAL_CONFIG if INITIAL_CONFIG else random_config)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display(screen, new_grid, 10)
        new_grid.update()

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()


if __name__ == "__main__":
    main()
