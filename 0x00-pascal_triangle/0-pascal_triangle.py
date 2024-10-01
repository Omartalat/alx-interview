#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n:

    Returns an empty list if n <= 0
    You can assume n will be always an integer
    """
    arr = []
    if n <= 0:
        return arr

    arr = [[1]]
    for i in range(1, n):
        temp = [0] + arr[-1] + [0]
        row = []
        for j in range(len(arr[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        arr.append(row)
    return arr
