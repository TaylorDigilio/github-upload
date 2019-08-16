# first day activity
import numpy as np
import random

length = random.randint(5, 10)
width = random.randint(5, 10)


def myGrid(length, width):
    x = length
    y = width
    grid = np.random.randint(2, size=(x, y))
    print(grid)


def fewer_than_two(grid):
    count = 0
    newGrid = grid

    return grid


def get_cell_state(num_alive_neighbors, current_state):
    if current_state == 1:
        if num_alive_neighbors == 2 or num_alive_neighbors == 3:
            return 1
        return 0
    else:
        if num_alive_neighbors == 3:
            return 1
        return 0
