#!/usr/bin/python3
"""
Module to calculate the perimeter of the island in a given grid.
"""


def island_perimeter(grid):
    """
    Function to calculate the perimeter of the island in a given grid.

    Args:
        grid (list): List of lists of integers representing the island.

    Returns:
        int: Perimeter of the island.
    """

    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4  # Start with assuming a full perimeter

                # Check adjacent cells and reduce perimeter for each adjacent land
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
