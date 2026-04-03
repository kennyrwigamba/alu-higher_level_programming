#!/usr/bin/python3
"""Generate Pascal's triangle."""


def pascal_triangle(n):
    """Return Pascal's triangle of size n as a list of lists."""
    if n <= 0:
        return []

    triangle = []
    for row_index in range(n):
        if row_index == 0:
            triangle.append([1])
            continue

        prev_row = triangle[row_index - 1]
        row = [1]
        for col_index in range(1, row_index):
            row.append(prev_row[col_index - 1] + prev_row[col_index])
        row.append(1)
        triangle.append(row)

    return triangle
