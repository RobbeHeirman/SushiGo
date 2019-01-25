class Coordinate:
    _x: int
    _y: int

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __getitem__(self, index):

        if index == 0:
            return self._x
        else:
            return self._y

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, x_val):

        if x_val < 0:
            raise ValueError("x of coordinate is {0} < 0. Not allowed.".format(x_val))

        self._x = x_val

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, y_val):

        if y_val < 0:
            raise ValueError("y of coordinate is {0} < 0. Not allowed.".format(y_val))

        self._y = y_val
