def geron(a, b, c):

    s = (a + b + c) / 2

    triangle = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return triangle