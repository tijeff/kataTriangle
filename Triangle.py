class Triangle:
    def __init__(self, a, b, c):
        self._a, self._b, self._c = sorted([a, c, b])

    def __str__(self):
        sufix = " is equilateral" if self._a == self._b and self._b == self._c else ""
        return "Triangle sides length: %d, %d, %d%s" % (self._a, self._b, self._c, sufix)
