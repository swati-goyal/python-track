def square_of_sum(n):
    result = (n * (n + 1)) / 2
    return result * result


def sum_of_squares(n):
    return (n * (n + 1) * (2 * n + 1)) / 6


def difference_of_squares(n):
    return square_of_sum(n) - sum_of_squares(n)
