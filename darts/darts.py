def score(x, y):
    radius = x ** 2 + y ** 2

    if radius > 100:
        return 0
    if 25 < radius <= 100:
        return 1
    if 1 < radius <= 25:
        return 5
    if radius <= 1:
        return 10
