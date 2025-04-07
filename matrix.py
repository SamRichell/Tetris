"""
This file contains code for the matrix
The matrix is seperated into minos
Height and width of the grid is determined when the matrix is defined
Only the matrix should be exported from this file
"""

import pygame

class _Mino:
    def __init__(self, length, screen, x, y, fill):
        self.__screen = screen
        self.__length = length
        self.__x = x
        self.__y = y
        self.__fill = fill

    def render(self):    # Draw 4 lines representing the edge of each square
        pygame.draw.rect(self.__screen, self.__fill, (self.__x, self.__y, self.__length, self.__length))
        pygame.draw.line(self.__screen, "white", [self.__x, self.__y], [self.__x, self.__y + self.__length])
        pygame.draw.line(self.__screen, "white", [self.__x, self.__y], [self.__x + self.__length, self.__y])
        pygame.draw.line(self.__screen, "white", [self.__x, self.__y + self.__length], [self.__x + self.__length, self.__y + self.__length])
        pygame.draw.line(self.__screen, "white", [self.__x + self.__length, self.__y], [self.__x + self.__length, self.__y + self.__length])

    def update(self, colour):
        self.__fill = colour

class Matrix:
    def __init__(self, screen, width, height, mino_length):
        self.__screen = screen
        self.__width = width
        self.__height = height
        self.__mino_length = mino_length
        self.__squares = []
        self.__centre()
        self.__initiate_squares()

    def __initiate_squares(self):    # Initiate squares array
        start_x = self.__x
        y = self.__y
        x = start_x
        for i in range (0, (self.__height)):
            new_line = []
            for j in range(0, self.__width):
                new_line.append(_Mino(self.__mino_length, self.__screen, x, y, "black"))
                if x < (((self.__width - 1) * self.__mino_length) + self.__x):
                    x += self.__mino_length
                else:
                    x = start_x
                    y += self.__mino_length
            self.__squares.append(new_line)

    def __centre(self):    # Find pixel position of top left of container
        self.__x = (self.__screen.get_width() // 2) - ((self.__width // 2) * self.__mino_length)
        print(self.__x)
        self.__y = (self.__screen.get_height() // 2) - ((self.__height // 2) * self.__mino_length)
        print(self.__y)

    def render(self):    # Render box then squares
        pygame.draw.line(self.__screen, "white", [self.__x, self.__y - (self.__mino_length // 2)], [self.__x, self.__y + (self.__height * self.__mino_length)])
        pygame.draw.line(self.__screen, "white", [self.__x, self.__y + (self.__height * self.__mino_length)], [self.__x + (self.__width * self.__mino_length), self.__y + (self.__height * self.__mino_length)])
        pygame.draw.line(self.__screen, "white", [self.__x + (self.__width * self.__mino_length), self.__y - (self.__mino_length // 2)], [self.__x + (self.__width * self.__mino_length), self.__y + (self.__height * self.__mino_length)])
        for line in self.__squares:
            for square in line:
                square.render()

    def summon_tetrimino(self, tetrimino):
        shape = tetrimino.get_shape()
        count = 0
        for line in shape:
            if line[0] == 1:
                self.__squares[count][(self.__width // 2) - 1].update(tetrimino.get_colour())
            if line[1] == 1:
                self.__squares[count][self.__width // 2].update(tetrimino.get_colour())
            count += 1

    def __move_down(self):
        for i in range (0, (self.__squares.length() - self.__width), -1):
            print()