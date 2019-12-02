class Triangle:
    def __init__(self, a, b, c):
        self._shortest_side, self._middle_side, self._longest_side = sorted([a, c, b])

    def _is_equilateral__(self):
        return self._shortest_side == self._middle_side and self._middle_side == self._longest_side

    def _is_isosceles__(self):
        return self._shortest_side == self._middle_side or self._middle_side == self._longest_side

    def __str__(self):
        sufix = " is equilateral" if self._is_equilateral__() else " is isosceles" if self._is_isosceles__() else ""
        return "Triangle sides length: %d, %d, %d%s" % (self._shortest_side, self._middle_side, self._longest_side, sufix)
