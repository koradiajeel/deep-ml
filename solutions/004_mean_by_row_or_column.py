"""Deep-ML #4: Calculate Mean by Row or Column.

Return the mean of each row (mode="row") or each column (mode="column")
of matrix `a`.
"""


def calculate_matrix_mean(a: list[list[float]], mode: str) -> list[float]:
    if mode == "row":
        return [sum(row) / len(row) for row in a]
    if mode == "column":
        return [sum(col) / len(col) for col in zip(*a)]
    raise ValueError("mode must be 'row' or 'column'")


if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert calculate_matrix_mean(m, "column") == [4.0, 5.0, 6.0]
    assert calculate_matrix_mean(m, "row") == [2.0, 5.0, 8.0]
    assert calculate_matrix_mean([[1, 2], [3, 4], [5, 6]], "column") == [3.0, 4.0]
    try:
        calculate_matrix_mean(m, "diagonal")
        raise AssertionError("expected ValueError")
    except ValueError:
        pass
    print("All tests passed.")
