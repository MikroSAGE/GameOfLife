# Conway's Game of Life in Python

This repository contains a Python implementation of Conway's Game of Life, a cellular automaton devised by mathematician John Conway. The Game of Life is a zero-player game, meaning that its evolution is determined by its initial state, and no further input is required. The game consists of a grid of cells, each of which can be in one of two states: alive or dead. The cells evolve over generations based on simple rules.

## Rules of Conway's Game of Life

1. **Underpopulation:** A living cell with fewer than two living neighbors dies due to loneliness.
2. **Survival:** A living cell with two or three living neighbors survives to the next generation.
3. **Overpopulation:** A living cell with more than three living neighbors dies due to overcrowding.
4. **Reproduction:** A dead cell with exactly three living neighbors becomes a living cell through reproduction.

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone the repository:

  ```bash
  git clone https://github.com/MikroSAGE/GameOfLife
  ```

2. Navigate to the project directory

  ```bash
  cd GameOfLife
  ```

### Usage

Run the main script to start the simulation:

  ```bash
  python main.py
  ```

This will execute the Game of Life simulation with a random initial state. You can customize the initial state or modify the script to load specific patterns.

### Customization

You can customize the following parameters in the `game_of_life.py` script:

- **GRID_SIZE:** Adjust the size of the grid (number of rows and columns).
- **INITIAL_PATTERN:** Choose the initial pattern (random, glider, blinker, etc.).
- **GENERATIONS:** Set the number of generations to simulate.

Feel free to modify the code and experiment with different patterns or settings.

## Examples

Here are some examples of popular patterns that you can try:

- **Glider:**
  ```python
  INITIAL_PATTERN = [
      [0, 1, 0],
      [0, 0, 1],
      [1, 1, 1],
  ]
  ```

- **Toad:**

  ```python
  INITIAL_PATTERN = [
      [0, 1, 1, 1],
      [1, 1, 1, 0],
  ]
  ```
  
Explore and create your own patterns!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- John Conway for creating the Game of Life.
- The open-source community for inspiring and contributing to the world of cellular automata.
