"""Deep-ML #2: Transpose of a Matrix.

Return the transpose of matrix `a` (n x m), producing an m x n matrix.
"""


def transpose_matrix(a: list[list[float]]) -> list[list[float]]:
    return [list(col) for col in zip(*a)]


if __name__ == "__main__":
    assert transpose_matrix([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert transpose_matrix([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]]
    assert transpose_matrix([[7]]) == [[7]]
    assert transpose_matrix([]) == []
    print("All tests passed.")
