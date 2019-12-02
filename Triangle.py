class Triangle:
    def __init__(self, a, b, c):
        self._a, self._b, self._c = sorted([a, c, b])

    def _is_equilateral__(self):
        return self._a == self._b and self._b == self._c

    def __str__(self):
        sufix = " is equilateral" if self._is_equilateral__() else ""
        return "Triangle sides length: %d, %d, %d%s" % (self._a, self._b, self._c, sufix)
