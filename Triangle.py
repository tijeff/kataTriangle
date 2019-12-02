class Triangle:
    def __init__(self, a, b, c):
        self._a, self._b, self._c = sorted([a, c, b])

    def __str__(self):
        return "Triangle sides length: %d, %d, %d" % (self._a, self._b, self._c)
