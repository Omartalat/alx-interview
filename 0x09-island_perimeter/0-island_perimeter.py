#!/usr/bin/python3
"""
Calculate the perimeter of an island represented by a grid.

The grid is a list of lists of integers where:
- 0 represents water
- 1 represents land

The function uses Depth-First Search (DFS) to traverse
the island and calculate its perimeter.

Args:
    grid (list of list of int): The grid representing the island.

Returns:
    int: The perimeter of the island.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.
    The grid is represented by a list of lists of integers where:
    - 0 represents water
    - 1 represents land
    The function uses depth-first search (DFS) to traverse the island and
    calculate its perimeter by counting the edges that are either water or
    out of bounds.
    Args:
        grid (List[List[int]]): A 2D list representing the grid.
    Returns:
        int: The perimeter of the island.
    """

    visits = set()

    def dsf(i, j):
        """
        Depth-First Search (DFS) helper function to
        calculate the perimeter of an island in a grid.
        Args:
            i (int): The row index of the current cell.
            j (int): The column index of the current cell.
        Returns:
            int: The perimeter contribution of the current cell.

        The function checks the boundaries of the grid and
        whether the current cell is water (0) or land (1).

        If the cell is water or out of bounds,
        it contributes 1 to the perimeter.

        If the cell has already been visited,
        it contributes 0 to the perimeter.

        The function recursively explores the neighboring cells
        (right, down, left, up) and sums up their perimeter contributions.
        """

        if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or\
                grid[i][j] == 0:
            return 1
        if (i, j) in visits:
            return 0

        visits.add((i, j))
        perim = dsf(i, j + 1)
        perim += dsf(i + 1, j)
        perim += dsf(i, j - 1)
        perim += dsf(i - 1, j)

        return perim

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                return dsf(i, j)
