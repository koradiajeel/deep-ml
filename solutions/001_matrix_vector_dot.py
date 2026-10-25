"""Deep-ML #1: Matrix-Vector Dot Product.

Return the dot product of matrix `a` (n x m) and vector `b` (length m),
or -1 if the dimensions are incompatible.
"""


def matrix_dot_vector(a: list[list[float]], b: list[float]) -> list[float] | int:
    if not a or any(len(row) != len(b) for row in a):
        return -1
    return [sum(x * y for x, y in zip(row, b)) for row in a]


if __name__ == "__main__":
    assert matrix_dot_vector([[1, 2], [2, 4]], [1, 2]) == [5, 10]
    assert matrix_dot_vector([[1, 2, 3], [2, 4, 5], [6, 8, 9]], [1, 2, 3]) == [14, 25, 49]
    assert matrix_dot_vector([[1, 2], [2, 4], [6, 8], [12, 4]], [1, 2, 3]) == -1
    print("All tests passed.")
