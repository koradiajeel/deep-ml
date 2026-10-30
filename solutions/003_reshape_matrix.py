"""Deep-ML #3: Reshape Matrix.

Reshape matrix `a` into `new_shape` (rows, cols), reading elements in
row-major order. Return [] if the total number of elements doesn't match.
"""


def reshape_matrix(a: list[list[float]], new_shape: tuple[int, int]) -> list[list[float]]:
    rows, cols = new_shape
    flat = [x for row in a for x in row]
    if len(flat) != rows * cols:
        return []
    return [flat[r * cols:(r + 1) * cols] for r in range(rows)]


if __name__ == "__main__":
    assert reshape_matrix([[1, 2, 3, 4], [5, 6, 7, 8]], (4, 2)) == [[1, 2], [3, 4], [5, 6], [7, 8]]
    assert reshape_matrix([[1, 2, 3, 4], [5, 6, 7, 8]], (1, 8)) == [[1, 2, 3, 4, 5, 6, 7, 8]]
    assert reshape_matrix([[1, 2], [3, 4]], (4, 1)) == [[1], [2], [3], [4]]
    assert reshape_matrix([[1, 2, 3, 4], [5, 6, 7, 8]], (3, 3)) == []
    print("All tests passed.")
