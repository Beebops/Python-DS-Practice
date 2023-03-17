def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    sum = 0

    # iterate through length of matrix
    for index in range(len(matrix)):
        # add to sum the val at current index of current list
        sum += matrix[index][index]
        # add to sum the val at current index of last item of current index
        sum += matrix[index][-1 - index]

    return sum

m1 = [
    [1, 2],
    [30, 40]
]

m2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(sum_up_diagonals(m1))
print(sum_up_diagonals(m2))