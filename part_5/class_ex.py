class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def ret_xy(self):
        return self.x, self.y

    def __repr__(self):
        return f'Coordinate({self.x}, {self.y})'

    def __str__(self):
        return f'x={self.x}, y={self.y}'

    @len
