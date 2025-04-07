o_shape = [[1, 1], [1, 1]]

l_shape = [[1, 0], [1, 0], [1, 1]]

j_shape = [[0, 1], [0, 1], [1, 1]]

s_shape = [[1, 0], [1, 1], [0, 1]]

z_shape = [[0, 1], [1, 1], [1, 0]]

t_shape = [[1, 0], [1, 1], [1, 0]]

i_shape = [[1, 0], [1, 0], [1, 0], [1, 0]]


class Tetrimino:
    def __init__(self, shape, colour):
        self.__shape = shape
        self.__colour = colour

    def get_shape(self):
        return self.__shape
    
    def get_colour(self):
        return self.__colour


class OShape(Tetrimino):
    def __init__(self):
        super().__init__(o_shape, "yellow")

class LShape(Tetrimino):
    def __init__(self):
        super().__init__(l_shape, "orange")

class JShape(Tetrimino):
    def __init__(self):
        super().__init__(j_shape, "blue")

class SShape(Tetrimino):
    def __init__(self):
        super().__init__(s_shape, "green")

class ZShape(Tetrimino):
    def __init__(self):
        super().__init__(z_shape, "red")

class TShape(Tetrimino):
    def __init__(self):
        super().__init__(t_shape, "purple")

class IShape(Tetrimino):
    def __init__(self):
        super().__init__(i_shape, "cyan")